# Day 2 GDPR and PII Handling

## PII fields identified

Customer data contains direct and indirect personal data.

Direct PII fields:

- first_name
- last_name
- email
- phone_number
- street
- postal_code
- date_of_birth

Sensitive financial field:

- iban_hash

## Handling in Silver

The following raw PII fields were removed from silver_customers:

- first_name
- last_name
- email
- phone_number
- street
- postal_code
- date_of_birth

The following pseudonymized fields were kept:

- customer_hash
- email_hash
- phone_hash

The following analytics-safe fields were kept:

- customer_id
- gender
- city
- bundesland
- country
- registration_date
- gdpr_consent
- customer_segment
- customer_age

## Payment data

silver_payments keeps iban_hash, not raw bank data.

## GDPR validation result

The GDPR/PII validation notebook confirmed that raw PII fields are not exposed in Silver and that hashed fields are present.

Status: PASS

## Access recommendation

- Bronze should be treated as restricted because it may contain raw PII.
- Silver reduces PII exposure through hashing and field removal.
- Gold dashboards should avoid direct PII and use aggregated or pseudonymized outputs.
