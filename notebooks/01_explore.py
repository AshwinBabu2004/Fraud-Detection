import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

# Load the dataset
print("Loading data...")
df = pd.read_csv("data/creditcard.csv")

print(f"Shape: {df.shape[0]:,} rows, {df.shape[1]} columns")
# Check for missing values

print(f"\nMissing values: {df.isnull().sum().sum()} total")

# Fraud vs normal breakdown
fraud_counts = df["Class"].value_counts()
fraud_pct = df["Class"].value_counts(normalize=True) * 100

print(f"\nTransaction Breakdown:")
print(f"  Normal (0): {fraud_counts[0]:,}  ({fraud_pct[0]:.2f}%)")
print(f"  Fraud  (1): {fraud_counts[1]:,}  ({fraud_pct[1]:.2f}%)")
# Amount stats by class

print(f"\nTransaction Amount by Class:")

print(df.groupby("Class")["Amount"].describe().round(2))

# Bar chart: fraud vs normal count

plt.figure(figsize=(6, 4))
sns.countplot(x="Class", data=df, palette=["steelblue", "crimson"])
plt.xticks([0, 1], ["Normal", "Fraud"])
plt.title("Fraud vs Normal Transactions")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("output/01_fraud_vs_normal.png")
print("Chart saved to output/01_fraud_vs_normal.png")

# Histogram: transaction amount by class
plt.figure(figsize=(8, 4))
df[df["Class"] == 0]["Amount"].clip(upper=500).hist(
    bins=50, alpha=0.6, label="Normal", color="steelblue"
)
df[df["Class"] == 1]["Amount"].clip(upper=500).hist(
    bins=50, alpha=0.7, label="Fraud", color="crimson"
)
plt.xlabel("Transaction Amount (capped at $500)")
plt.ylabel("Count")
plt.title("Transaction Amount Distribution")
plt.legend()
plt.tight_layout()
plt.savefig("output/02_amount_distribution.png")
print("Chart saved to output/02_amount_distribution.png")
