# Milestone 2 — Policies Silver and Customer Foreign Key Validation

## Goal

Create:

```text
silver_policies
quarantine_invalid_policies
```

## Required work

- validate `policy_id`
- deduplicate by `policy_id`
- validate `customer_id`
- check that policy `customer_id` exists in `silver_customers`
- standardize `policy_type`
- standardize `policy_status`
- cast `premium_amount`
- cast `coverage_amount`
- validate `premium_amount > 0`
- validate `coverage_amount > premium_amount`
- cast dates and timestamps

## Valid values

Policy types: `car`, `home`, `health`, `travel`, `liability`  
Policy statuses: `active`, `cancelled`, `expired`
