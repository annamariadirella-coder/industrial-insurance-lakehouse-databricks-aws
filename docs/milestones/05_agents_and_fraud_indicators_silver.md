# Milestone 5 — Agents and Fraud Indicators Silver

## Goal

Create:

```text
silver_agents
silver_fraud_indicators
```

## Agents

- validate `agent_id`
- deduplicate by `agent_id`
- standardize city and Bundesland
- cast commission rate
- validate active flag

## Fraud indicators

- validate `claim_id`
- validate claim exists in `silver_claims`
- cast previous claim count
- validate boolean flags
- validate `risk_score` between 0 and 100
- deduplicate by `claim_id`
