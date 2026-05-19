# Day 2 Data Quality Report

## Scope

Day 2 transformed Bronze insurance data into trusted Silver tables for Rheinland Versicherung AG.

The work covered:

- customer cleaning and GDPR-safe PII handling
- policy validation and customer foreign key checks
- claims validation and relationship checks
- payment validation and date logic checks
- agent validation
- fraud indicator validation
- quarantine table creation
- data quality summary

## Quality summary

 Dataset | Bronze rows | Silver rows | Quarantine rows | Status |
---|---:|---:|---:|---|
 customers | 10000 | 10000 | 0 | PASS |
 policies | 25000 | 25000 | 0 | PASS |
 claims | 50000 | 50000 | 0 | PASS |
 payments | 50000 | 27689 | 22311 | PASS |
 agents | 1000 | 1000 | 0 | PASS |
 fraud_indicators | 50000 | 18575 | 31425 | PASS |

## Quarantine results

 Dataset | Error reason | Count |
---|---|---:|
 payments | payment_before_claim_date | 22311 |
 fraud_indicators | duplicate_claim_id | 31425 |

## Interpretation

All Bronze records are accounted for either in trusted Silver tables or in quarantine tables.

Payments had invalid date logic where payment_date was earlier than claim_date. These records were excluded from Silver and preserved in quarantine.

Fraud indicators contained duplicate claim_id values. These records were excluded from Silver and preserved in quarantine.

## Day 3 readiness

The Silver layer is ready for Day 3 Gold analytics. Trusted records are available in Silver, while invalid records remain traceable in quarantine.
