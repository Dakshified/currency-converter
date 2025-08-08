import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.exchangerate.host/convert"

print("💱 Currency Converter")
from_currency = input("From Currency (e.g., USD): ").upper()
to_currency = input("To Currency (e.g., INR): ").upper()
amount = float(input("Amount: "))

params = {
    "from": from_currency,
    "to": to_currency,
    "amount": amount,
    "access_key": API_KEY
}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()
    if data.get("result") is not None:
        print(f"\n✅ {amount} {from_currency} = {round(data['result'], 2)} {to_currency}")
    else:
        print("\n❌ Conversion failed. Check currency codes.")
else:
    print("\n❌ Error fetching data.")
