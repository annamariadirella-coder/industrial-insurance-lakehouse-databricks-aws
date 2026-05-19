# Bronze to Silver Concept

## Bronze

Bronze is evidence of arrival.

It preserves raw values and ingestion metadata:

- `ingest_timestamp`
- `ingest_run_id`
- `source_file_name`

## Silver

Silver is evidence of trust.

It includes:

- clean data types
- standardized text values
- deduplicated records
- validated primary keys
- validated foreign keys
- valid business statuses
- valid amounts
- GDPR-aware PII handling
- quarantine for invalid records

## Core idea

Bronze keeps what arrived.  
Silver decides what is trustworthy enough to use.
