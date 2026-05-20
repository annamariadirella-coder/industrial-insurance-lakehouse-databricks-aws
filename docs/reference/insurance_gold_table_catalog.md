# Insurance Gold Table Catalog

| Table | Purpose | Grain |
|---|---|---|
| gold_claims_overview | Claims operations reporting | month + status + type + product + region |
| gold_policy_performance | Policy and premium reporting | product + status + channel + region |
| gold_customer_risk_profile | Customer-level risk profile | one row per customer |
| gold_claims_payment_summary | Claim settlement reporting | one row per claim |
| gold_fraud_risk_summary | Fraud-risk monitoring | region + product + claim type + risk band |
| gold_agent_performance | Broker/agent performance | one row per agent |
| gold_claim_fraud_features | Future fraud modeling features | one row per claim |
