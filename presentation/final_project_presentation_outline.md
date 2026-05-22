# Presentation Strategy

## Purpose

This document prepares the final presentation story for the Week 11 Industrial Insurance Lakehouse project.

The goal is to explain the project clearly as both a technical data engineering implementation and a business-facing insurance analytics product.

---

## Presentation objective

The presentation should show that the project is:

- complete
- validated
- governed
- dashboard-ready
- privacy-aware
- suitable for portfolio and interview discussion

The presentation should not be a notebook walkthrough.

It should tell a clear story:

1. Business problem
2. Architecture
3. Data pipeline
4. Data quality and governance
5. Gold analytics
6. Dashboard views
7. AI-ready fraud features
8. Validation evidence
9. Lessons learned
10. Future improvements

---

## Opening statement

I built an industrial-style insurance lakehouse for Rheinland Versicherung AG using Databricks on AWS, AWS S3, Delta Lake, PySpark, Spark SQL, Unity Catalog, and medallion architecture.

The project generates synthetic German insurance data, lands it in S3, ingests it into Bronze, cleans and validates it in Silver, preserves invalid records in quarantine, creates Gold KPI tables and AI-ready fraud features, and exposes dashboard-ready views for business users.

---

## Slide structure

### Slide 1 - Project title and business context

**Title**

Industrial Insurance Lakehouse on Databricks and AWS

**Key message**

This project simulates a German insurance company modernizing its reporting and analytics platform.

**Speaking points**

- Fictional company: Rheinland Versicherung AG
- Insurance domains: customers, policies, claims, payments, agents, fraud indicators
- Business goals: trusted analytics, fraud-risk monitoring, dashboard-ready KPIs, AI-ready features

---

### Slide 2 - Business problem

**Key message**

Insurance data is often fragmented, sensitive, and difficult to trust without proper engineering controls.

**Speaking points**

- Raw data alone is not enough for business analytics
- Claims, payments, policies, and fraud signals need relationship validation
- GDPR-sensitive fields require careful handling
- Business users need clear KPIs and dashboard-ready outputs

---

### Slide 3 - Lakehouse architecture

**Key message**

The project follows a medallion architecture from raw data to business-ready views.

**Flow**

Synthetic data  
→ AWS S3 raw landing  
→ Bronze Delta tables  
→ Silver trusted data and quarantine  
→ Gold KPI tables and AI-ready feature table  
→ Dashboard-ready SQL views

**Speaking points**

- Bronze preserves what arrived
- Silver proves what can be trusted
- Gold proves what the business can use
- Day 5 proves the project can be delivered and explained

---

### Slide 4 - Day 1: Raw and Bronze

**Key message**

Day 1 created the technical foundation.

**Speaking points**

- Databricks workspace connected to AWS S3
- Synthetic German insurance data generated
- Raw CSV data landed in S3
- Bronze Delta tables created
- Ingestion metadata added
- Raw-to-Bronze validation completed

**Evidence to show**

- S3 bucket or folder structure screenshot
- Bronze table validation screenshot
- README Day 1 section

---

### Slide 5 - Day 2: Silver, quality, quarantine, and GDPR

**Key message**

Silver turns raw ingested data into trusted, reusable, GDPR-aware data.

**Speaking points**

- Customers, policies, claims, payments, agents, and fraud indicators cleaned
- Primary keys and foreign keys validated
- Invalid records moved to quarantine
- Raw customer PII removed from Silver
- Hashes kept for pseudonymized analytics

**Important results**

| Dataset | Silver rows | Quarantine rows |
|---|---:|---:|
| customers | 10000 | 0 |
| policies | 25000 | 0 |
| claims | 50000 | 0 |
| payments | 27689 | 22311 |
| agents | 1000 | 0 |
| fraud_indicators | 18575 | 31425 |

**Evidence to show**

- Day 2 quality summary screenshot
- Quarantine review screenshot
- GDPR PII check screenshot

---

### Slide 6 - Day 3: Gold KPIs and AI-ready features

**Key message**

Gold transforms trusted Silver data into business-ready analytics.

**Gold tables**

- gold_claims_overview
- gold_policy_performance
- gold_customer_risk_profile
- gold_claims_payment_summary
- gold_fraud_risk_summary
- gold_agent_performance
- gold_claim_fraud_features

**Speaking points**

- Each Gold table has a clear business purpose and grain
- Payments were aggregated before joining to claims
- The AI-ready feature table has one row per claim
- Gold validation confirmed row counts and duplicate grain checks

**Evidence to show**

- Gold row counts screenshot
- Feature table sample screenshot
- Gold validation screenshot

---

### Slide 7 - Dashboard-ready views

**Key message**

Day 5 exposes Gold outputs through business-friendly SQL views.

**Dashboard views**

| View | Purpose |
|---|---|
| vw_executive_insurance_overview | Executive KPI overview |
| vw_claims_operations | Claims operations monitoring |
| vw_policy_portfolio | Policy portfolio analytics |
| vw_fraud_risk_monitoring | Fraud-risk monitoring |
| vw_agent_regional_performance | Agent and regional performance |
| vw_data_quality_monitoring | Quarantine and data quality monitoring |

