# Governance and GDPR Strategy

## Purpose

This document explains how the insurance lakehouse handles privacy, governance, access control, and GDPR-aware analytics.

The project uses synthetic data, but the design follows realistic principles for a German insurance company.

---

## PII classification

The following fields are treated as personal or sensitive data.

| Field | Type | Handling |
|---|---|---|
| first_name | direct PII | restricted to Bronze, removed from Silver and Gold |
| last_name | direct PII | restricted to Bronze, removed from Silver and Gold |
| email | direct PII | hashed in Silver, not exposed in Gold or dashboard views |
| phone_number | direct PII | hashed in Silver, not exposed in Gold or dashboard views |
| street | direct PII | restricted to Bronze, removed from Silver and Gold |
| postal_code | indirect PII | removed from Silver customer output |
| date_of_birth | indirect PII | transformed into customer_age, removed from Silver and Gold |
| iban_hash | financial identifier | hashed value only, not exposed in dashboard views |
| customer_id | operational identifier | used for joins and analytics, not raw personal identity |

---

## Layer-by-layer governance design

### Raw / S3

Raw CSV files are landed in AWS S3.

This layer is treated as restricted because it may contain raw personal data and unvalidated records.

Access should be limited to data engineers and platform administrators.

### Bronze

Bronze preserves what arrived.

Bronze tables keep:

- raw source fields
- ingestion metadata
- source file names
- ingest run identifiers

Bronze is useful for traceability and audit, but it should not be broadly exposed to analysts.

### Silver

Silver creates trusted, reusable, GDPR-aware data.

Customer PII handling in Silver:

- raw names removed
- email hashed
- phone number hashed
- date_of_birth transformed into customer_age
- customer_hash created for pseudonymized analytics
- raw address-level fields removed

Silver keeps data useful for analytics while reducing unnecessary personal data exposure.

### Quarantine

Invalid records are preserved in quarantine tables with:

- record identifier
- source table
- error reason
- error severity
- quarantine timestamp
- source file name
- ingest run identifier
- original record JSON

Quarantine supports:

- debugging
- auditability
- data quality monitoring
- evidence-based pipeline improvement

### Gold

Gold creates business KPIs, fraud-risk summaries, agent performance metrics, payment summaries, and AI-ready features.

Gold does not expose raw personal fields such as:

- first_name
- last_name
- email
- phone_number
- street
- date_of_birth

Gold outputs are designed for business users and analytical consumption.

### Dashboard views

Dashboard views are business-facing and PII-safe.

The final PII exposure check confirmed that no checked raw PII fields are exposed in the dashboard views.

Status: PASS

---

## Role-based access model

| Role | Access | Purpose |
|---|---|---|
| Data Engineers | Raw, Bronze, Silver, Gold, Quarantine | Build, operate, validate, and debug pipelines |
| Analysts | Gold tables and dashboard views | Business analysis and reporting |
| Fraud Analysts | Fraud summaries and claim fraud feature table | Investigate fraud-risk patterns |
| Compliance | Quality reports, quarantine evidence, GDPR documentation | Review controls and audit evidence |
| Executives | Aggregated dashboard views only | Strategic decisions |

---

## Consent-aware analytics

The field `gdpr_consent` is preserved in the trusted customer layer and customer-level Gold outputs.

In a production environment, customer-level analytics could be restricted to records where:

```sql
gdpr_consent = true
```

A possible consent-aware view would be:

```sql
CREATE OR REPLACE VIEW insurance_lakehouse.gold.vw_consent_customer_analytics AS
SELECT *
FROM insurance_lakehouse.gold.gold_customer_risk_profile
WHERE gdpr_consent = true;
```

For this training project, the consent-aware logic is documented and the field is retained for governance-aware analytics.

---

## Dashboard PII exposure validation

The following dashboard views were checked:

- vw_executive_insurance_overview
- vw_claims_operations
- vw_policy_portfolio
- vw_fraud_risk_monitoring
- vw_agent_regional_performance
- vw_data_quality_monitoring

The following fields were checked:

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

---

## Retention and audit considerations

In a production implementation:

- Raw and Bronze data should have restricted access.
- Quarantine records should be retained for audit and debugging.
- Access to sensitive layers should be logged.
- Dashboard views should remain aggregated or pseudonymized.
- Retention policies should be aligned with legal and business requirements.
- Sensitive data access should be reviewed periodically.

---

## Final governance status

The project demonstrates GDPR-aware data engineering through:

- PII identification
- hashing and pseudonymization
- removal of raw PII from Silver and Gold
- quarantine evidence
- dashboard PII checks
- role-based access model
- consent-aware analytics design

Final governance status: PASS