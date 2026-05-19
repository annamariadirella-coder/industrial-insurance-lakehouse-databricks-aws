# PII Field Catalog

## Direct PII

- `first_name`
- `last_name`
- `email`
- `phone_number`
- `street`
- `postal_code`

## Sensitive fields

- `date_of_birth`
- `customer_id`
- `iban_hash`

## Recommended handling

- hash email
- hash phone number
- create `customer_hash`
- avoid direct PII in Gold dashboards
- document consent-aware analytics
