# Gold Layer Design Principles

## 1. Every Gold table needs a purpose

Bad: `gold_claims_table`

Better: `gold_claims_overview`  
Purpose: claims operations reporting by month, status, claim type, product, and region.

## 2. Every Gold table needs a grain

| Gold table | Grain |
|---|---|
| gold_claims_overview | month + claim_status + claim_type + policy_type + bundesland |
| gold_policy_performance | policy_type + policy_status + sales_channel + bundesland |
| gold_customer_risk_profile | one row per customer |
| gold_claims_payment_summary | one row per claim |
| gold_agent_performance | one row per agent |
| gold_claim_fraud_features | one row per claim |

## 3. Avoid one-to-many duplication

If one claim can have multiple payments, aggregate payments by `claim_id` before joining to claims.

## 4. Do not expose unnecessary PII

Gold outputs should be business-ready and privacy-aware.
