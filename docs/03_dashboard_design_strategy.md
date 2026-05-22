# Dashboard Design Strategy

## Purpose

The dashboard layer makes the insurance lakehouse business-facing.

The dashboard views are built on top of the Gold layer and are designed for executives, claims teams, portfolio analysts, fraud analysts, agent performance users, and data quality reviewers.

All dashboard views are PII-safe and do not expose raw personal data.

---

## Dashboard page 1 - Executive Insurance Overview

**Audience**

Executives and senior management.

**Source view**

`insurance_lakehouse.gold.vw_executive_insurance_overview`

**Business question**

Is the insurance portfolio healthy, profitable, and operationally stable?

**KPIs**

- total_customers
- total_policies
- total_active_policies
- total_premium_revenue
- total_claims
- paid_claims
- total_claim_amount
- claims_ratio
- fraud_risk_rate
- payment_rejection_rate

**Suggested visuals**

- KPI cards for customers, active policies, premium revenue, claims ratio
- KPI card for fraud risk rate
- KPI card for payment rejection rate

---

## Dashboard page 2 - Claims Operations

**Audience**

Claims operations team and insurance analysts.

**Source view**

`insurance_lakehouse.gold.vw_claims_operations`

**Business question**

Which claim types, statuses, products, and regions drive claims volume and claim amount?

**KPIs**

- total_claims
- total_claim_amount
- average_claim_amount
- average_risk_score

**Suggested visuals**

- Claims by status
- Claims by claim type
- Claim amount by Bundesland
- Average risk score by claim type

**Useful filters**

- claim_status
- claim_type
- policy_type
- bundesland

---

## Dashboard page 3 - Policy Portfolio

**Audience**

Portfolio managers, product teams, and business analysts.

**Source view**

`insurance_lakehouse.gold.vw_policy_portfolio`

**Business question**

Which products, statuses, channels, and regions generate premium revenue?

**KPIs**

- total_policies
- active_policies
- cancelled_policies
- premium_revenue
- average_premium
- total_coverage

**Suggested visuals**

- Premium revenue by policy type
- Active policies by product
- Policy status distribution
- Premium revenue by sales channel

**Useful filters**

- policy_type
- policy_status
- sales_channel
- bundesland

---

## Dashboard page 4 - Fraud Risk Monitoring

**Audience**

Fraud analysts and risk teams.

**Source view**

`insurance_lakehouse.gold.vw_fraud_risk_monitoring`

**Business question**

Where are the highest fraud-risk patterns across products, claim types, and regions?

**KPIs**

- total_claims
- high_risk_claims
- high_risk_rate
- average_risk_score
- suspicious_amount_count
- duplicate_claim_count
- late_report_count

**Suggested visuals**

- High-risk claims by Bundesland
- Average risk score by risk band
- Duplicate claim count by claim type
- Late report count by product type

**Useful filters**

- bundesland
- policy_type
- claim_type
- risk_band

---

## Dashboard page 5 - Agent and Regional Performance

**Audience**

Sales leadership, regional managers, and agent performance analysts.

**Source view**

`insurance_lakehouse.gold.vw_agent_regional_performance`

**Business question**

Which agents and regions generate strong premium revenue, and where are claims ratios too high?

**KPIs**

- total_policies_sold
- premium_revenue
- total_claims_linked
- total_claim_amount
- total_paid_amount
- claims_ratio
- estimated_commission

**Suggested visuals**

- Premium revenue by agent
- Claims ratio by region
- Estimated commission by agent
- Total claims linked by agent

**Useful filters**

- region
- bundesland
- active_flag

---

## Dashboard page 6 - Data Quality Monitoring

**Audience**

Data engineering team, compliance reviewers, and project reviewers.

**Source view**

`insurance_lakehouse.gold.vw_data_quality_monitoring`

**Business question**

Can the business trust the pipeline outputs?

**KPIs**

- quarantine_count by dataset

**Suggested visuals**

- Quarantine count by dataset
- Data quality status table

**Useful filters**

- dataset

---

## Dashboard view counts

| View | Row count | Status |
|---|---:|---|
| vw_executive_insurance_overview | 1 | PASS |
| vw_claims_operations | 1350 | PASS |
| vw_policy_portfolio | 540 | PASS |
| vw_fraud_risk_monitoring | 810 | PASS |
| vw_agent_regional_performance | 1000 | PASS |
| vw_data_quality_monitoring | 5 | PASS |

## PII note

The dashboard views were checked for raw PII exposure.

No checked PII fields were exposed.

Status: PASS