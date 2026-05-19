# Milestone 4 — Payments Silver and Date Validation

## Goal

Create:

```text
silver_payments
quarantine_invalid_payments
```

## Required work

- validate `payment_id`
- deduplicate by `payment_id`
- validate `claim_id`
- check that payment `claim_id` exists in `silver_claims`
- cast `payment_date`
- cast `payment_amount`
- validate `payment_amount >= 0`
- validate `payment_status`
- validate `payment_method`
- validate `payment_date >= claim_date`

Valid payment statuses: `paid`, `pending`, `rejected`  
Valid methods: `SEPA`, `bank_transfer`, `card`
