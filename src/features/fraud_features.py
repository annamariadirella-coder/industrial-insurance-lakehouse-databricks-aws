from pyspark.sql import functions as F

def add_claim_feature_columns(df):
    return (
        df.withColumn("claim_amount_to_coverage_ratio", F.when(F.col("coverage_amount") == 0, None).otherwise(F.col("claim_amount") / F.col("coverage_amount")))
          .withColumn("policy_age_days", F.datediff(F.col("claim_date"), F.col("start_date")))
          .withColumn("customer_age", F.floor(F.datediff(F.col("claim_date"), F.col("date_of_birth")) / F.lit(365.25)))
          .withColumn("payment_delay_days", F.datediff(F.col("first_payment_date"), F.col("claim_date")))
    )
