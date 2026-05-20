# Day 3 KPI Definitions

## Purpose

This document defines the main KPIs used in the Day 3 Gold layer for Rheinland Versicherung AG.

The goal is to make the business logic explainable and reusable for dashboards, analytics, and future AI-ready features.

---

## gold_claims_overview

**Grain**

claim_month + claim_status + claim_type + policy_type + bundesland

| KPI | Formula | Meaning |
|---|---|---|
| total_claims | count(*) | Number of claims in the group |
| total_claim_amount | sum(claim_amount) | Total claim amount |
| avg_claim_amount | avg(claim_amount) | Average claim size |
| fraud_flag_rate | avg(fraud_flag as integer) | Share of claims flagged as fraud |
| avg_risk_score | avg(risk_score) | Average fraud risk score |

---

## gold_policy_performance

**Grain**

policy_type + policy_status + sales_channel + bundesland

| KPI | Formula | Meaning |
|---|---|---|
| total_policies | count(policy_id) | Number of policies |
| active_policies | count where policy_status = active | Number of active policies |
| cancelled_policies | count where policy_status = cancelled | Number of cancelled policies |
| premium_revenue | sum(premium_amount) | Total premium revenue |
| avg_premium | avg(premium_amount) | Average premium amount |
| total_coverage | sum(coverage_amount) | Total insured coverage amount |

---

## gold_customer_risk_profile

**Grain**

One row per customer.

| KPI | Formula | Meaning |
|---|---|---|
| policy_count | count distinct policy_id | Number of policies per customer |
| claim_count | count distinct claim_id | Number of claims per customer |
| total_claim_amount | sum(claim_amount) | Total claim amount per customer |
| avg_claim_amount | avg(claim_amount) | Average claim amount per customer |
| avg_risk_score | avg(risk_score) | Average risk score per customer |
| high_risk_claims | count where risk_score >= 70 | Number of high-risk claims |
| gdpr_consent | carried from silver_customers | Consent indicator for analytics use |

---

## gold_claims_payment_summary

**Grain**

One row per claim.

| KPI | Formula | Meaning |
|---|---|---|
| total_paid_amount | sum(payment_amount) by claim_id | Total paid amount for the claim |
| payment_count | count payments by claim_id | Number of payment records |
| payment_rejection_count | count where payment_status = rejected | Number of rejected payments |
| first_payment_date | min(payment_date) | First valid payment date |
| last_payment_date | max(payment_date) | Last valid payment date |
| payment_delay_days | datediff(first_payment_date, claim_date) | Days from claim to first payment |
| claim_to_payment_ratio | total_paid_amount / claim_amount | Share of claim amount paid |

**Important assumption**

Payments are aggregated by claim_id before joining to claims to avoid multiplying claim rows.

---

## gold_fraud_risk_summary

**Grain**

bundesland + policy_type + claim_type + risk_band

| KPI | Formula | Meaning |
|---|---|---|
| total_claims | count(*) | Number of claims in the group |
| high_risk_claims | count where risk_score >= 70 | Number of high-risk claims |
| high_risk_rate | high_risk_claims / total_claims | Share of high-risk claims |
| avg_risk_score | avg(risk_score) | Average fraud risk score |
| duplicate_claim_count | sum(duplicate_claim_flag) | Number of duplicate claim signals |
| late_report_count | sum(late_report_flag) | Number of late report signals |

---

## gold_agent_performance

**Grain**

One row per agent.

| KPI | Formula | Meaning |
|---|---|---|
| total_policies_sold | count distinct policy_id | Number of policies linked to the agent |
| active_policies | count where policy_status = active | Number of active policies |
| premium_revenue | sum(premium_amount) | Premium revenue generated |
| total_claims_linked | count distinct claim_id | Claims linked to agent policies |
| total_claim_amount | sum(claim_amount) | Claim exposure linked to agent policies |
| claims_ratio | total_claim_amount / premium_revenue | Claim exposure compared to premium revenue |
| estimated_commission | premium_revenue * commission_rate | Estimated commission amount |

---

## gold_claim_fraud_features

**Grain**

One row per claim.

This table is AI-ready, so it contains features rather than business KPIs.

| Feature | Formula | Meaning |
|---|---|---|
| claim_amount_to_coverage_ratio | claim_amount / coverage_amount | Claim size compared to coverage |
| policy_age_days | datediff(claim_date, start_date) | Age of policy at claim date |
| customer_age | from silver_customers | GDPR-safe customer age |
| total_paid_amount | sum(payment_amount) by claim_id | Total paid amount |
| payment_count | count payments by claim_id | Number of payments |
| payment_rejection_count | count rejected payments | Payment rejection signal |
| payment_delay_days | datediff(first_payment_date, claim_date) | Delay between claim and first payment |
| previous_claims_count | from fraud indicators | Historical claim indicator |
| suspicious_amount_flag | from fraud indicators | Suspicious amount signal |
| duplicate_claim_flag | from fraud indicators | Duplicate claim signal |
| late_report_flag | from fraud indicators | Late report signal |
| high_risk_region_flag | from fraud indicators | Regional risk signal |
| risk_score | from fraud indicators | Fraud risk score from 0 to 100 |
| risk_band | low / medium / high | Human-readable risk category |

## KPI sanity assumptions

- Claim amounts should be non-negative.
- Premium revenue should be non-negative.
- Coverage amount should be greater than premium amount.
- Risk score should be between 0 and 100.
- One-row-per-claim tables must not contain duplicate claim_id values.