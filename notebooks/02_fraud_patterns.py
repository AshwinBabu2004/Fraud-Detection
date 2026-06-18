import pandas as pd

# Load data
df = pd.read_csv("data/creditcard.csv")

# Create amount buckets
df["Amount_Bucket"] = pd.cut(
    df["Amount"],
    bins=[0, 10, 50, 200, 500, 25000],
    labels=["$0-10", "$10-50", "$50-200", "$200-500", "$500+"]
)

print(df["Amount_Bucket"].value_counts().sort_index())
# Fraud rate per amount bucket
bucket_stats = df.groupby("Amount_Bucket", observed=True).agg(
    total=("Class", "count"),
    fraud=("Class", "sum")
)
bucket_stats["fraud_rate"] = (bucket_stats["fraud"] / bucket_stats["total"] * 100).round(2)

print("\nFraud Rate by Amount Bucket:")
print(bucket_stats)
# Convert Time (seconds) to hour of day
df["Hour"] = (df["Time"] / 3600 % 24).astype(int)

hourly = df.groupby("Hour").agg(
    total=("Class", "count"),
    fraud=("Class", "sum")
)
hourly["fraud_rate"] = (hourly["fraud"] / hourly["total"] * 100).round(2)

print("\nTop 5 Highest Fraud Hours:")
print(hourly.sort_values("fraud_rate", ascending=False).head())
# Save pattern data to output folder
bucket_stats.to_csv("output/fraud_by_amount_bucket.csv")
hourly.to_csv("output/fraud_by_hour.csv")

print("\nSaved:")
print("  output/fraud_by_amount_bucket.csv")
print("  output/fraud_by_hour.csv")


