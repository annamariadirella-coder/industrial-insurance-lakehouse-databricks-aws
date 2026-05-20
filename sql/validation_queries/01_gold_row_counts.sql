SELECT 'gold_claims_overview' AS table_name, COUNT(*) AS row_count FROM insurance_lakehouse.gold.gold_claims_overview
UNION ALL SELECT 'gold_policy_performance', COUNT(*) FROM insurance_lakehouse.gold.gold_policy_performance
UNION ALL SELECT 'gold_customer_risk_profile', COUNT(*) FROM insurance_lakehouse.gold.gold_customer_risk_profile
UNION ALL SELECT 'gold_claims_payment_summary', COUNT(*) FROM insurance_lakehouse.gold.gold_claims_payment_summary
UNION ALL SELECT 'gold_fraud_risk_summary', COUNT(*) FROM insurance_lakehouse.gold.gold_fraud_risk_summary
UNION ALL SELECT 'gold_agent_performance', COUNT(*) FROM insurance_lakehouse.gold.gold_agent_performance
UNION ALL SELECT 'gold_claim_fraud_features', COUNT(*) FROM insurance_lakehouse.gold.gold_claim_fraud_features;
