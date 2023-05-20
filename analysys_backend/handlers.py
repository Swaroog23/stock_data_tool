from fastapi import HTTPException

from utils import fetch_stock_data, transform_api_stock_data
from validators import validate_api_result


def retrive_and_transform_stock_data(stock_symbol:str, is_full:bool):
    stock_symbol = stock_symbol.upper()
    raw_stock_data = fetch_stock_data(stock_symbol, full_output=is_full)
    if validate_api_result(raw_stock_data) == -1:
        raise HTTPException(status_code=404, detail="Item not found")
    transformed_data = transform_api_stock_data(raw_stock_data)
    
    return {"symbol": stock_symbol, "data": transformed_data}
