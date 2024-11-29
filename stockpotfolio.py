import requests

# Constants
API_KEY = 'your_alpha_vantage_api_key'  # Replace with your actual API key
BASE_URL = 'https://www.alphavantage.co/query'

# Portfolio dictionary to store stocks and their information
portfolio = {}

def add_stock(symbol, quantity):
    """Adds a stock to the portfolio with the given quantity."""
    if symbol in portfolio:
        portfolio[symbol]['quantity'] += quantity
    else:
        portfolio[symbol] = {'quantity': quantity}
    print(f"Added {quantity} shares of {symbol} to portfolio.")

def remove_stock(symbol):
    """Removes a stock from the portfolio."""
    if symbol in portfolio:
        del portfolio[symbol]
        print(f"Removed {symbol} from portfolio.")
    else:
        print(f"{symbol} not found in portfolio.")

def fetch_stock_price(symbol):
    """Fetches the current stock price using the Alpha Vantage API."""
    try:
        params = {
            'function': 'TIME_SERIES_INTRADAY',
            'symbol': symbol,
            'interval': '5min',
            'apikey': API_KEY
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        # Extract the latest closing price
        latest_time = list(data['Time Series (5min)'])[0]
        price = float(data['Time Series (5min)'][latest_time]['4. close'])
        return price
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None

def view_portfolio():
    """Displays the portfolio with current stock prices and total value."""
    total_value = 0.0
    print("\nPortfolio:")
    for symbol, info in portfolio.items():
        quantity = info['quantity']
        price = fetch_stock_price(symbol)
        if price is not None:
            stock_value = price * quantity
            total_value += stock_value
            print(f"{symbol}: {quantity} shares @ ${price:.2f} each, Value: ${stock_value:.2f}")
    print(f"Total Portfolio Value: ${total_value:.2f}")

# Example Usage
add_stock("AAPL", 10)
add_stock("GOOGL", 5)
view_portfolio()
remove_stock("AAPL")
view_portfolio()
