import pandas as pd

# Load transaction data
df = pd.read_csv("data/raw/08_investor_transactions.csv")

# Convert transaction date
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

# Remove duplicates
df = df.drop_duplicates()

# Keep positive transaction amounts
df = df[df["amount_inr"] > 0]

# Standardize transaction type
df["transaction_type"] = df["transaction_type"].str.strip()

# Save cleaned file
df.to_csv(
    "data/processed/clean_transactions.csv",
    index=False
)

print("Transactions cleaned successfully!")