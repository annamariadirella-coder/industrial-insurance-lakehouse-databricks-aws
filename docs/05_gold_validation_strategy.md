# Gold Validation Strategy

Gold tables are business-facing. A wrong Gold output can create wrong management reporting.

Required checks:

1. Table exists.
2. Row count is greater than zero.
3. Grain uniqueness.
4. Null checks on important fields.
5. KPI sanity checks.
6. No unnecessary raw PII exposure.

Example duplicate check:

```sql
SELECT claim_id, COUNT(*)
FROM insurance_lakehouse.gold.gold_claim_fraud_features
GROUP BY claim_id
HAVING COUNT(*) > 1;
```
