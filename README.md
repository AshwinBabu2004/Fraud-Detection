# Financial Fraud Detection & Risk Scoring

Analyzed 284,807 real credit card transactions to detect fraud patterns, build a risk scoring model, and quantify financial exposure per risk tier.

## Key Findings

- **Fraud rate:** 0.17% (492 out of 284,807 transactions)
- **Peak fraud hours:** 2–5 AM — fraud rate at 2 AM is 1.71%, over 10x the average
- **Highest fraud rate by amount:** Transactions over $500 have the highest fraud rate (0.38%)
- **Risk tier exposure:**
  - Critical tier: 1.072% fraud rate — highest risk
  - High tier: $9.9M total exposure — largest dollar risk
  - 45.7% of all fraud hides in the Medium tier — fraudsters use mid-range amounts to avoid detection

## Tools Used

- **Python** — data cleaning, fraud pattern analysis, risk scoring (pandas, matplotlib, seaborn)
- **SQL (SQLite)** — financial exposure queries per risk tier
- **Tableau Public** — interactive dashboard (coming soon)

## Project Structure

```
fraud-detection/
├── notebooks/
│   ├── 01_explore.py           # Data loading, missing value check, class distribution
│   ├── 02_fraud_patterns.py    # Fraud rate by amount bucket and hour of day
│   ├── 03_risk_scoring.py      # Risk score and tier assignment for all transactions
│   └── 04_exposure_analysis.py # SQL queries: exposure and fraud share per tier
├── output/
│   ├── 01_fraud_vs_normal.png
│   ├── 02_amount_distribution.png
│   ├── fraud_by_amount_bucket.csv
│   ├── fraud_by_hour.csv
│   ├── sql_exposure_by_tier.csv
│   └── sql_fraud_share_by_tier.csv
└── .gitignore
```

## Dataset

Credit Card Fraud Detection — ULB Machine Learning Group (Kaggle)
284,807 transactions with 28 anonymized features, transaction amount, and fraud label.
