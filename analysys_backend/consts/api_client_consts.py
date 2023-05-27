import os

from dotenv import load_dotenv

load_dotenv("conf/.env")

API_KEY = os.getenv("AV_API_KEY")
BASE_URL = "https://www.alphavantage.co/query"
