import numpy as np
import requests

from consts.api_client_consts import API_KEY, BASE_URL


def get_data_set(symbol: str):
    params = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": f"{symbol}",
        "outputsize": "full",
        "apikey": API_KEY
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    time_series_data = data["Time Series (Daily)"]
    stock_data = [
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

    return stock_data

def prepare_feature(data: list):
    features = np.array([[
        data_point["open"],
        data_point["close"],
        data_point["high"],
        data_point["low"],
        data_point["volume"]
    ] for data_point in data])

    return features

def prepare_target(data: list):
    target = np.array([data_point["close"] for data_point in data])

    return target
