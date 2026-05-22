# Final Presentation Speaking Points

## Opening

I built an industrial-style insurance lakehouse for Rheinland Versicherung AG, a fictional German insurance company.

The project uses Databricks on AWS, AWS S3, Delta Lake, PySpark, Spark SQL, Unity Catalog, GitHub, and medallion architecture.

The goal was to turn raw insurance data into trusted, governed, dashboard-ready, and AI-ready data products.

---

## Business problem

Insurance companies need reliable analytics for:

- claims operations
- policy portfolio performance
- payment monitoring
- fraud-risk analysis
- agent performance
- data quality monitoring

Raw data alone is not enough because it may contain duplicates, invalid references, wrong dates, sensitive PII, and records that should not be trusted without validation.

---

## Architecture

The project follows a medallion architecture:

Synthetic German insurance data  
→ AWS S3 raw landing  
→ Bronze Delta tables  
→ Silver trusted tables and quarantine  
→ Gold KPI tables and AI-ready feature table  
→ Dashboard-ready SQL views

The idea is:

- Bronze proves what arrived.
- Silver proves what can be trusted.
- Gold proves what the business can use.
- Day 5 proves the project can be delivered and explained.

---

## Day 1 - Raw and Bronze

Day 1 created the foundation.

I generated synthetic German insurance data in Databricks and wrote it to AWS S3 as raw CSV data.

Then I ingested the data into Bronze Delta tables and added ingestion metadata such as:

- ingest_timestamp
- ingest_run_id
- source_file_name

The raw-to-Bronze validation passed for all datasets.

---

## Day 2 - Silver, quality, quarantine, and GDPR

Day 2 created trusted Silver data.

I cleaned and validated:

- customers
- policies
- claims
- payments
- agents
- fraud indicators

Invalid records were not silently deleted. They were moved into quarantine tables with error reasons.

The most important quarantine results were:

- payments: payment_before_claim_date
- fraud_indicators: duplicate_claim_id

For GDPR, raw customer PII was removed from Silver. Email and phone were hashed, and date_of_birth was transformed into customer_age.

---

## Day 3 - Gold analytics and AI-ready features

Day 3 created business-ready Gold outputs.

Gold tables created:

- gold_claims_overview
- gold_policy_performance
- gold_customer_risk_profile
- gold_claims_payment_summary
- gold_fraud_risk_summary
- gold_agent_performance
- gold_claim_fraud_features

Each Gold table has a clear purpose and grain.

The most important design decision was to aggregate payments before joining them to claims, so claim-level KPIs were not duplicated.

The AI-ready feature table has one row per claim and passed the duplicate grain check.

---

## Day 5 - Final delivery

Day 5 packaged the lakehouse as a presentable data product.

I created dashboard-ready SQL views for:

- executive overview
- claims operations
- policy portfolio
- fraud-risk monitoring
- agent and regional performance
- data quality monitoring

All dashboard views return rows and passed the PII exposure check.

---

## Dashboard views

The dashboard views make the Gold layer easier to consume.

Examples:

- `vw_executive_insurance_overview` gives leadership a one-row KPI summary.
- `vw_claims_operations` supports claims teams.
- `vw_fraud_risk_monitoring` supports fraud analysts.
- `vw_data_quality_monitoring` shows quarantine evidence.

These views are business-facing and do not expose checked raw PII fields.

---

## Governance and GDPR

The project applies GDPR-aware design.

Raw PII is restricted to raw and Bronze.

Silver removes or hashes sensitive customer fields.

Gold and dashboard views avoid raw personal fields such as:

- first_name
- last_name
- email
- phone_number
- street
- date_of_birth

A role-based access model was documented for data engineers, analysts, fraud analysts, compliance, and executives.

---

## Validation evidence

Final validation confirmed:

- Gold tables exist and return rows.
- Dashboard views exist and return rows.
- The claim fraud feature table has one row per claim.
- Duplicate claim_id groups = 0.
- Dashboard views expose no checked raw PII fields.
- Quarantine counts are documented.

Final validation status: PASS.

---

## Performance

Performance thinking was included in Day 3.

Important decisions:

- select only required columns before joins
- aggregate one-to-many payment data before joining to claims
- validate table grain after joins
- inspect an explain plan
- run Delta optimization where available

The feature table explain plan was inspected and OPTIMIZE completed successfully.

---

## Main lessons learned

The most important lessons were:

- Table grain must be defined before creating KPIs.
- Quarantine tables are better than silently deleting invalid records.
- GDPR handling should start before the dashboard layer.
- Dashboard views make Gold tables easier to explain.
- Documentation is part of the final data product.

---

## Future improvements

Possible next improvements:

- add Databricks Workflows orchestration
- add incremental ingestion
- add automated data quality tests
- build full Databricks SQL dashboards
- train a fraud-risk model using the AI-ready feature table
- add CI/CD checks for notebooks and SQL

---

## Closing

This project demonstrates the full data engineering lifecycle:

raw landing, Bronze ingestion, Silver quality and GDPR handling, Gold analytics, dashboard views, governance, validation, and final delivery.

It is ready to be used as a portfolio project and as an interview discussion example.