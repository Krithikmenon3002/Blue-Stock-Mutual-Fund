import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🏦 Fund House Analysis")

# Load dataset
aum = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

# Top 10 fund houses by AUM
top_aum = (
    aum.groupby("fund_house")["aum_crore"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

# Show table
st.subheader("Top 10 Fund Houses by AUM")
st.dataframe(top_aum)

# Plot
fig = px.bar(
    top_aum,
    x="fund_house",
    y="aum_crore",
    title="Top 10 Fund Houses by AUM",
    color="aum_crore"
)

fig.update_layout(xaxis_tickangle=-45)

st.plotly_chart(fig, use_container_width=True)
