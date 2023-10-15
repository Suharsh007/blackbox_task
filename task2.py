import yfinance as yf
import pandas as pd
from pymongo import MongoClient
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta

client = MongoClient("mongodb://localhost:27017/")
db = client["stock_data"]
collection = db["icici_bank"]


def fetch_and_store_data():
    
    now = datetime.now()

    
    start_time = now.replace(hour=15, minute=45, second=0, microsecond=0)
    end_time = now.replace(hour=16, minute=15, second=0, microsecond=0)

   
    data = yf.download("ICICIBANK.NS", start=start_time, end=end_time, interval="15m")

    
    if not data.empty:
        data_dict = data.to_dict(orient="records")
        collection.insert_many(data_dict)
        print("Data stored successfully.")

fetch_and_store_data()

try:
    while True:
        pass
except (KeyboardInterrupt, SystemExit):

    print("End Script")
