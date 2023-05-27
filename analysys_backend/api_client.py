import requests

from consts.api_client_consts import API_KEY, BASE_URL


def fetch_data(params: dict, url: str = BASE_URL):
    response = requests.get(url, params=params)
    data = response.json()
    return data


def fetch_time_series_daily_stock_data(stock_symbol: str, full_output: bool = False):
    params = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": stock_symbol,
        "outputsize": "full" if full_output else "compact",
        "apikey": API_KEY
    }
    return fetch_data(params)


def fetch_time_series_intraday_stock_data(stock_symbol: str, interval: int, full_output: bool = False):
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": stock_symbol,
        "interval": str(interval),
        "outputsize": "full" if full_output else "compact",
        "apikey": API_KEY
    }
    return fetch_data(params)


def fetch_company_data(search_query: str):
    params = {
        "function": "SYMBOL_SEARCH",
        "keywords": search_query,
        "apikey": API_KEY
    }
    return fetch_data(params)
