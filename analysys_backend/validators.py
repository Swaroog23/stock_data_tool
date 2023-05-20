def validate_api_result(stock_data):
    try:
        stock_data["Time Series (Daily)"]
    except KeyError as e:
        print(e)
        return -1