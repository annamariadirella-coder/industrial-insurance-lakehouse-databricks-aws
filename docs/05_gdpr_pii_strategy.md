# GDPR and PII Strategy

Insurance data is sensitive.

## PII fields

```text
first_name
last_name
email
phone_number
street
postal_code
date_of_birth
iban_hash
```

## Recommended handling

- hash email
- hash phone number
- create a stable `customer_hash`
- avoid exposing raw contact data in Gold
- use `gdpr_consent` in analytics logic where required
- document what is masked and why

## Important principle

Gold dashboards should not expose personal data.  
Business users should consume aggregated, masked, or pseudonymized outputs.
