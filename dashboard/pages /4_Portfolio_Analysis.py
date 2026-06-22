import streamlit as st
import pandas as pd
import plotly.express as px

st.title("💼 Portfolio Analysis")

# Load dataset
portfolio = pd.read_csv("data/raw/09_portfolio_holdings.csv")

# ---------------- Top Stocks ----------------
top_weight = (
    portfolio.sort_values("weight_pct", ascending=False)
    .head(10)
)

st.subheader("Top 10 Holdings by Weight")

st.dataframe(
    top_weight[
        ["stock_name", "sector", "weight_pct", "market_value_cr"]
    ]
)

fig1 = px.bar(
    top_weight,
    x="stock_name",
    y="weight_pct",
    color="weight_pct",
    title="Top Holdings by Weight %"
)

fig1.update_layout(xaxis_tickangle=-45)

st.plotly_chart(fig1, use_container_width=True)

# ---------------- Sector Allocation ----------------
sector_weight = (
    portfolio.groupby("sector")["weight_pct"]
    .sum()
    .sort_values(ascending=False)
)

st.subheader("Sector Allocation")

fig2 = px.pie(
    values=sector_weight.values,
    names=sector_weight.index,
    title="Sector Allocation"
)

st.plotly_chart(fig2, use_container_width=True)

# ---------------- Market Value ----------------
top_market = (
    portfolio.groupby("stock_name")["market_value_cr"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.subheader("Top Stocks by Market Value")

fig3 = px.bar(
    x=top_market.index,
    y=top_market.values,
    labels={"x":"Stock","y":"Market Value (Cr)"},
    title="Top Stocks by Market Value"
)

fig3.update_layout(xaxis_tickangle=-45)

st.plotly_chart(fig3, use_container_width=True)
