SELECT
  SUM(CASE WHEN claim_id IS NULL THEN 1 ELSE 0 END) AS null_claim_id,
  SUM(CASE WHEN policy_id IS NULL THEN 1 ELSE 0 END) AS null_policy_id,
  SUM(CASE WHEN customer_id IS NULL THEN 1 ELSE 0 END) AS null_customer_id,
  SUM(CASE WHEN risk_score IS NULL THEN 1 ELSE 0 END) AS null_risk_score
FROM insurance_lakehouse.gold.gold_claim_fraud_features;
