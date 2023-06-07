def transform_api_stock_data(stock_data, api_function):
    _, time_series_data_key = stock_data
    time_series_data = stock_data[time_series_data_key]
    
    volume_key = "5. volume" if api_function == "TIME_SERIES_INTRADAY" else "6. volume"
    
    transformed_data = [
        {
            "date": date,
            "open": float(values["1. open"]),
            "high": float(values["2. high"]),
            "low": float(values["3. low"]),
            "close": float(values["4. close"]),
            "volume": int(values[volume_key])
        }
        for date, values in time_series_data.items()
    ]

    return transformed_data