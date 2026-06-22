import requests
import pandas as pd
from pathlib import Path

scheme_code = "125497"

url = f"https://api.mfapi.in/mf/{scheme_code}"

response = requests.get(url)

if response.status_code == 200:

	data = response.json()

	nav_df = pd.DataFrame(data["data"])

	output_folder = Path("data/raw")
	output_folder.mkdir(parents=True, exist_ok=True)

	nav_df.to_csv(
		output_folder / "hdfc_top100_nav.csv",
		index=False
	)

	print("NAV data saved successfully")

else:
	print("API request failed")

