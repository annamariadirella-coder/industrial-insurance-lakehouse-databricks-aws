# Day 2 Quality Summary

 Dataset | Bronze rows | Silver rows | Quarantine rows | Status |
---|---:|---:|---:|---|
 customers | 10000 | 10000 | 0 | PASS |
 policies | 25000 | 25000 | 0 | PASS |
 claims | 50000 | 50000 | 0 | PASS |
 payments | 50000 | 27689 | 22311 | PASS |
 agents | 1000 | 1000 | 0 | PASS |
 fraud_indicators | 50000 | 18575 | 31425 | PASS |

## Main findings

- Customers, policies, claims, and agents passed Silver validation without quarantine records.
- Payments produced quarantine records because some payment dates were before the related claim dates.
- Fraud indicators produced quarantine records because duplicate claim IDs were detected.
- Invalid records were not silently deleted. They were preserved in quarantine tables with error reasons.

## Ready for Day 3?

Yes. The Silver layer is ready for Day 3 Gold analytics because all Bronze rows are accounted for through Silver plus quarantine.