**Speaking points**

- Views simplify business consumption
- Views avoid raw PII exposure
- Views are ready for dashboards or portfolio screenshots

**Evidence to show**

- Executive KPI view screenshot
- Fraud-risk monitoring screenshot
- Dashboard view counts screenshot

---

### Slide 8 - Governance and GDPR

**Key message**

The project applies privacy-aware design across the lakehouse.

**Speaking points**

- Raw PII is restricted to raw/Bronze
- Silver removes or hashes sensitive customer fields
- Gold and dashboard views avoid raw personal data
- Quarantine tables preserve audit evidence
- Role-based access model documented

**PII fields checked**

- first_name
- last_name
- email
- phone_number
- street
- postal_code
- date_of_birth
- iban
- iban_hash

**Result**

No checked PII fields were exposed in dashboard views.

**Evidence to show**

- Day 5 PII exposure check screenshot
- Governance document in repo

---

### Slide 9 - Final validation

**Key message**

The final delivery was validated across tables, views, grain, PII, and quarantine evidence.

**Validation results**

- Gold tables exist and return rows
- Dashboard views exist and return rows
- Feature table has one row per claim
- Duplicate claim_id groups = 0
- Dashboard views expose no checked PII fields
- Quarantine counts are documented

**Evidence to show**

- Final validation screenshot
- Feature table duplicate check screenshot
- Final project inventory file

---

### Slide 10 - Lessons learned and next steps

**Key message**

The project demonstrates both technical data engineering and business-facing delivery.

**Lessons learned**

- Clear table grain prevents misleading KPIs
- Quarantine tables are better than silently deleting invalid records
- GDPR-aware design must be considered from Silver onward
- Dashboard views make Gold tables easier to consume
- Documentation is part of the final data product

**Future improvements**

- Add automated orchestration with Databricks Workflows
- Add incremental ingestion
- Add automated data quality tests
- Build full Databricks SQL dashboards
- Train a fraud-risk model using the AI-ready feature table
- Add CI/CD checks for notebooks and SQL

---

## Demo script

### 1. Open the GitHub README

Explain the project goal, architecture, and final outputs.

### 2. Show the architecture documentation

Explain the flow from synthetic data to S3, Bronze, Silver, Gold, and dashboard views.

### 3. Open Catalog Explorer

Show the schemas:

- bronze
- silver
- quarantine
- gold

### 4. Show one dashboard view query

Recommended view:

- vw_executive_insurance_overview

Explain the executive KPIs.

### 5. Show fraud monitoring

Recommended view:

- vw_fraud_risk_monitoring

Explain risk bands, high-risk claims, and fraud indicators.

### 6. Show data quality monitoring

Recommended view:

- vw_data_quality_monitoring

Explain quarantine counts and why this supports trust.

### 7. Show GDPR evidence

Open:

- docs/04_governance_gdpr_strategy.md
- outputs/pii_exposure_check.md

Explain that dashboard views expose no checked raw PII.

### 8. Show AI-ready feature table

Open:

- gold_claim_fraud_features
- outputs/day3_feature_table_profile.md

Explain that the table has one row per claim and can support future fraud-risk modelling.

### 9. Close with final validation

Open:

- outputs/final_validation_summary.md

Explain that the project is complete, validated, governed, and dashboard-ready.

---

## Short speaking points

### Business value

This lakehouse turns fragmented insurance data into trusted, dashboard-ready analytics for claims, policies, payments, agents, fraud-risk monitoring, and data quality.

### Technical value

The project demonstrates Databricks, AWS S3, Delta Lake, PySpark, Spark SQL, Unity Catalog, medallion architecture, data quality rules, and validation.

### Governance value

The project identifies PII, removes or hashes sensitive customer fields, preserves quarantine evidence, and documents a role-based access model.

### AI-readiness

The project creates a claim-level fraud feature table with one row per claim, engineered features, risk indicators, payment behavior, and no raw customer PII.

---

## Screenshot checklist

Use these screenshots for the final presentation:

- GitHub README overview
- lakehouse architecture or repository architecture file
- S3 raw landing or folder structure
- Bronze validation
- Day 2 quality summary
- Day 2 quarantine review
- Day 2 GDPR PII check
- Day 3 Gold row counts
- Day 3 feature table sample
- Day 3 Gold validation summary
- Day 5 executive KPI view
- Day 5 fraud-risk monitoring view
- Day 5 dashboard view counts
- Day 5 PII exposure check
- Day 5 final validation summary

---

## Final presentation closing

This project demonstrates how to build, validate, govern, document, and present a cloud data engineering project using Databricks and AWS.

It shows the full journey from raw insurance data to trusted Silver data, business-ready Gold KPIs, fraud-risk analytics, AI-ready features, dashboard views, and final delivery documentation.