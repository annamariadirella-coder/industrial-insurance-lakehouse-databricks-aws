from pyspark.sql import functions as F

def aggregate_payments_by_claim(payments):
    return payments.groupBy("claim_id").agg(
        F.count("*").alias("payment_count"),
        F.sum("payment_amount").alias("total_paid_amount"),
        F.sum(F.when(F.col("payment_status") == "rejected", 1).otherwise(0)).alias("payment_rejection_count"),
        F.min("payment_date").alias("first_payment_date"),
        F.max("payment_date").alias("last_payment_date")
    )
