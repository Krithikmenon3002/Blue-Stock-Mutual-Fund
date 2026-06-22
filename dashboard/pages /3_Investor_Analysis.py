import streamlit as st
import pandas as pd
import plotly.express as px

st.title("👥 Investor Analysis")

# Load dataset
investor = pd.read_csv("data/raw/08_investor_transactions.csv")

# ---------------- Gender Distribution ----------------
gender_count = investor["gender"].value_counts()

st.subheader("Gender Distribution")

fig1 = px.pie(
    values=gender_count.values,
    names=gender_count.index,
    title="Investor Gender Distribution"
)

st.plotly_chart(fig1, use_container_width=True)

# ---------------- Transaction Types ----------------
transaction_count = investor["transaction_type"].value_counts()

st.subheader("Transaction Types")

fig2 = px.bar(
    x=transaction_count.index,
    y=transaction_count.values,
    labels={"x":"Transaction Type","y":"Count"},
    title="Transaction Types"
)

st.plotly_chart(fig2, use_container_width=True)

# ---------------- Payment Modes ----------------
payment_count = investor["payment_mode"].value_counts()

st.subheader("Payment Modes")

fig3 = px.bar(
    x=payment_count.index,
    y=payment_count.values,
    labels={"x":"Payment Mode","y":"Count"},
    title="Payment Modes"
)

st.plotly_chart(fig3, use_container_width=True)

# ---------------- Top States ----------------
state_amount = (
    investor.groupby("state")["amount_inr"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.subheader("Top States by Investment Amount")

fig4 = px.bar(
    x=state_amount.index,
    y=state_amount.values,
    labels={"x":"State","y":"Investment Amount"},
    title="Top 10 States"
)

st.plotly_chart(fig4, use_container_width=True)