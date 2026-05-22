# Final Demo Script

## Purpose

This demo script prepares a clean walkthrough of the Week 11 Industrial Insurance Lakehouse project.

The goal is to avoid random clicking and show only the most important evidence.

---

## Demo duration

Recommended length: 7–10 minutes.

---

## Demo flow

### 1. Open the GitHub repository

Open the repository:

`industrial-insurance-lakehouse-databricks-aws`

Explain:

- this is the final standalone public repository
- the project covers Raw, Bronze, Silver, Quarantine, Gold, dashboard views, governance, and final validation
- the fictional company is Rheinland Versicherung AG

Key sentence:

“I built an industrial-style insurance lakehouse on Databricks and AWS for a fictional German insurance company.”

---

### 2. Show the README

Open `README.md`.

Point out:

- project title
- business context
- architecture overview
- Day 1, Day 2, Day 3, Day 5 sections
- final outputs
- validation and documentation links

Key sentence:

“The README is structured so that a reviewer can understand the project without opening every notebook.”

---

### 3. Show the architecture

Open:

`architecture/lakehouse_architecture.md`

Explain the flow:

Synthetic data  
→ S3 raw landing  
→ Bronze Delta tables  
→ Silver trusted tables and quarantine  
→ Gold KPI tables and AI-ready feature table  
→ Dashboard-ready SQL views

Key sentence:

“The project follows the medallion architecture: Bronze preserves what arrived, Silver proves what can be trusted, and Gold proves what the business can use.”

---

### 4. Show Catalog Explorer

In Databricks, open Catalog Explorer and show:

- `insurance_lakehouse.bronze`
- `insurance_lakehouse.silver`
- `insurance_lakehouse.quarantine`
- `insurance_lakehouse.gold`

Explain:

- Bronze contains raw ingested Delta tables
- Silver contains cleaned and trusted data
- Quarantine contains invalid records with error reasons
- Gold contains business KPIs, fraud analytics, features, and dashboard views

---

### 5. Show Day 2 data quality evidence

Open:

`outputs/day2_quality_summary.md`

Explain:

- customers, policies, claims, and agents passed validation
- payments had quarantine records because some payment dates were before claim dates
- fraud indicators had quarantine records because duplicate claim IDs were detected
- invalid records were preserved instead of silently deleted

Key sentence:

“Silver is not just cleaned data. It is trusted data with validation and quarantine evidence.”

---

### 6. Show GDPR / PII evidence

Open:

`docs/04_governance_gdpr_strategy.md`

Then open:

`outputs/pii_exposure_check.md`

Explain:

- raw customer PII was removed or hashed
- email and phone were hashed
- date_of_birth was transformed into customer_age
- dashboard views expose no checked raw PII fields

Key sentence:

“The dashboard layer is designed to be business-facing and PII-safe.”

---

### 7. Show Gold table outputs

Open:

`outputs/day3_gold_row_counts.md`

Explain:

- all required Gold tables were created
- each Gold table has a clear grain
- the AI-ready feature table has one row per claim

Key sentence:

“Gold tables are not copies of Silver. They answer business questions with defined KPIs and grains.”

---

### 8. Show the AI-ready fraud feature table

Open:

`outputs/day3_feature_table_profile.md`

Or show the table in Databricks:

`insurance_lakehouse.gold.gold_claim_fraud_features`

Explain:

- one row per claim
- includes claim amount, policy information, payment behavior, fraud indicators, risk score, and risk band
- no raw customer PII
- ready for future fraud-risk modelling

Key sentence:

“AI-ready means the data is clean, joined, validated, and structured at the right grain. No model is trained today.”

---

### 9. Show dashboard views

In Databricks, query or open:

- `vw_executive_insurance_overview`
- `vw_fraud_risk_monitoring`
- `vw_data_quality_monitoring`

Explain:

- executive view gives leadership KPIs
- fraud view supports risk monitoring
- data quality view shows quarantine counts

Key sentence:

“The dashboard views make the Gold layer easier and safer for business users to consume.”

---

### 10. Show final validation

Open:

`outputs/final_validation_summary.md`

Explain:

- Gold tables return rows
- dashboard views return rows
- feature table duplicate claim_id groups = 0
- dashboard views expose no checked raw PII
- quarantine evidence is documented

Key sentence:

“The final validation status is PASS.”

---

### 11. Show screenshots

Open:

`screenshots/day5/`

Recommended screenshots:

- executive KPI view
- claims operations view
- policy portfolio view
- fraud risk monitoring view
- agent regional performance view
- data quality monitoring view
- dashboard view counts
- PII exposure check
- final validation summary

Explain:

“These screenshots make the project easy to present even without running the notebooks live.”

---

### 12. Close with lessons learned

Main lessons:

- table grain must be defined before building KPIs
- payments should be aggregated before joining to claims
- invalid data should be quarantined, not silently deleted
- GDPR handling should be designed before dashboards
- documentation is part of the final data product

Closing sentence:

“This project demonstrates the full data engineering lifecycle: raw landing, Bronze ingestion, Silver quality and GDPR handling, Gold analytics, dashboard views, governance, validation, and final delivery.”

---

## What not to do during the demo

Avoid:

- scrolling through every notebook cell
- showing old errors that were fixed
- opening raw PII fields unnecessarily
- clicking randomly through folders
- spending too long on setup details
- explaining every line of PySpark code

Focus on:

- architecture
- business value
- validation evidence
- governance
- dashboard outputs
- AI-ready feature design

---

## Backup plan

If Databricks is slow or unavailable, use:

- GitHub README
- docs files
- outputs files
- screenshots folder

This is enough to explain the full project without running live compute.