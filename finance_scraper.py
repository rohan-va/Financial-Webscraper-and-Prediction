# imports - data and dates
import yfinance as yf
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

# Retrieving today's date
todayDate = datetime.today().strftime("%Y-%m-%d")
folderPath = os.getenv("FOLDER_PATH")

# check if loading/correct path (machine specfic)
if folderPath:
    print(f"Data will be saved to: {folderPath}")
else:
    print("Error: Could not find FOLDER_PATH in environment variables.")


# Function defining to saving of stock data
def save_stock_data(ticker, nameFile):
    # Start date for data
    data = yf.download([ticker], start="2024-01-01")
    # Applies 'Date' as column for prediction.py
    data.reset_index(inplace=True)
    filename = f"{nameFile}.{todayDate}.csv"
    full_path = f"{folderPath}/{filename}"
    data.to_csv(full_path, index=False)
    print(f"Saved {full_path}")


# List of stock ticker and name
stocks = {
    "AAPL": "Apple",
    "MSFT": "Microsoft",
    "ABNB": "Airbnb",
    "AMZN": "Amazon",
    "GOOGL": "Google",
    "META": "Meta",
    "TGT": "Target",
    "WMT": "Walmart",
    "NVDA": "NVIDIA-Corp",
    "PLTR": "Palantir-Technologies-Inc",
    "JPM": "JPMorgan-Chase-&-Co",
    "NKE": "Nike-Inc",
    "COST": "Costco",
    "AVGO": "Broadcom",
    "2222.SR": "Saudi-Aramco",
    "TSM": "Taiwan-Semiconducter-Manufacturing",
    "MCD": "McDonald's-Corporation",
    "BTC-USD": "Bitcoin-USD",
    "NFLX": "Netflix",
    "F": "Ford-Motor-Company",
    "HMC": "Honda-Motor-Company",
    "DELL": "Dell-Technologies-Inc.",
    "CVS": "CVS-Health-Corporation",
    "W": "Wayfair-Inc.",
    "AAL": "American-Airlines-Group-Inc.",
    "UPS": "United-Parcel-Service",
    # More to come
}

# Loop through each stock, saving ticker and name listed above
for ticker, name in stocks.items():
    save_stock_data(ticker, name)
