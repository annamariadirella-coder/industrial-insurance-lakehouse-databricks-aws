# Final Validation Summary

## Scope

This file summarizes the final validation evidence for the Week 11 Industrial Insurance Lakehouse project.

The validation covers:

- Gold table existence and row counts
- Dashboard view existence and row counts
- Feature table grain validation
- PII exposure checks
- Quarantine evidence

---

## Gold table row counts

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

## Dashboard view row counts

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

The AI-ready feature table was validated to confirm one row per claim.

| Check | Result |
|---|---:|
| rows | 50000 |
| distinct claim_id | 50000 |
| duplicate claim_id groups | 0 |

Status: PASS

---

## PII exposure validation

Dashboard views were checked for raw PII exposure.

Checked PII fields:

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

| Dataset | Quarantine rows | Main reason |
|---|---:|---|
| customers | 0 | none |
| policies | 0 | none |
| claims | 0 | none |
| payments | 22311 | payment_before_claim_date |
| fraud_indicators | 31425 | duplicate_claim_id |

---

## Final status

The project is ready for final presentation and portfolio review.

Final validation status: PASS