from fastapi import APIRouter
import requests
from handlers import retrive_and_transform_stock_data, retrive_company_data

router = APIRouter()

@router.get("/stock/{stock_symbol}/latest")
def get_latest_daily_data_view(stock_symbol:str):
    return retrive_and_transform_stock_data(stock_symbol, False, "TIME_SERIES_DAILY_ADJUSTED")

@router.get("/stock/{stock_symbol}/full")
def get_full_daily_data_view(stock_symbol:str):
    return retrive_and_transform_stock_data(stock_symbol, True, "TIME_SERIES_DAILY_ADJUSTED")


@router.get("/search/{search_query}")
def get_company_view(search_query:str):
    return retrive_company_data(search_query)
    

@router.get("/intraday/{stock_symbol}")
def get_latest_intraday_data_view(stock_symbol:str, interval:int = 60):
    return retrive_and_transform_stock_data(stock_symbol, False, "TIME_SERIES_INTRADAY", interval)