# Quarantine Design

Invalid records should not be silently deleted.

Quarantine tables preserve invalid records with an explanation.

Recommended columns:

```text
record_id
source_table
error_reason
error_severity
quarantine_timestamp
source_file_name
ingest_run_id
original_record_json
```

Example reasons:

```text
missing_customer_id
duplicate_policy_id
invalid_policy_status
negative_claim_amount
missing_policy_reference
payment_before_claim_date
invalid_risk_score
```

Quarantine supports debugging, auditability, and compliance thinking.
