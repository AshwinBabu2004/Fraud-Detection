import pandas as pd

# Load data
df = pd.read_csv("data/creditcard.csv")

# Add hour column
df["Hour"] = (df["Time"] / 3600 % 24).astype(int)

# Score based on amount (higher or very low = riskier)
def amount_score(amount):
    if amount > 500:
        return 3
    elif amount > 200:
        return 2
    elif amount < 10:
        return 1
    else:
        return 0

df["Score_Amount"] = df["Amount"].apply(amount_score)
print(df["Score_Amount"].value_counts().sort_index())
# Score based on hour (2-5 AM = high risk)
def hour_score(hour):
    if hour in [2, 3, 4, 5]:
        return 3
    elif hour in [0, 1, 6]:
        return 1
    else:
        return 0

df["Score_Hour"] = df["Hour"].apply(hour_score)
print(df["Score_Hour"].value_counts().sort_index())
# Add scores together
df["Risk_Score"] = df["Score_Amount"] + df["Score_Hour"]

# Assign risk tier based on total score
def risk_tier(score):
    if score >= 5:
        return "Critical"
    elif score >= 3:
        return "High"
    elif score >= 1:
        return "Medium"
    else:
        return "Low"

df["Risk_Tier"] = df["Risk_Score"].apply(risk_tier)

print("\nRisk Tier Breakdown:")
print(df["Risk_Tier"].value_counts())

# Save scored dataset
df.to_csv("output/transactions_scored.csv", index=False)
print("\nSaved: output/transactions_scored.csv")

