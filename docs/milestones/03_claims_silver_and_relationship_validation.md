# Milestone 3 — Claims Silver and Relationship Validation

## Goal

Create:

```text
silver_claims
quarantine_invalid_claims
```

## Required work

- validate `claim_id`
- deduplicate by `claim_id`
- validate `policy_id`
- validate `customer_id`
- check that claim `policy_id` exists in `silver_policies`
- check that claim `customer_id` exists in `silver_customers`
- cast `claim_date`
- cast `claim_amount`
- validate `claim_amount > 0`
- standardize claim status, type, and reported channel

Valid claim statuses: `open`, `approved`, `rejected`, `under_review`, `paid`
