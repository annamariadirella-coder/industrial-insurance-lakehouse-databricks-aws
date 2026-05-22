# Governance and GDPR Strategy

This project simulates a German insurance company, so governance and GDPR awareness are essential.

You must document:

- which fields are PII
- where PII exists
- where PII is hashed or masked
- which layers should be restricted
- which outputs are safe for business users
- how `gdpr_consent` affects analytics
- which roles should access which data

Basic principle:

```text
Raw and Bronze may contain sensitive data.
Silver should clean and reduce risk.
Gold and dashboards should avoid raw PII.
```
