from fastapi import HTTPException

from utils import fetch_company_data, fetch_time_series_daily_stock_data, fetch_time_series_intraday_stock_data, transform_api_stock_data
from validators import validate_api_result


def retrive_and_transform_stock_data(stock_symbol:str, is_full:bool, api_function:str, interval=None):
    api_result = None
    stock_symbol = stock_symbol.upper()
    if api_function == "TIME_SERIES_DAILY_ADJUSTED":
        api_result = fetch_time_series_daily_stock_data(stock_symbol, is_full)
    elif api_function == "TIME_SERIES_INTRADAY":
        interval = f"{interval}min" if interval else "60min"
        print(interval)
        api_result = fetch_time_series_intraday_stock_data(stock_symbol, interval, is_full)
    if validate_api_result(api_result) == -1:
        raise HTTPException(status_code=404, detail="Item not found")
    transformed_data = transform_api_stock_data(api_result, api_function)
    
    return {"symbol": stock_symbol, "data": transformed_data}

def retrive_company_data(search_query:str):
    api_result = fetch_company_data(search_query)
    if validate_api_result(api_result) == -1:
        raise HTTPException(status_code=404, detail="Item not found")
    return api_result
