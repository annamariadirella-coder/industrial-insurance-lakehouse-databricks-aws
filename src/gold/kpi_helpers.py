from pyspark.sql import functions as F

def add_risk_band(df, risk_col="risk_score"):
    return df.withColumn("risk_band", F.when(F.col(risk_col) < 30, "low").when(F.col(risk_col) < 70, "medium").otherwise("high"))

def safe_ratio(numerator_col, denominator_col):
    return F.when(F.col(denominator_col) == 0, None).otherwise(F.col(numerator_col) / F.col(denominator_col))
