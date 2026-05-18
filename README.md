# Week 11 Day 1 — Industrial Insurance Lakehouse on Databricks and AWS

## Project title
**Industrial Insurance Lakehouse on Databricks and AWS: Claims, Policies, BI and AI-Ready Data Engineering**

## Fictional company
**Rheinland Versicherung AG**

This is my Day 1 project repository for the Week 11 industrial Databricks trial project.

Day 1 builds the foundation:

```text
Databricks trial + AWS S3 + Git project structure + synthetic German insurance data + raw S3 landing + Bronze Delta ingestion + validation
```

This is not a small CSV exercise. You generate synthetic insurance data with PySpark, write it to AWS S3 as raw data, then ingest it into Bronze Delta tables.

## Day 1 implementation status

Status: completed in small mode

AWS S3 bucket:

s3://insurance-lakehouse-week11-day1-anna-dirella-2026

Day 1 completed work:

- Databricks trial workspace used
- AWS S3 bucket and folder structure created
- synthetic German insurance data generated with PySpark
- raw CSV data written to S3
- Bronze Delta tables created for customers, policies, claims, payments, agents, and fraud indicators
- ingestion metadata added to Bronze tables
- raw-to-Bronze row counts validated successfully

## Day 1 validation results

| Dataset | Raw count | Bronze count | Status |
|---|---:|---:|---|
| customers | 10000 | 10000 | PASS |
| policies | 25000 | 25000 | PASS |
| claims | 50000 | 50000 | PASS |
| payments | 50000 | 50000 | PASS |
| agents | 100 | 100 | PASS |
| fraud_indicators | 50000 | 50000 | PASS |

## Data modes

| Mode | Customers | Policies | Claims | Payments | Purpose |
|---|---:|---:|---:|---:|---|
| small | 10,000 | 25,000 | 50,000 | 50,000 | required first test |
| medium | 500,000 | 1,500,000 | 5,000,000 | 5,000,000 | realistic student target |
| large | 2,000,000+ | 5,000,000+ | 20,000,000+ | 20,000,000+ | optional industrial scale |

Always start with:

```python
DATA_MODE = "small"
```

## Cost-control rules

- Use one dedicated S3 bucket.
- Use small mode first.
- Use small or medium compute only.
- Stop clusters when not in use.
- Do not leave clusters running overnight.
- Set AWS budget alerts.
- Never commit AWS credentials.
- Do not run large mode unless instructed.
- Delete or stop resources after the project.

## Day 1 notebook order

```text
notebooks/
  00_setup/
    00_project_setup.py
  01_data_generation/
    01_generate_synthetic_insurance_data.py
    02_write_raw_data_to_s3.py
  02_bronze/
    03_bronze_ingestion_customers.py
    04_bronze_ingestion_policies.py
    05_bronze_ingestion_claims.py
    06_bronze_ingestion_payments.py
    07_bronze_ingestion_agents.py
    08_bronze_ingestion_fraud_indicators.py
  03_validation/
    09_day1_bronze_validation.py
```

## Day 1 success statement

> I created the Databricks/AWS foundation for an industrial insurance lakehouse, generated synthetic German insurance data with PySpark, landed it in S3, ingested it into Bronze Delta tables, added ingestion metadata, and validated raw-to-Bronze row counts.
