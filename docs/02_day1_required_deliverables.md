# Day 1 Required Deliverables

## Platform
- Databricks trial workspace
- AWS S3 bucket
- S3 folder structure
- S3 access strategy documented

## Repository
- `README.md`
- `config/project_config.yml`
- `config/data_size_config.yml`
- `architecture/s3_folder_design.md`
- `docs/day1_setup_notes.md`

## Data
- generated synthetic customers, policies, claims, payments, agents, fraud indicators
- raw data written to S3
- small mode completed

## Bronze
- six Bronze Delta tables
- metadata columns:
  - `ingest_timestamp`
  - `ingest_run_id`
  - `source_file_name`

## Validation
- raw counts
- Bronze counts
- raw-to-Bronze comparison
- validation summary
