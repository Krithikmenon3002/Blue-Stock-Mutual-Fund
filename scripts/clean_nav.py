import pandas as pd

# Load NAV history data
nav = pd.read_csv("data/raw/02_nav_history.csv")

# Convert date column to datetime
nav["date"] = pd.to_datetime(nav["date"])

# Sort values
nav = nav.sort_values(["amfi_code", "date"])

# Remove duplicates
nav = nav.drop_duplicates()

# Forward fill missing NAV values
nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()

# Keep only positive NAV values
nav = nav[nav["nav"] > 0]

# Save cleaned data
nav.to_csv("data/processed/clean_nav.csv", index=False)

print("NAV cleaned successfully!")