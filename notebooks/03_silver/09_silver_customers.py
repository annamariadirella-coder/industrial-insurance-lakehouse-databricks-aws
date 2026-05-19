# Databricks notebook source
# Silver Customers and GDPR-safe PII handling

from pyspark.sql import functions as F

CATALOG = "insurance_lakehouse"
BRONZE_SCHEMA = "bronze"
SILVER_SCHEMA = "silver"
QUARANTINE_SCHEMA = "quarantine"

bronze_table = f"{CATALOG}.{BRONZE_SCHEMA}.bronze_customers"
silver_table = f"{CATALOG}.{SILVER_SCHEMA}.silver_customers"
quarantine_table = f"{CATALOG}.{QUARANTINE_SCHEMA}.quarantine_invalid_customers"

spark.sql(f"CREATE SCHEMA IF NOT EXISTS {CATALOG}.{SILVER_SCHEMA}")
spark.sql(f"CREATE SCHEMA IF NOT EXISTS {CATALOG}.{QUARANTINE_SCHEMA}")

customers_bronze = spark.table(bronze_table)

customers_prepared = (
    customers_bronze
    .withColumn("customer_id", F.trim(F.col("customer_id")))
    .withColumn("first_name", F.trim(F.col("first_name")))
    .withColumn("last_name", F.trim(F.col("last_name")))
    .withColumn("gender", F.lower(F.trim(F.col("gender"))))
    .withColumn("email", F.lower(F.trim(F.col("email").cast("string"))))
    .withColumn("phone_number", F.trim(F.col("phone_number").cast("string")))
    .withColumn("street", F.trim(F.col("street")))
    .withColumn("city", F.initcap(F.trim(F.col("city"))))
    .withColumn("postal_code", F.col("postal_code").cast("string"))
    .withColumn("bundesland", F.trim(F.col("bundesland")))
    .withColumn("country", F.trim(F.col("country")))
    .withColumn("date_of_birth", F.to_date(F.col("date_of_birth")))
    .withColumn("registration_date", F.to_date(F.col("registration_date")))
    .withColumn("gdpr_consent", F.col("gdpr_consent").cast("boolean"))
    .withColumn("customer_segment", F.lower(F.trim(F.col("customer_segment"))))
    .withColumn("customer_hash", F.sha2(F.col("customer_id").cast("string"), 256))
    .withColumn("email_hash", F.sha2(F.lower(F.trim(F.col("email").cast("string"))), 256))
    .withColumn("phone_hash", F.sha2(F.trim(F.col("phone_number").cast("string")), 256))
    .withColumn(
        "customer_age",
        F.floor(F.months_between(F.current_date(), F.col("date_of_birth")) / 12)
    )
)

duplicate_customer_ids = (
    customers_prepared
    .groupBy("customer_id")
    .count()
    .filter(F.col("customer_id").isNotNull() & (F.col("count") > 1))
    .select("customer_id")
    .withColumn("is_duplicate_customer_id", F.lit(True))
)

customers_checked = (
    customers_prepared
    .join(duplicate_customer_ids, on="customer_id", how="left")
    .withColumn(
        "is_duplicate_customer_id",
        F.coalesce(F.col("is_duplicate_customer_id"), F.lit(False))
    )
)

invalid_condition = (
    F.col("customer_id").isNull()
    | F.col("gdpr_consent").isNull()
    | F.col("is_duplicate_customer_id")
)

error_reason = (
    F.when(F.col("customer_id").isNull(), F.lit("missing_customer_id"))
    .when(F.col("gdpr_consent").isNull(), F.lit("invalid_gdpr_consent"))
    .when(F.col("is_duplicate_customer_id"), F.lit("duplicate_customer_id"))
    .otherwise(F.lit("unknown_customer_quality_issue"))
)

invalid_customers = (
    customers_checked
    .filter(invalid_condition)
    .withColumn("record_id", F.col("customer_id").cast("string"))
    .withColumn("source_table", F.lit("bronze_customers"))
    .withColumn("error_reason", error_reason)
    .withColumn("error_severity", F.lit("HIGH"))
    .withColumn("quarantine_timestamp", F.current_timestamp())
    .withColumn(
        "original_record_json",
        F.to_json(F.struct(*[F.col(c) for c in customers_prepared.columns]))
    )
    .select(
        "record_id",
        "source_table",
        "error_reason",
        "error_severity",
        "quarantine_timestamp",
        "source_file_name",
        "ingest_run_id",
        "original_record_json"
    )
)

valid_customers_raw = (
    customers_checked
    .filter(~invalid_condition)
    .drop("is_duplicate_customer_id")
    .dropDuplicates(["customer_id"])
)

safe_customer_columns = [
    "customer_id",
    "gender",
    "city",
    "bundesland",
    "country",
    "registration_date",
    "gdpr_consent",
    "customer_segment",
    "customer_hash",
    "email_hash",
    "phone_hash",
    "customer_age",
    "ingest_timestamp",
    "ingest_run_id",
    "source_file_name"
]

existing_safe_customer_columns = [
    c for c in safe_customer_columns if c in valid_customers_raw.columns
]

valid_customers = valid_customers_raw.select(*existing_safe_customer_columns)

valid_customers.write.format("delta").mode("overwrite").option("overwriteSchema", "true").saveAsTable(silver_table)

invalid_customers.write.format("delta").mode("overwrite").option("overwriteSchema", "true").saveAsTable(quarantine_table)

print("Bronze customers:", customers_bronze.count())
print("Silver customers:", spark.table(silver_table).count())
print("Quarantine customers:", spark.table(quarantine_table).count())

print("Silver customer columns:")
print(spark.table(silver_table).columns)

# COMMAND ----------

display(spark.table("insurance_lakehouse.silver.silver_customers").limit(10))

# COMMAND ----------

display(spark.table("insurance_lakehouse.quarantine.quarantine_invalid_customers").limit(10))

# COMMAND ----------

cols = spark.table("insurance_lakehouse.silver.silver_customers").columns

raw_pii_fields = [
    "first_name",
    "last_name",
    "email",
    "phone_number",
    "street",
    "postal_code",
    "date_of_birth"
]

print("PII fields still present:", [c for c in raw_pii_fields if c in cols])
