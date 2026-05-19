# Milestone 6 — Quarantine Tables

Create quarantine tables:

```text
quarantine_invalid_customers
quarantine_invalid_policies
quarantine_invalid_claims
quarantine_invalid_payments
```

Required columns:

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

Do not silently delete invalid records.
