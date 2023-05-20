import requests


def fetch_stock_data(stock_symbol, full_output=False):
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": f"{stock_symbol}",
        "outputsize": "full" if full_output else "compact",
        "apikey": "NA9LMVVVZNFJOHL1"
    }

    response = requests.get(url, params=params)
    data = response.json()
    
    return data

def transform_api_stock_data(stock_data):
    time_series_data = stock_data["Time Series (Daily)"]
    
    data = [
        {
            "date": date,
            "open": float(values["1. open"]),
            "high": float(values["2. high"]),
            "low": float(values["3. low"]),
            "close": float(values["4. close"]),
            "volume": int(values["6. volume"])
        }
        for date, values in time_series_data.items()
    ]

    return data

def fetch_company_data(search_query):
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "SYMBOL_SEARCH",
        "keywords": f"{search_query}",
        "apikey": "NA9LMVVVZNFJOHL1"
    }

    response = requests.get(url, params=params)
    data = response.json()
    return data
