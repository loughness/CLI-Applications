# Currency Converter CLI

A simple command-line tool for converting currencies using real-time exchange rates. This tool fetches live exchange rates from an API and allows users to convert an amount from one currency to another with ease.

## Features

✅ Fetches real-time exchange rates
✅ Converts between different currencies
✅ User-friendly CLI interface
✅ Error handling for invalid currencies and API failures
✅ Logs the last exchange rate refresh time

## Installation

1. **Clone the repository**:

   ```sh
   git clone https://github.com/loughness/currency_converter_cli.git
   cd currency_converter_cli
   ```

2. **Create a virtual environment (optional but recommended):**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Set up your API key:**
   - Create a `.env` file in the `src` folder.
   - Add the following line to the `.env` file:
     ```
     API_KEY=your_api_key_here
     ```
   - Replace `your_api_key_here` with your actual API key from [ExchangeRate-API](https://www.exchangerate-api.com/).
   - Ensure that your `.env` file is listed in `.gitignore` to prevent exposing sensitive information.
   - A sample `.env.example` file is included to show how to format your environment file.

## Usage

### Convert Currency

Run the script using the following command:

```sh
python src/exchange_cli.py USD EUR 100
```

This converts **100 USD to EUR** using real-time exchange rates.

### Example Output

```
══════════════════════════════════════
🎯 Currency Conversion Result
══════════════════════════════════════

───────────────────────────────────────
🌍 Currency Conversion Report
───────────────────────────────────────
🏦 Conversion: 100.00 USD → EUR
💰 Converted Amount: 92.45 EUR
🔄 Exchange Rate: 1 USD = 0.9245 EUR
📅 Last Refreshed: 2025-02-08 14:30:15
───────────────────────────────────────

══════════════════════════════════════
```

### Get Help

To see usage instructions, run:

```sh
python src/exchange_cli.py --help
```

## Notes

- **Make sure your `.env` file is ignored in `.gitignore`** to prevent exposing your API key.
- A `.env.example` file is included to show how environment variables should be formatted.
- The API has rate limits on free-tier plans; check their documentation for details.

## Contributing

Feel free to fork the repository and submit a pull request if you’d like to improve the project!

## License

This project is licensed under the MIT License.

---

📌 **Thank you for using the Currency Converter CLI!** 🚀
