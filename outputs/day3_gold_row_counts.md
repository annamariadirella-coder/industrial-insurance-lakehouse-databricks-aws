# Day 3 Gold Row Counts

| Gold table | Row count | Grain |
|---|---:|---|
| gold_claims_overview | 30158 | claim_month + claim_status + claim_type + policy_type + bundesland |
| gold_policy_performance | 540 | policy_type + policy_status + sales_channel + bundesland |
| gold_customer_risk_profile | 10000 | one row per customer |
| gold_claims_payment_summary | 50000 | one row per claim |
| gold_fraud_risk_summary | 810 | bundesland + policy_type + claim_type + risk_band |
| gold_agent_performance | 1000 | one row per agent |
| gold_claim_fraud_features | 50000 | one row per claim |

## Notes

All required Day 3 Gold tables were created in:

`insurance_lakehouse.gold`

The row counts were validated with the Day 3 Gold validation notebook.