# Day 3 Gold Business Logic

## Purpose of the Gold layer

The Gold layer turns trusted Silver insurance data into business-ready analytics, KPI tables, fraud-risk summaries, agent performance outputs, and AI-ready feature tables.

Gold tables are not copies of Silver tables. Each Gold table has a defined business purpose, a clear grain, and validated KPIs or features.

---

## Gold tables

### gold_claims_overview

**Business purpose**

Support claims operations analytics by summarizing claim volume, claim amounts, claim statuses, claim types, product types, and regional patterns.

**Audience**

Claims operations team, insurance analysts, BI users.

**Input tables**

- silver_claims
- silver_policies
- silver_customers
- silver_fraud_indicators

**Grain**

One row per:

- claim_month
- claim_status
- claim_type
- policy_type
- bundesland

**Main KPIs**

- total_claims
- total_claim_amount
- avg_claim_amount
- fraud_flag_rate
- avg_risk_score

**Output table**

`insurance_lakehouse.gold.gold_claims_overview`

---

### gold_policy_performance

**Business purpose**

Support portfolio and premium analytics by showing how policy types, statuses, sales channels, and regions perform.

**Audience**

Portfolio managers, product teams, executive reporting.

**Input tables**

- silver_policies
- silver_customers
- silver_agents

**Grain**

One row per:

- policy_type
- policy_status
- sales_channel
- bundesland

**Main KPIs**

- total_policies
- active_policies
- cancelled_policies
- premium_revenue
- avg_premium
- total_coverage

**Output table**

`insurance_lakehouse.gold.gold_policy_performance`

---

### gold_customer_risk_profile

**Business purpose**

Create a customer-level risk profile that combines policy exposure, claim behavior, and fraud-risk indicators.

**Audience**

Risk analysts, customer analytics teams, fraud monitoring teams.

**Input tables**

- silver_customers
- silver_policies
- silver_claims
- silver_fraud_indicators

**Grain**

One row per customer.

**Main KPIs**

- policy_count
- claim_count
- total_claim_amount
- avg_claim_amount
- avg_risk_score
- high_risk_claims
- gdpr_consent

**Output table**

`insurance_lakehouse.gold.gold_customer_risk_profile`

---

### gold_claims_payment_summary

**Business purpose**

Analyze claim settlement and payment behavior without multiplying claim records.

**Audience**

Claims operations, finance reporting, payment operations.

**Input tables**

- silver_claims
- silver_payments

**Grain**

One row per claim.

**Main KPIs**

- total_paid_amount
- payment_count
- payment_rejection_count
- first_payment_date
- last_payment_date
- payment_delay_days
- claim_to_payment_ratio

**Important design decision**

Payments are aggregated by claim_id before joining to claims. This prevents one-to-many payment records from duplicating claim amounts.

**Output table**

`insurance_lakehouse.gold.gold_claims_payment_summary`

---

### gold_fraud_risk_summary

**Business purpose**

Support fraud monitoring by summarizing fraud-risk patterns by region, product, claim type, and risk band.

**Audience**

Fraud analysts, risk teams, BI users.

**Input tables**

- silver_claims
- silver_policies
- silver_customers
- silver_fraud_indicators

**Grain**

One row per:

- bundesland
- policy_type
- claim_type
- risk_band

**Main KPIs**

- total_claims
- high_risk_claims
- high_risk_rate
- avg_risk_score
- duplicate_claim_count
- late_report_count

**Output table**

`insurance_lakehouse.gold.gold_fraud_risk_summary`

---

### gold_agent_performance

**Business purpose**

Measure agent and regional performance across policies, premium revenue, claims exposure, and estimated commissions.

**Audience**

Sales leadership, regional managers, agent performance analysts.

**Input tables**

- silver_agents
- silver_policies
- silver_claims
- silver_payments

**Grain**

One row per agent.

**Main KPIs**

- total_policies_sold
- active_policies
- premium_revenue
- total_claims_linked
- total_claim_amount
- claims_ratio
- estimated_commission

**Output table**

`insurance_lakehouse.gold.gold_agent_performance`

---

### gold_claim_fraud_features

**Business purpose**

Create an AI-ready claim-level feature table for future fraud-risk modelling or analytical scoring.

**Audience**

Data scientists, fraud analytics teams, machine learning engineers.

**Input tables**

- silver_claims
- silver_policies
- silver_customers
- silver_payments
- silver_fraud_indicators

**Grain**

One row per claim.

**Main features**

- claim_amount
- premium_amount
- coverage_amount
- claim_amount_to_coverage_ratio
- policy_age_days
- customer_age
- total_paid_amount
- payment_count
- payment_rejection_count
- payment_delay_days
- previous_claims_count
- suspicious_amount_flag
- duplicate_claim_flag
- late_report_flag
- high_risk_region_flag
- risk_score
- risk_band

**PII decision**

The feature table does not expose raw customer PII such as email, phone number, street, full name, or date of birth.

**Output table**

`insurance_lakehouse.gold.gold_claim_fraud_features`