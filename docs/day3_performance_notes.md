# Day 3 Performance Notes

## Scope

This document records the main performance considerations for the Day 3 Gold layer.

The focus was on building business-ready Gold tables while keeping the transformations Spark-friendly and avoiding common performance mistakes such as unnecessary columns, repeated actions, and one-to-many join duplication.

---

## Performance observation 1 — Column pruning before joins

For the `gold_claim_fraud_features` table, only the required columns were selected from each Silver input table before joining.

This reduced the amount of data carried through the execution plan and also avoided duplicate technical columns such as:

- ingest_run_id
- ingest_timestamp
- source_file_name

This was especially important after the first version of the feature table failed because duplicate metadata columns were carried through the joins.

---

## Performance observation 2 — Payments aggregated before joining to claims

Payments can contain multiple rows per claim.

To preserve the required grain of one row per claim, `silver_payments` was aggregated by `claim_id` before joining to `silver_claims`.

This avoided multiplying claim rows and protected claim-level KPIs and features from duplication.

Derived payment features included:

- total_paid_amount
- payment_count
- payment_rejection_count
- first_payment_date
- payment_delay_days

---

## Performance observation 3 — Feature table grain validation

The AI-ready feature table was validated after creation.

Validation result:

| Metric | Count |
|---|---:|
| rows | 50000 |
| distinct claim_id | 50000 |
| duplicate claim_id count | 0 |

This confirms that the final table respects the intended grain of one row per claim.

---

## Performance observation 4 — Explain plan inspected

The execution plan for `gold_claim_fraud_features` was inspected with:

```python
gold_claim_fraud_features.explain(True)