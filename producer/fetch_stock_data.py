import requests
from config.config import FINNHUB_API_KEY, FINNHUB_BASE_URL

def get_stock_price(symbol):
    url = f"{FINNHUB_BASE_URL}/quote"
    params = {
        "symbol": symbol,
        "token": FINNHUB_API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    # Finnhub returns empty dict if limit exceeded
    if "c" not in data:
        return None

    return {
        "symbol": symbol,
        "price": data["c"],   # current price
        "high": data["h"],
        "low": data["l"],
        "open": data["o"],
        "prev_close": data["pc"]
    }
