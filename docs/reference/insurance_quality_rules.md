# Insurance Data Quality Rules

| Rule | Dataset |
|---|---|
| `customer_id` must not be null | customers |
| `policy_id` must be unique | policies |
| `claim_id` must be unique | claims |
| `payment_id` must be unique | payments |
| policy `customer_id` must exist in customers | policies |
| claim `policy_id` must exist in policies | claims |
| claim `customer_id` must exist in customers | claims |
| `claim_amount > 0` | claims |
| `premium_amount > 0` | policies |
| `coverage_amount > premium_amount` | policies |
| `payment_amount >= 0` | payments |
| `risk_score` between 0 and 100 | fraud indicators |
| `gdpr_consent` must be true or false | customers |
| payment date must not be before claim date | payments |
