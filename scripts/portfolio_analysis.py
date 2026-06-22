import pandas as pd
import matplotlib.pyplot as plt

portfolio = pd.read_csv("data/raw/09_portfolio_holdings.csv")

print(portfolio.columns)

top_stocks = (
    portfolio.sort_values("market_value_cr", ascending=False)
    .head(10)
)

print(top_stocks[["stock_name", "market_value_cr"]])

plt.figure(figsize=(10,5))
plt.bar(top_stocks["stock_name"], top_stocks["market_value_cr"])
plt.xticks(rotation=45)
plt.ylabel("Market Value (Cr)")
plt.title("Top 10 Holdings")
plt.tight_layout()
plt.show()

sector_alloc = (
    portfolio.groupby("sector")["market_value_cr"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(sector_alloc)

plt.figure(figsize=(8,8))
sector_alloc.plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Sector Allocation")
plt.show()

top_weight = (
    portfolio.sort_values("weight_pct", ascending=False)
    .head(10)
)

print(top_weight[["stock_name","weight_pct"]])

plt.figure(figsize=(10,5))
plt.bar(top_weight["stock_name"], top_weight["weight_pct"])
plt.xticks(rotation=45)
plt.ylabel("Weight %")
plt.title("Top Portfolio Weights")
plt.tight_layout()
plt.show()