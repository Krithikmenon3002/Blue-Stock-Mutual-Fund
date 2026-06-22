import pandas as pd
import matplotlib.pyplot as plt

scheme = pd.read_csv("data/raw/07_scheme_performance.csv")

print(scheme.columns)
print(scheme.columns)
top_scheme = (
    scheme.sort_values("return_5yr_pct", ascending=False)
    .head(10)
)

print(top_scheme[["scheme_name", "return_5yr_pct"]])
print(top_scheme[["scheme_name", "return_5yr_pct"]])
plt.figure(figsize=(12,6))

plt.bar(
    top_scheme["scheme_name"],
    top_scheme["return_5yr_pct"]
)

plt.title("Top 10 Schemes by 5-Year Return")
plt.ylabel("Return (%)")
plt.xticks(rotation=90)

plt.tight_layout()
plt.show()

plt.figure(figsize=(8,6))

plt.scatter(
    scheme["beta"],
    scheme["return_5yr_pct"]
)

plt.xlabel("Beta")
plt.ylabel("5-Year Return (%)")
plt.title("Risk vs Return")

plt.show()