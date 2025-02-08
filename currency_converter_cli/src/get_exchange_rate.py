import requests
import datetime
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")

def last_refresh():
    """Returns the current timestamp for when the rates were last fetched."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/EUR"

def get_exchange_rates():
    """Fetches exchange rates from the API."""
    try:
        response = requests.get(url)
        data = response.json()
        return data["conversion_rates"]
    except Exception as e:
        print(f"\n❌ An error occurred while fetching exchange rates: {e}\n")
        return None

def convert_currency(amount, currency_from, currency_to, rates):
    """Converts an amount from one currency to another using exchange rates."""
    if currency_from not in rates or currency_to not in rates:
        return f"\n⚠️ Error: One or both currency codes are invalid ({currency_from} → {currency_to}). Please check and try again.\n"

    converted = amount * (rates[currency_to] / rates[currency_from])

    output = "─" * 40 + "\n"
    output += "🌍 Currency Conversion Report\n"
    output += "─" * 40 + "\n"
    output += f"🏦 Conversion: {amount:,.2f} {currency_from} → {currency_to}\n"
    output += f"💰 Converted Amount: {converted:,.2f} {currency_to}\n"
    output += f"🔄 Exchange Rate: 1 {currency_from} = {rates[currency_to] / rates[currency_from]:.4f} {currency_to}\n"
    output += f"📅 Last Refreshed: {last_refresh()}\n"
    output += "─" * 40 + "\n"

    return output