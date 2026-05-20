# Databricks notebook source
# MAGIC %md
# MAGIC # 21 — Gold Claim Fraud Features
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
silver_policies = spark.table(t(SILVER_SCHEMA, "silver_policies"))
silver_customers = spark.table(t(SILVER_SCHEMA, "silver_customers"))
silver_payments = spark.table(t(SILVER_SCHEMA, "silver_payments"))
silver_fraud = spark.table(t(SILVER_SCHEMA, "silver_fraud_indicators"))
payments_by_claim = silver_payments.groupBy("claim_id").agg(F.min("payment_date").alias("first_payment_date"), F.round(F.sum("payment_amount"), 2).alias("total_paid_amount"))
gold_claim_fraud_features = (
    silver_claims
    .join(silver_policies.select("policy_id", "policy_type", "start_date", "premium_amount", "coverage_amount"), "policy_id", "left")
    .join(silver_customers.select("customer_id", "date_of_birth", "bundesland"), "customer_id", "left")
    .join(payments_by_claim, "claim_id", "left")
    .join(silver_fraud, "claim_id", "left")
    .withColumn("claim_amount_to_coverage_ratio", F.when(F.col("coverage_amount") == 0, None).otherwise(F.col("claim_amount") / F.col("coverage_amount")))
    .withColumn("policy_age_days", F.datediff(F.col("claim_date"), F.col("start_date")))
    .withColumn("customer_age", F.floor(F.datediff(F.col("claim_date"), F.col("date_of_birth")) / F.lit(365.25)))
    .withColumn("payment_delay_days", F.datediff(F.col("first_payment_date"), F.col("claim_date")))
)
gold_claim_fraud_features.write.mode("overwrite").format("delta").saveAsTable(t(GOLD_SCHEMA, "gold_claim_fraud_features"))
display(gold_claim_fraud_features.limit(20))

