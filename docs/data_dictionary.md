# Data Dictionary

## Purpose

This document describes the main tables and dashboard views in the Week 11 Industrial Insurance Lakehouse project.

It explains the layer, purpose, grain, important columns, sensitive fields, and source objects for each main output.

---

## Bronze layer

Bronze preserves what arrived from raw S3 landing.

| Object | Grain | Purpose | Key columns | Sensitive fields | Source |
|---|---|---|---|---|---|
| bronze_customers | one row per raw customer record | Raw customer ingestion evidence | customer_id, email, phone_number, city, bundesland, gdpr_consent | first_name, last_name, email, phone_number, street, postal_code, date_of_birth | raw customer CSV |
| bronze_policies | one row per raw policy record | Raw policy ingestion evidence | policy_id, customer_id, policy_type, policy_status, premium_amount | customer_id | raw policy CSV |
| bronze_claims | one row per raw claim record | Raw claim ingestion evidence | claim_id, policy_id, customer_id, claim_date, claim_amount, claim_status | customer_id | raw claim CSV |
| bronze_payments | one row per raw payment record | Raw payment ingestion evidence | payment_id, claim_id, payment_date, payment_amount, payment_status, iban_hash | iban_hash | raw payment CSV |
| bronze_agents | one row per raw agent record | Raw agent ingestion evidence | agent_id, agent_name, region, city, commission_rate | none critical | raw agent CSV |
| bronze_fraud_indicators | one row per raw fraud indicator record | Raw fraud signal ingestion evidence | claim_id, risk_score, duplicate_claim_flag, late_report_flag | claim_id | raw fraud indicator CSV |

---

## Silver layer

Silver creates trusted, cleaned, validated, and GDPR-aware data.

| Object | Grain | Purpose | Key columns | Sensitive fields | Source |
|---|---|---|---|---|---|
| silver_customers | one row per customer | GDPR-aware trusted customer profile | customer_id, customer_hash, email_hash, phone_hash, customer_age, city, bundesland, gdpr_consent | hashed email and phone only | bronze_customers |
| silver_policies | one row per policy | Trusted policy table with customer relationship validation | policy_id, customer_id, policy_type, policy_status, premium_amount, coverage_amount, sales_channel, agent_id | customer_id | bronze_policies + silver_customers |
| silver_claims | one row per claim | Trusted claim table with policy and customer validation | claim_id, policy_id, customer_id, claim_date, claim_type, claim_status, claim_amount | customer_id | bronze_claims + silver_policies + silver_customers |
| silver_payments | one row per valid payment | Trusted payment records after claim/date validation | payment_id, claim_id, payment_date, payment_amount, payment_status, payment_method, iban_hash | iban_hash | bronze_payments + silver_claims |
| silver_agents | one row per agent | Trusted agent dimension | agent_id, agent_name, region, city, bundesland, commission_rate, active_flag | none critical | bronze_agents |
| silver_fraud_indicators | one row per valid claim fraud signal | Trusted fraud indicators after duplicate validation | claim_id, previous_claims_count, risk_score, risk flags | claim_id | bronze_fraud_indicators + silver_claims |

---

## Quarantine layer

Quarantine preserves invalid records with error reasons instead of silently deleting them.

| Object | Grain | Purpose | Main columns | Main error reasons |
|---|---|---|---|---|
| quarantine_invalid_customers | one row per invalid customer record | Preserve invalid customer records | record_id, error_reason, error_severity, original_record_json | none in final small mode |
| quarantine_invalid_policies | one row per invalid policy record | Preserve invalid policy records | record_id, error_reason, error_severity, original_record_json | none in final small mode |
| quarantine_invalid_claims | one row per invalid claim record | Preserve invalid claim records | record_id, error_reason, error_severity, original_record_json | none in final small mode |
| quarantine_invalid_payments | one row per invalid payment record | Preserve invalid payment records | record_id, error_reason, error_severity, original_record_json | payment_before_claim_date |
| quarantine_invalid_fraud_indicators | one row per invalid fraud indicator record | Preserve invalid fraud indicator records | record_id, error_reason, error_severity, original_record_json | duplicate_claim_id |

---

## Gold layer

