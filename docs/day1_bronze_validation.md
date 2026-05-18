# Day 1 Bronze Validation

## Data mode

small

## Validation summary

| Dataset | Raw count | Bronze count | Status |
|---|---:|---:|---|
| customers | 10000 | 10000 | PASS |
| policies | 25000 | 25000 | PASS |
| claims | 50000 | 50000 | PASS |
| payments | 50000 | 50000 | PASS |
| agents | 100 | 100 | PASS |
| fraud_indicators | 50000 | 50000 | PASS |

## Bronze metadata columns

All Bronze tables include:

- ingest_timestamp
- ingest_run_id
- source_file_name

## Notes

Raw data was written to AWS S3 and ingested into Bronze Delta tables in Databricks.  
Raw-to-Bronze row counts matched for all Day 1 datasets.