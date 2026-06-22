import streamlit as st
import pandas as pd

st.title("📈 Live NAV")

# Load data
nav = pd.read_csv("data/raw/02_nav_history.csv")

# Select AMFI code
codes = nav["amfi_code"].unique()

selected_code = st.selectbox(
    "Select AMFI Code",
    codes
)

# Filter data
fund_data = nav[nav["amfi_code"] == selected_code]

# Latest NAV
latest = fund_data.sort_values("date").iloc[-1]

st.subheader("Latest NAV")
st.write("AMFI Code:", selected_code)
st.write("NAV:", latest["nav"])
st.write("Date:", latest["date"])

# NAV history chart
st.subheader("NAV History")

st.line_chart(
    fund_data.set_index("date")["nav"]
)

# Table
st.subheader("Data")

st.dataframe(
    fund_data.sort_values("date", ascending=False)
)