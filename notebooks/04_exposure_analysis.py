import pandas as pd
import sqlite3

# Load scored dataset
df = pd.read_csv("output/transactions_scored.csv")

# Create an in-memory SQLite database and load the data into it
conn = sqlite3.connect(":memory:")
df.to_sql("transactions", conn, index=False, if_exists="replace")

print("Database ready.")
print(f"Loaded {len(df):,} transactions into SQL table.")
# Query 1: Total exposure and fraud count per risk tier
query1 = """
SELECT
    Risk_Tier,
    COUNT(*) AS total_transactions,
    SUM(Class) AS fraud_count,
    ROUND(SUM(Amount), 2) AS total_exposure,
    ROUND(AVG(Amount), 2) AS avg_amount,
    ROUND(100.0 * SUM(Class) / COUNT(*), 3) AS fraud_rate_pct
FROM transactions
GROUP BY Risk_Tier
ORDER BY total_exposure DESC;
"""

result1 = pd.read_sql(query1, conn)
print("\nExposure by Risk Tier:")
print(result1.to_string(index=False))
# Query 2: Share of total fraud per tier
query2 = """
SELECT
    Risk_Tier,
    SUM(Class) AS fraud_count,
    ROUND(100.0 * SUM(Class) / (SELECT SUM(Class) FROM transactions), 1) AS pct_of_all_fraud
FROM transactions
GROUP BY Risk_Tier
ORDER BY fraud_count DESC;
"""

result2 = pd.read_sql(query2, conn)
print("\nShare of Total Fraud by Tier:")
print(result2.to_string(index=False))
# Save SQL results
result1.to_csv("output/sql_exposure_by_tier.csv", index=False)
result2.to_csv("output/sql_fraud_share_by_tier.csv", index=False)

print("\nSaved:")
print("  output/sql_exposure_by_tier.csv")
print("  output/sql_fraud_share_by_tier.csv")

conn.close()
