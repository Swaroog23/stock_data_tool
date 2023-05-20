from fastapi import APIRouter

from handlers import retrive_and_transform_stock_data
from utils import fetch_company_data

router = APIRouter()

@router.get("/stock/{stock_symbol}/latest")
def get_latest_stock_data_view(stock_symbol:str):
    return retrive_and_transform_stock_data(stock_symbol, False)

@router.get("/stock/{stock_symbol}/full")
def get_full_stock_data_view(stock_symbol:str):
        return retrive_and_transform_stock_data(stock_symbol, True)


@router.get("/search/{search_query}")
def get_company_view(search_query:str):
    return fetch_company_data(search_query)
    