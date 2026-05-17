# Milestone — Bronze Delta Ingestion


Read raw S3 files and write Bronze Delta tables.

Required metadata:
- `ingest_timestamp`
- `ingest_run_id`
- `source_file_name`

Bronze should preserve raw values and avoid heavy cleaning.
