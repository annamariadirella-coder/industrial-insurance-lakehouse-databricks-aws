SELECT SUM(total_policies) AS total_policies, SUM(active_policies) AS active_policies, ROUND(SUM(premium_revenue), 2) AS premium_revenue FROM insurance_lakehouse.gold.gold_policy_performance;
