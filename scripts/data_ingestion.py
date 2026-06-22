import pandas as pd
from pathlib import Path

data_folder = Path("data/raw")

csv_files = list(data_folder.glob("*.csv"))

if not csv_files:
    print("No CSV files found in data/raw")
else:
    for file in csv_files:
        print("\n" + "=" * 60)

        try:
            df = pd.read_csv(file)

            print(f"File Name : {file.name}")
            print(f"Shape     : {df.shape}")

            print("\nData Types:")
            print(df.dtypes)

            print("\nFirst 5 Rows:")
            print(df.head())

        except Exception as e:
            print(f"Error reading {file.name}: {e}")
            