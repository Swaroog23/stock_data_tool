def validate_api_result(stock_data):
    if "Error Message" in stock_data:
        return -1
    return 0
