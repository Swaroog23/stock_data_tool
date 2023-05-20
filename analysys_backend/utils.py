import requests


def fetch_time_series_daily_stock_data(stock_symbol, full_output=False):
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

def transform_api_stock_data(stock_data, api_function):
    _, time_series_data_key = stock_data
    time_series_data = stock_data[time_series_data_key]
    volume = None
    if api_function == "TIME_SERIES_INTRADAY":
        volume = "5. volume"
    else:
        volume = "6. volume"
    time_series_data = [
        {
            "date": date,
            "open": float(values["1. open"]),
            "high": float(values["2. high"]),
            "low": float(values["3. low"]),
            "close": float(values["4. close"]),
            "volume": int(values[volume]) 
        }
        for date, values in time_series_data.items()
    ]

    return time_series_data

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

def fetch_time_series_intraday_stock_data(stock_symbol, interval, full_output=False):
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": f"{stock_symbol}",
        "interval": f"{interval}",
        "outputsize": "full" if full_output else "compact",
        "apikey": "NA9LMVVVZNFJOHL1"
    }

    response = requests.get(url, params=params)
    data = response.json()
    
    return data
