# Databricks notebook source

# MAGIC %md
# MAGIC # 24 — Dashboard Views
# MAGIC Create final dashboard-ready SQL views. Use Gold tables as inputs and avoid raw PII.

# COMMAND ----------

catalog = "insurance_lakehouse"
gold_schema = "gold"
spark.sql(f"USE CATALOG {catalog}")

# COMMAND ----------

spark.sql(f'''
CREATE OR REPLACE VIEW {catalog}.{gold_schema}.vw_executive_insurance_overview AS
SELECT
    SUM(active_policies) AS total_active_policies,
    SUM(total_policies) AS total_policies,
    ROUND(SUM(premium_revenue), 2) AS total_premium_revenue
FROM {catalog}.{gold_schema}.gold_policy_performance
''')

# COMMAND ----------

spark.sql(f'''
CREATE OR REPLACE VIEW {catalog}.{gold_schema}.vw_claims_operations AS
SELECT
    claim_status,
    claim_type,
    policy_type,
    bundesland,
    SUM(total_claims) AS total_claims,
    ROUND(SUM(total_claim_amount), 2) AS total_claim_amount,
    ROUND(AVG(average_claim_amount), 2) AS average_claim_amount
FROM {catalog}.{gold_schema}.gold_claims_overview
GROUP BY claim_status, claim_type, policy_type, bundesland
''')

