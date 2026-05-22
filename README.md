# Week 11 Day 1 - Industrial Insurance Lakehouse on Databricks and AWS

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

## Day 2 - Silver Layer, Data Quality, Quarantine and GDPR

Status: completed

Day 2 transformed the Bronze insurance data into trusted Silver tables with data quality validation, quarantine handling and GDPR-aware PII protection.

### Silver tables created

- silver_customers
- silver_policies
- silver_claims
- silver_payments
- silver_agents
- silver_fraud_indicators

### Quarantine tables created

- quarantine_invalid_customers
- quarantine_invalid_policies
- quarantine_invalid_claims
- quarantine_invalid_payments
- quarantine_invalid_fraud_indicators

### Day 2 validation results

| Dataset | Bronze rows | Silver rows | Quarantine rows | Status |
|---|---:|---:|---:|---|
| customers | 10000 | 10000 | 0 | PASS |
| policies | 25000 | 25000 | 0 | PASS |
| claims | 50000 | 50000 | 0 | PASS |
| payments | 50000 | 27689 | 22311 | PASS |
| agents | 1000 | 1000 | 0 | PASS |
| fraud_indicators | 50000 | 18575 | 31425 | PASS |

### Main quality findings

- Payments with `payment_date` before `claim_date` were moved to quarantine.
- Fraud indicator records with duplicate `claim_id` were moved to quarantine.
- All Bronze records are accounted for through Silver plus quarantine.
- Raw PII fields were removed from `silver_customers`.
- Hashed fields such as `customer_hash`, `email_hash` and `phone_hash` were kept for pseudonymized analytics.

### Day 2 documentation

- `docs/day2_data_quality_report.md`
- `docs/day2_gdpr_pii_handling.md`
- `outputs/day2_quality_summary.md`

Day 2 success statement:

> I created a trusted Silver layer from Bronze insurance data, applied data quality rules, quarantined invalid records with error reasons, protected GDPR-sensitive customer fields, and documented the results for Day 3 Gold analytics.

## Day 3 - Gold Analytics, Insurance KPIs, AI-Ready Features and Performance

Status: completed

Day 3 transformed trusted Silver data into business-ready Gold tables for insurance analytics, fraud-risk monitoring, agent performance, and AI-ready feature engineering.

### Gold tables created

- gold_claims_overview
- gold_policy_performance
- gold_customer_risk_profile
- gold_claims_payment_summary
- gold_fraud_risk_summary
- gold_agent_performance
- gold_claim_fraud_features

### Gold validation results

| Gold table | Row count | Grain | Status |
|---|---:|---|---|
| gold_claims_overview | 30158 | claim_month + claim_status + claim_type + policy_type + bundesland | PASS |
| gold_policy_performance | 540 | policy_type + policy_status + sales_channel + bundesland | PASS |
| gold_customer_risk_profile | 10000 | one row per customer | PASS |
| gold_claims_payment_summary | 50000 | one row per claim | PASS |
| gold_fraud_risk_summary | 810 | bundesland + policy_type + claim_type + risk_band | PASS |
| gold_agent_performance | 1000 | one row per agent | PASS |
| gold_claim_fraud_features | 50000 | one row per claim | PASS |

### Main Day 3 work

- Built business-facing Gold KPI tables from trusted Silver data
- Defined the grain of each Gold output
- Aggregated payments before joining to claims to avoid duplicate claim rows
- Created an AI-ready fraud feature table with one row per claim
- Validated Gold row counts and duplicate grain checks
- Inspected the execution plan for the feature table
- Ran Delta optimization successfully on the AI-ready feature table

### Day 3 documentation

- `docs/day3_gold_business_logic.md`
- `docs/day3_kpi_definitions.md`
- `docs/day3_feature_table_design.md`
- `docs/day3_performance_notes.md`
- `outputs/day3_gold_row_counts.md`
- `outputs/day3_gold_validation_summary.md`
- `outputs/day3_feature_table_profile.md`

Day 3 success statement:

> I created a business-ready Gold layer from trusted Silver insurance data, calculated insurance KPIs, built fraud-risk summaries, created an AI-ready claim-level feature table, validated table grains and row counts, and documented performance considerations.

## Day 5 - Final Delivery, Dashboard Views, Governance and Presentation

Status: completed

Day 5 packaged the insurance lakehouse as a professional, portfolio-ready data engineering project.

The focus was not only on code, but also on making the project:

- dashboard-ready
- validated
- governed
- documented
- presentation-ready
- suitable for portfolio and interview discussion

### Dashboard-ready SQL views created

The following dashboard views were created in `insurance_lakehouse.gold`:

| View | Purpose | Row count | Status |
|---|---|---:|---|
| `vw_executive_insurance_overview` | Executive KPI overview | 1 | PASS |
| `vw_claims_operations` | Claims operations monitoring | 1350 | PASS |
| `vw_policy_portfolio` | Policy portfolio analytics | 540 | PASS |
| `vw_fraud_risk_monitoring` | Fraud-risk monitoring | 810 | PASS |
| `vw_agent_regional_performance` | Agent and regional performance | 1000 | PASS |
| `vw_data_quality_monitoring` | Quarantine and data quality monitoring | 5 | PASS |

### Final validation results

| Validation area | Result |
|---|---|
| Gold tables exist and return rows | PASS |
| Dashboard views exist and return rows | PASS |
| AI-ready feature table has one row per claim | PASS |
| Duplicate claim_id groups in feature table | 0 |
| Dashboard views expose checked raw PII fields | No |
| Quarantine evidence documented | PASS |
| Final documentation completed | PASS |

### Governance and GDPR

The dashboard views were checked for raw PII exposure.

Checked fields:

- first_name
- last_name
- email
- phone_number
- street
- postal_code
- date_of_birth
- iban
- iban_hash

Result:

No checked PII fields were exposed in the dashboard views.

Status: PASS

### Final documentation

Day 5 added or finalized the following documentation:

- `docs/03_dashboard_design_strategy.md`
- `docs/04_governance_gdpr_strategy.md`
- `docs/05_final_validation_strategy.md`
- `docs/06_data_dictionary.md`
- `docs/07_presentation_strategy.md`
- `outputs/dashboard_view_counts.md`
- `outputs/pii_exposure_check.md`
- `outputs/final_validation_summary.md`
- `outputs/final_project_inventory.md`
- `presentation/final_project_presentation_outline.md`
- `presentation/speaking_points.md`
- `presentation/demo_script.md`

### Final screenshots

Final delivery screenshots are stored in:

- `screenshots/day5/`

They include dashboard view samples, dashboard view counts, PII exposure checks, Gold table counts, and feature table validation evidence.

### Day 5 success statement

I created dashboard-ready SQL views, validated final Gold and dashboard outputs, confirmed that dashboard views do not expose checked raw PII fields, documented governance and final validation evidence, and prepared the project for presentation and portfolio use.
