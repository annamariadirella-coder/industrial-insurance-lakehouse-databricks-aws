# Milestone 1 — Customers Silver and GDPR

## Goal

Create:

```text
silver_customers
quarantine_invalid_customers
```

## Required work

- trim text columns
- standardize `city` and `bundesland`
- cast `date_of_birth`
- cast `registration_date`
- validate `customer_id`
- remove duplicate `customer_id`
- validate `gdpr_consent`
- hash email
- hash phone number
- create `customer_hash`
- calculate `customer_age`
- avoid exposing raw email and raw phone in Silver

## PII reminder

Customer data contains direct PII. Treat it carefully from the Silver layer onward.
