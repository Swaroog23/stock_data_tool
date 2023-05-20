from utils import fetch_company_data, fetch_stock_data, transform_api_stock_data
from validators import validate_api_result
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/stock/{stock_symbol}/latest")
def get_latest_stock_data_view(stock_symbol:str):
    stock_symbol = stock_symbol.upper()
    raw_stock_data = fetch_stock_data(stock_symbol)
    if validate_api_result(raw_stock_data) == -1:
        raise HTTPException(status_code=404, detail="Item not found")
    transformed_data = transform_api_stock_data(raw_stock_data)
    
    return {"symbol": stock_symbol, "data": transformed_data}

@router.get("/stock/{stock_symbol}/full")
def get_full_stock_data_view(stock_symbol:str):
    stock_symbol = stock_symbol.upper()
    raw_stock_data = fetch_stock_data(stock_symbol, True)
    if validate_api_result(raw_stock_data) == -1:
        raise HTTPException(status_code=404, detail="Item not found")
    transformed_data = transform_api_stock_data(raw_stock_data)
    
    return {"symbol": stock_symbol, "data": transformed_data}

@router.get("/search/{search_query}")
def get_company_view(search_query:str):
    return fetch_company_data(search_query)
    