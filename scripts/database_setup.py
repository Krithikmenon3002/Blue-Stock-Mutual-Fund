import pandas as pd
import sqlite3
from pathlib import Path

# Create database connection
db_path = Path("data/db")
db_path.mkdir(parents=True, exist_ok=True)

conn = sqlite3.connect(db_path / "mutual_fund.db")

# Folder containing CSV files
data_folder = Path("data/raw")

# Load all CSV files into SQLite
for file in data_folder.glob("*.csv"):
    try:
        df = pd.read_csv(file)

        table_name = file.stem

        df.to_sql(
            table_name,
            conn,
            if_exists="replace",
            index=False
        )

        print(f"{table_name} loaded successfully")

    except Exception as e:
        print(f"Error loading {file.name}: {e}")

conn.close()

print("Database created successfully!")
