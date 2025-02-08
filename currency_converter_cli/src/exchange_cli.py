import argparse
from get_exchange_rate import get_exchange_rates, convert_currency

parser = argparse.ArgumentParser(
    prog="Currency Converter",
    description="""
    🌍 Currency Converter CLI
    ---------------------------------
    A simple tool to check exchange rates and convert between currencies.
    Example usage:
        python currency_converter.py USD EUR 100
    """,
    epilog="📌 Thank you for using Currency Converter!",
    allow_abbrev=True,
)

parser.add_argument(
    "currency1",
    metavar="(EUR, USD, GBP, ...)",
    type=str,
    help="💱 Enter the currency you are converting from (e.g., USD).",
)

parser.add_argument(
    "currency2",
    metavar="(USD, EUR, GBP, ...)",
    type=str,
    help="🔄 Enter the currency you are converting to (e.g., EUR).",
)

parser.add_argument(
    "value",
    nargs="?",
    default=1.0,
    action="store",
    metavar="100",
    type=float,
    help="💰 *Optional | Enter the amount to convert | Default: 1",
)

args = parser.parse_args()

exchange_rates = get_exchange_rates()

converted_amount = convert_currency(
    amount=args.value,
    currency_from=args.currency1.upper(),
    currency_to=args.currency2.upper(),
    rates=exchange_rates,
)

print("\n" + "*" * 40)
print("🎯 Currency Conversion Result")
print("*" * 40)
print(converted_amount)
print("*" * 40 + "\n")
