# Final Validation Strategy

## Purpose

This document explains the final validation approach for the Week 11 Industrial Insurance Lakehouse project.

The goal is to prove that the lakehouse is complete, trustworthy, dashboard-ready, and safe for business consumption.

---

## Validation scope

The final validation covers:

- Gold table existence
- Gold table row counts
- Dashboard view existence
- Dashboard view row counts
- AI-ready feature table grain
- PII exposure checks
- Quarantine evidence
- KPI sanity checks

---

## Gold table validation

All required Gold tables were validated in `insurance_lakehouse.gold`.

| Gold table | Row count | Status |
|---|---:|---|
| gold_claims_overview | 30158 | PASS |
| gold_policy_performance | 540 | PASS |
| gold_customer_risk_profile | 10000 | PASS |
| gold_claims_payment_summary | 50000 | PASS |
| gold_fraud_risk_summary | 810 | PASS |
| gold_agent_performance | 1000 | PASS |
| gold_claim_fraud_features | 50000 | PASS |

---

## Dashboard view validation

All required dashboard views were created in `insurance_lakehouse.gold`.

| Dashboard view | Row count | Status |
|---|---:|---|
| vw_executive_insurance_overview | 1 | PASS |
| vw_claims_operations | 1350 | PASS |
| vw_policy_portfolio | 540 | PASS |
| vw_fraud_risk_monitoring | 810 | PASS |
| vw_agent_regional_performance | 1000 | PASS |
| vw_data_quality_monitoring | 5 | PASS |

---

## Feature table grain validation

The AI-ready feature table must have one row per claim.

Validated table:

`insurance_lakehouse.gold.gold_claim_fraud_features`

| Check | Result |
|---|---:|
| rows | 50000 |
| distinct claim_id | 50000 |
| duplicate claim_id groups | 0 |

Status: PASS

---

## PII exposure validation

Dashboard views were checked for raw PII fields.

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

---

## Quarantine evidence

The quarantine layer preserves invalid records instead of silently deleting them.

| Dataset | Quarantine rows | Main reason |
|---|---:|---|
| customers | 0 | none |
| policies | 0 | none |
| claims | 0 | none |
| payments | 22311 | payment_before_claim_date |
| fraud_indicators | 31425 | duplicate_claim_id |

---

## KPI sanity checks

The final validation also reviewed key business metrics for obvious issues.

| Check | Purpose | Status |
|---|---|---|
| Gold row counts greater than zero | Ensure outputs are populated | PASS |
| Dashboard views return rows | Ensure views are usable | PASS |
| Feature table duplicate claim_id count = 0 | Ensure correct AI feature grain | PASS |
| Dashboard views do not expose raw PII | Ensure business-facing layer is privacy-safe | PASS |
| Quarantine counts documented | Ensure invalid records remain traceable | PASS |

---

## Evidence files

Supporting evidence is stored in:

- outputs/final_validation_summary.md
- outputs/final_project_inventory.md
- outputs/dashboard_view_counts.md
- outputs/pii_exposure_check.md
- screenshots/day5/

---

## Final validation status

The final delivery validation passed.

Status: PASS