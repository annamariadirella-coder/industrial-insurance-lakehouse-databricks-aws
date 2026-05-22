# Final Project Inventory

## Scope

This inventory lists the main objects created for the Week 11 Industrial Insurance Lakehouse project.

It includes Bronze, Silver, Quarantine, Gold, and dashboard view objects.

---

## Bronze tables

| Layer | Object | Purpose | Exists? | Rows |
|---|---|---|---|---:|
| Bronze | bronze_customers | Raw ingested customer records | yes | 10000 |
| Bronze | bronze_policies | Raw ingested policy records | yes | 25000 |
| Bronze | bronze_claims | Raw ingested claim records | yes | 50000 |
| Bronze | bronze_payments | Raw ingested payment records | yes | 50000 |
| Bronze | bronze_agents | Raw ingested agent records | yes | 1000 |
| Bronze | bronze_fraud_indicators | Raw ingested fraud indicator records | yes | 50000 |

---

## Silver tables

| Layer | Object | Purpose | Exists? | Rows |
|---|---|---|---|---:|
| Silver | silver_customers | Trusted GDPR-aware customer dimension | yes | 10000 |
| Silver | silver_policies | Trusted policy data with customer validation | yes | 25000 |
| Silver | silver_claims | Trusted claim events with relationship validation | yes | 50000 |
| Silver | silver_payments | Trusted payment records after date and claim checks | yes | 27689 |
| Silver | silver_agents | Trusted agent dimension | yes | 1000 |
| Silver | silver_fraud_indicators | Trusted fraud indicators after duplicate checks | yes | 18575 |

---

## Quarantine tables

| Layer | Object | Purpose | Exists? | Rows |
|---|---|---|---|---:|
| Quarantine | quarantine_invalid_customers | Invalid customer records with error reasons | yes | 0 |
| Quarantine | quarantine_invalid_policies | Invalid policy records with error reasons | yes | 0 |
| Quarantine | quarantine_invalid_claims | Invalid claim records with error reasons | yes | 0 |
| Quarantine | quarantine_invalid_payments | Invalid payment records with error reasons | yes | 22311 |
| Quarantine | quarantine_invalid_fraud_indicators | Invalid fraud indicator records with error reasons | yes | 31425 |

---

## Gold tables

| Layer | Object | Purpose | Exists? | Rows |
|---|---|---|---|---:|
| Gold | gold_claims_overview | Claims operations KPIs | yes | 30158 |
| Gold | gold_policy_performance | Policy portfolio and premium KPIs | yes | 540 |
| Gold | gold_customer_risk_profile | Customer-level risk profile | yes | 10000 |
| Gold | gold_claims_payment_summary | Claim-level payment summary | yes | 50000 |
| Gold | gold_fraud_risk_summary | Fraud-risk monitoring summary | yes | 810 |
| Gold | gold_agent_performance | Agent and regional performance KPIs | yes | 1000 |
| Gold | gold_claim_fraud_features | AI-ready claim-level fraud feature table | yes | 50000 |

---

## Dashboard views

| Layer | Object | Purpose | Exists? | Rows |
|---|---|---|---|---:|
| View | vw_executive_insurance_overview | Executive KPI overview | yes | 1 |
| View | vw_claims_operations | Claims operations dashboard view | yes | 1350 |
| View | vw_policy_portfolio | Policy portfolio dashboard view | yes | 540 |
| View | vw_fraud_risk_monitoring | Fraud-risk dashboard view | yes | 810 |
| View | vw_agent_regional_performance | Agent performance dashboard view | yes | 1000 |
| View | vw_data_quality_monitoring | Data quality and quarantine monitoring view | yes | 5 |

---

## Summary

The final project contains all required medallion layers and dashboard-ready views.

All core objects exist and return rows where expected.

Final object inventory status: PASS