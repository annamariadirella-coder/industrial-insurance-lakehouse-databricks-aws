# PII Exposure Check

## Scope

This check verifies whether the Day 5 dashboard views expose raw personal data.

Checked views:

- vw_executive_insurance_overview
- vw_claims_operations
- vw_policy_portfolio
- vw_fraud_risk_monitoring
- vw_agent_regional_performance
- vw_data_quality_monitoring

## PII fields checked

- first_name
- last_name
- email
- phone_number
- street
- postal_code
- date_of_birth
- iban
- iban_hash

## Result

| Dashboard view | Exposed PII fields | Status |
|---|---|---|
| vw_executive_insurance_overview | none | PASS |
| vw_claims_operations | none | PASS |
| vw_policy_portfolio | none | PASS |
| vw_fraud_risk_monitoring | none | PASS |
| vw_agent_regional_performance | none | PASS |
| vw_data_quality_monitoring | none | PASS |

## Summary

No raw PII fields were exposed in the Day 5 dashboard views.

The dashboard layer is safe for business users and uses aggregated, operational, or non-sensitive fields only.

Status: PASS