# Milestone — AWS S3 Lakehouse Bucket


Create one dedicated project bucket.

Example:

```text
s3://insurance-lakehouse-project-<your-name>/
```

Required folders:

```text
raw/customers/
raw/policies/
raw/claims/
raw/payments/
raw/agents/
raw/fraud_indicators/
bronze/
silver/
gold/
checkpoints/
quarantine/
```

Output:
- update `architecture/s3_folder_design.md`
