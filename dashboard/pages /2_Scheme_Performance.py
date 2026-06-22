import streamlit as st
import pandas as pd
import plotly.express as px

st.title("⭐ Scheme Performance")

# Load dataset
scheme = pd.read_csv("data/raw/07_scheme_performance.csv")

# Top 10 schemes by 5-year return
top_scheme = (
    scheme.sort_values("return_5yr_pct", ascending=False)
    .head(10)
)

# Table
st.subheader("Top 10 Schemes by 5-Year Return")

st.dataframe(
    top_scheme[
        ["scheme_name",
         "fund_house",
         "return_5yr_pct",
         "morningstar_rating",
         "risk_grade"]
    ]
)

# Chart
fig = px.bar(
    top_scheme,
    x="scheme_name",
    y="return_5yr_pct",
    color="return_5yr_pct",
    title="Top 10 Schemes by 5-Year Return"
)

fig.update_layout(
    xaxis_tickangle=-45
)

st.plotly_chart(fig, use_container_width=True)