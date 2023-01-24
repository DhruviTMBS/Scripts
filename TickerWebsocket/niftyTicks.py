import requests 
import csv
from io import StringIO
import time
from sgqlc_app import endpoint

def execute_nifty50_query(symbol):
    is_nifty50_query = '''mutation niftyMutation($symbolname: String!) {
    update_master_data(where: {tradingsymbol: {_eq: $symbolname}}, _set: {is_nifty: true}) {
        affected_rows
    }
    }'''

    query_variables= {'symbolname': ''}

    try:
        query_variables["symbolname"] = symbol
        data=  endpoint(is_nifty50_query, query_variables)

    except Exception as e:
        print("While Executing Query Exception Occured:", e)

def store_nifty50_data():
    try:
        url = "https://archives.nseindia.com/content/indices/ind_nifty50list.csv"

        response = requests.get(url)

        if response.status_code == 200: 
            f = StringIO(response.text) 
            reader = csv.DictReader(f) 
            data = list(reader) 
            f.close() 
            symbol_list = [item["Symbol"] for item in data]
            for symbol in symbol_list:
                print("nifty50 Symbol", symbol)
                execute_nifty50_query(symbol)
                time.sleep(1)
            
        else: 
            print("Failed to download file.")

    except Exception as e:    
        print("Error occured: ", e)

store_nifty50_data()