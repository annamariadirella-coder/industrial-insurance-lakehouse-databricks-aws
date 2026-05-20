# Day 3 Gold Validation Summary

| Gold table | Row count | Grain columns | Duplicate grain count | Status |
|---|---:|---|---:|---|
| gold_claims_overview | 30158 | claim_month + claim_status + claim_type + policy_type + bundesland | n/a | PASS |
| gold_policy_performance | 540 | policy_type + policy_status + sales_channel + bundesland | n/a | PASS |
| gold_customer_risk_profile | 10000 | customer_id | 0 | PASS |
| gold_claims_payment_summary | 50000 | claim_id | 0 | PASS |
| gold_fraud_risk_summary | 810 | bundesland + policy_type + claim_type + risk_band | n/a | PASS |
| gold_agent_performance | 1000 | agent_id | 0 | PASS |
| gold_claim_fraud_features | 50000 | claim_id | 0 | PASS |

## Validation results

All required Day 3 Gold tables were created in `insurance_lakehouse.gold`.

The one-row-per-entity Gold tables passed duplicate grain validation:

- `gold_customer_risk_profile`: one row per customer
- `gold_claims_payment_summary`: one row per claim
- `gold_agent_performance`: one row per agent
- `gold_claim_fraud_features`: one row per claim

The aggregate Gold tables were validated through row count checks and business grain review.

## Key checks completed

- Gold tables exist
- Row counts are greater than zero
- Duplicate grain checks passed where applicable
- AI-ready feature table has one row per claim
- No unnecessary raw PII is exposed in the Gold feature table

## Status

Day 3 Gold validation status: PASS