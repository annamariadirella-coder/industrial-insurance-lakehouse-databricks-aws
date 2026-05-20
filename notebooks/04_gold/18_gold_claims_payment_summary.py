# Databricks notebook source
# MAGIC %md
# MAGIC # 18 — Gold Claims Payment Summary
# MAGIC
# MAGIC Week 11 Day 3 — Gold Analytics, Insurance KPIs, AI-Ready Features, and Performance.
# MAGIC
# MAGIC Replace catalog/schema names if your environment uses different names.

# COMMAND ----------

from pyspark.sql import functions as F
from pyspark.sql import Window

CATALOG = "insurance_lakehouse"
SILVER_SCHEMA = "silver"
GOLD_SCHEMA = "gold"

spark.sql(f"CREATE SCHEMA IF NOT EXISTS {CATALOG}.{GOLD_SCHEMA}")

def t(schema, table):
    return f"{CATALOG}.{schema}.{table}"

# COMMAND ----------


silver_claims = spark.table(t(SILVER_SCHEMA, "silver_claims"))
silver_payments = spark.table(t(SILVER_SCHEMA, "silver_payments"))
silver_policies = spark.table(t(SILVER_SCHEMA, "silver_policies"))
payments_by_claim = silver_payments.groupBy("claim_id").agg(
    F.count("*").alias("payment_count"),
    F.round(F.sum("payment_amount"), 2).alias("total_paid_amount"),
    F.sum(F.when(F.col("payment_status") == "rejected", 1).otherwise(0)).alias("rejected_payment_count"),
    F.min("payment_date").alias("first_payment_date")
)
gold_claims_payment_summary = (
    silver_claims.join(silver_policies.select("policy_id", "policy_type", "premium_amount", "coverage_amount"), "policy_id", "left")
    .join(payments_by_claim, "claim_id", "left")
    .withColumn("payment_delay_days", F.datediff(F.col("first_payment_date"), F.col("claim_date")))
    .withColumn("claim_to_payment_ratio", F.when(F.col("claim_amount") == 0, None).otherwise(F.col("total_paid_amount") / F.col("claim_amount")))
)
gold_claims_payment_summary.write.mode("overwrite").format("delta").saveAsTable(t(GOLD_SCHEMA, "gold_claims_payment_summary"))
display(gold_claims_payment_summary.limit(20))

