import pandas as pd

investor = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

print(investor.columns)

import matplotlib.pyplot as plt

top_states = (
    investor.groupby("state")["amount_inr"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_states)

plt.figure(figsize=(10,5))
top_states.plot(kind="bar")
plt.title("Top 10 States by Investment Amount")
plt.ylabel("Amount (INR)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print(investor["transaction_type"].value_counts())

trans = investor["transaction_type"].value_counts()

plt.figure(figsize=(6,6))
trans.plot(kind="pie", autopct='%1.1f%%')
plt.ylabel("")
plt.title("Transaction Type Distribution")
plt.show()

print(investor["gender"].value_counts())

gender = investor["gender"].value_counts()

plt.figure(figsize=(6,6))
gender.plot(kind="pie", autopct='%1.1f%%')
plt.ylabel("")
plt.title("Gender Distribution")
plt.show()

age = investor["age_group"].value_counts()

plt.figure(figsize=(8,5))
age.plot(kind="bar")
plt.title("Age Group Distribution")
plt.ylabel("Number of Investors")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

payment = investor["payment_mode"].value_counts()

plt.figure(figsize=(8,5))
payment.plot(kind="bar")
plt.title("Payment Modes")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()