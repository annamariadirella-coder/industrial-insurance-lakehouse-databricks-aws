# Day 3 Feature Table Design

## Table

`insurance_lakehouse.gold.gold_claim_fraud_features`

## Purpose

The purpose of this table is to create an AI-ready claim-level feature table for future fraud-risk modelling or analytical scoring.

No model is trained on Day 3. The goal is to prepare clean, validated, business-ready features at the correct grain.

## Grain

One row per claim.

Primary grain column:

- claim_id

Validation result:

- rows: 50000
- distinct claim_id: 50000
- duplicate claim_id count: 0

## Input tables

The feature table is built from trusted Silver tables:

- `silver_claims`
- `silver_policies`
- `silver_customers`
- `silver_payments`
- `silver_fraud_indicators`

## Design decisions

### 1. Payment data is aggregated before joining

Payments can have multiple rows per claim.

To avoid duplicating claim rows, payments are first aggregated by `claim_id`.

Derived payment features:

- total_paid_amount
- payment_count
- payment_rejection_count
- first_payment_date
- payment_delay_days

### 2. Customer PII is not exposed

The feature table does not expose raw customer PII.

Excluded fields:

- first_name
- last_name
- email
- phone_number
- street
- postal_code
- date_of_birth

Included customer fields:

- customer_id
- customer_age
- bundesland

### 3. Risk score is transformed into a risk band

The `risk_score` field is converted into a human-readable category:

| Risk band | Logic |
|---|---|
| low | risk_score < 30 |
| medium | risk_score >= 30 and risk_score < 70 |
| high | risk_score >= 70 |

## Feature list

| Feature | Source | Formula / logic |
|---|---|---|
| claim_amount | silver_claims | Original claim amount |
| premium_amount | silver_policies | Policy premium |
| coverage_amount | silver_policies | Policy coverage |
| claim_amount_to_coverage_ratio | derived | claim_amount / coverage_amount |
| policy_age_days | derived | claim_date - policy start_date |
| customer_age | silver_customers | GDPR-safe customer age |
| bundesland | silver_customers | Regional feature |
| total_paid_amount | silver_payments | sum(payment_amount) by claim_id |
| payment_count | silver_payments | count payments by claim_id |
| payment_rejection_count | silver_payments | count rejected payments |
| first_payment_date | silver_payments | min(payment_date) |
| payment_delay_days | derived | first_payment_date - claim_date |
| previous_claims_count | silver_fraud_indicators | Historical claim signal |
| suspicious_amount_flag | silver_fraud_indicators | Fraud signal |
| duplicate_claim_flag | silver_fraud_indicators | Fraud signal |
| late_report_flag | silver_fraud_indicators | Fraud signal |
| high_risk_region_flag | silver_fraud_indicators | Fraud signal |
| risk_score | silver_fraud_indicators | Fraud risk score from 0 to 100 |
| risk_band | derived | low / medium / high |

## Null handling

Missing payment values are filled with safe defaults:

- total_paid_amount = 0
- payment_count = 0
- payment_rejection_count = 0

Missing fraud indicator values are filled with safe defaults:

- previous_claims_count = 0
- boolean fraud flags = false
- risk_score = 0

## Validation

The final table was validated with a duplicate grain check.

Result:

| Check | Result |
|---|---|
| row count | 50000 |
| distinct claim_id | 50000 |
| duplicate claim_id count | 0 |
| grain status | PASS |

## Day 3 readiness

The feature table is ready for Day 4 dashboarding and future AI/fraud-risk modelling use cases.