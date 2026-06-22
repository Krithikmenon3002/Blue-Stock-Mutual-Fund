import sqlite3
import pandas as pd

conn = sqlite3.connect("data/db/mutual_fund.db")

# Example query
query = """
SELECT * FROM "01_fund_master"
LIMIT 5
"""

df = pd.read_sql(query, conn)

print(df)

conn.close()