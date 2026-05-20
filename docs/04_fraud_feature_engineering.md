# Fraud Feature Engineering

Day 3 includes one AI-ready feature table:

```text
gold_claim_fraud_features
```

This table is not a model. It is a clean, joined, feature-ready dataset that could later be used for fraud-risk modeling.

## Grain

```text
one row per claim
```

## Required features

claim_amount, premium_amount, coverage_amount, claim_amount_to_coverage_ratio, previous_claims_count, suspicious_amount_flag, duplicate_claim_flag, late_report_flag, high_risk_region_flag, policy_age_days, customer_age, policy_type, bundesland, payment_delay_days, risk_score, fraud_flag.

Avoid direct raw PII in this table.
