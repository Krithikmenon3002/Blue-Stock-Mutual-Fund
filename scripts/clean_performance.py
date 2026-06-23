import pandas as pd

# Load scheme performance data
df = pd.read_csv("data/raw/07_scheme_performance.csv")

# Remove duplicates
df = df.drop_duplicates()

# Convert return columns to numeric
cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Remove rows with missing returns
df = df.dropna(subset=cols)

# Save cleaned file
df.to_csv(
    "data/processed/clean_performance.csv",
    index=False
)

print("Performance cleaned successfully!")