# Day 3 Feature Table Profile

## Table

`insurance_lakehouse.gold.gold_claim_fraud_features`

## Purpose

This table is an AI-ready fraud feature table.

It prepares claim-level insurance data for future fraud-risk modelling or analytical scoring.

## Grain

One row per claim.

## Row count

| Metric | Count |
|---|---:|
| rows | 50000 |
| distinct claim_id | 50000 |
| duplicate claim_id count | 0 |

## Main input tables

- `silver_claims`
- `silver_policies`
- `silver_customers`
- `silver_payments`
- `silver_fraud_indicators`

## Feature columns

| Feature | Meaning |
|---|---|
| claim_amount | Original claim amount |
| premium_amount | Policy premium amount |
| coverage_amount | Policy coverage amount |
| claim_amount_to_coverage_ratio | Claim amount divided by coverage amount |
| policy_age_days | Days between policy start date and claim date |
| customer_age | Customer age from GDPR-safe Silver customer profile |
| total_paid_amount | Total payment amount linked to the claim |
| payment_count | Number of valid payment records linked to the claim |
| payment_rejection_count | Number of rejected payments linked to the claim |
| payment_delay_days | Days between claim date and first payment date |
| previous_claims_count | Previous claims indicator from fraud signals |
| suspicious_amount_flag | Fraud signal flag |
| duplicate_claim_flag | Fraud signal flag |
| late_report_flag | Fraud signal flag |
| high_risk_region_flag | Fraud signal flag |
| risk_score | Fraud risk score from 0 to 100 |
| risk_band | Low, medium, or high risk category |

## PII handling

The feature table does not expose raw customer PII such as:

- first_name
- last_name
- email
- phone_number
- street
- date_of_birth

The table uses operational IDs and analytics-safe fields only.

## Validation result

The feature table passed the grain validation.

Status: PASS