Gold turns trusted Silver data into business-ready KPIs, analytics outputs, and AI-ready features.

| Object | Grain | Purpose | Key columns | Source |
|---|---|---|---|---|
| gold_claims_overview | claim_month + claim_status + claim_type + policy_type + bundesland | Claims operations KPIs | total_claims, total_claim_amount, average_claim_amount, average_risk_score | silver_claims, silver_policies, silver_customers, silver_fraud_indicators |
| gold_policy_performance | policy_type + policy_status + sales_channel + bundesland | Policy portfolio and premium analytics | total_policies, active_policies, premium_revenue, average_premium, total_coverage | silver_policies, silver_customers, silver_agents |
| gold_customer_risk_profile | one row per customer | Customer-level risk and exposure profile | customer_id, policy_count, claim_count, total_claim_amount, avg_risk_score, gdpr_consent | silver_customers, silver_policies, silver_claims, silver_fraud_indicators |
| gold_claims_payment_summary | one row per claim | Claim-level settlement and payment behavior | claim_id, total_paid_amount, payment_count, payment_delay_days, claim_to_payment_ratio | silver_claims, silver_payments |
| gold_fraud_risk_summary | bundesland + policy_type + claim_type + risk_band | Fraud-risk monitoring summary | total_claims, high_risk_claims, high_risk_rate, average_risk_score, duplicate_claim_count | silver_claims, silver_policies, silver_customers, silver_fraud_indicators |
| gold_agent_performance | one row per agent | Agent and regional performance KPIs | agent_id, premium_revenue, total_claims_linked, claims_ratio, estimated_commission | silver_agents, silver_policies, silver_claims, silver_payments |
| gold_claim_fraud_features | one row per claim | AI-ready fraud feature table | claim_id, claim_amount, premium_amount, coverage_amount, payment_delay_days, risk_score, risk_band | silver_claims, silver_policies, silver_customers, silver_payments, silver_fraud_indicators |

---

## Dashboard views

Dashboard views expose business-friendly, PII-safe outputs for final presentation and BI use.

| View | Grain | Purpose | Main KPIs / fields | Source |
|---|---|---|---|---|
| vw_executive_insurance_overview | one row | Executive KPI overview | total_customers, total_policies, premium_revenue, total_claims, claims_ratio, fraud_risk_rate | Gold KPI tables |
| vw_claims_operations | claim_status + claim_type + policy_type + bundesland | Claims operations analysis | total_claims, total_claim_amount, average_claim_amount, average_risk_score | gold_claims_overview |
| vw_policy_portfolio | policy_type + policy_status + sales_channel + bundesland | Policy portfolio analysis | total_policies, active_policies, premium_revenue, average_premium | gold_policy_performance |
| vw_fraud_risk_monitoring | bundesland + policy_type + claim_type + risk_band | Fraud-risk monitoring | high_risk_claims, high_risk_rate, average_risk_score, duplicate_claim_count | gold_fraud_risk_summary |
| vw_agent_regional_performance | one row per agent | Agent and regional performance analysis | premium_revenue, total_claims_linked, claims_ratio, estimated_commission | gold_agent_performance |
| vw_data_quality_monitoring | one row per dataset | Data quality and quarantine monitoring | quarantine_count | quarantine tables |

---

## PII and sensitive fields

| Field | Classification | Handling |
|---|---|---|
| first_name | direct PII | removed from Silver, Gold, and dashboard views |
| last_name | direct PII | removed from Silver, Gold, and dashboard views |
| email | direct PII | hashed in Silver, not exposed in Gold views |
| phone_number | direct PII | hashed in Silver, not exposed in Gold views |
| street | direct PII | removed from Silver, Gold, and dashboard views |
| postal_code | indirect PII | removed from Silver customer output |
| date_of_birth | indirect PII | transformed into customer_age |
| iban_hash | sensitive financial identifier | retained only as hashed value, not exposed in dashboard views |
| customer_id | operational identifier | used for joins and analytics |
| customer_hash | pseudonymized identifier | used for GDPR-aware analytics |

---

## Final status

The data dictionary covers the main Bronze, Silver, Quarantine, Gold, and dashboard view objects.

Status: PASS