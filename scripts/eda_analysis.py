import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
aum = pd.read_csv("data/raw/03_aum_by_fund_house.csv")
sip = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")
print(sip.columns)
category = pd.read_csv("data/raw/05_category_inflows.csv")
print(category.columns)
scheme = pd.read_csv("data/raw/07_scheme_performance.csv")

# ----------------------------
# Top Fund Houses by AUM
# ----------------------------
top_aum = (
    aum.groupby("fund_house")["aum_crore"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_aum)

plt.figure(figsize=(10,5))
top_aum.plot(kind="bar")
plt.title("Top 10 Fund Houses by AUM")
plt.ylabel("AUM (Crore)")
plt.xticks(rotation=45)
plt.show()

# ----------------------------
# Monthly SIP Inflows Trend
# ----------------------------
# ----------------------------
# Monthly SIP Inflows Trend
# ----------------------------
plt.figure(figsize=(10,5))
plt.plot(sip["month"], sip["sip_inflow_crore"])
plt.xticks(rotation=45)
plt.title("Monthly SIP Inflows")
plt.ylabel("SIP Inflow (Crore)")
plt.xlabel("Month")
plt.tight_layout()
plt.show()

# ----------------------------
# Category Inflows
# ----------------------------
top_category = (
    category.groupby("category")["net_inflow_crore"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10,5))
top_category.plot(kind="bar")
plt.title("Category-wise Inflows")
plt.ylabel("Inflow (Crore)")
plt.xticks(rotation=45)
plt.show()

