from ticker import *
from helpers import GetQuotes, StoreTicks, format_ticks, format_date

def store_stocks_data():
    while True:
        nfo_stock_symbols_values = GetQuotes(nfo_stock_symbols)
        
        print("nfo_stock_symbols",len(nfo_stock_symbols_values))
        stocks_data = format_ticks(nfo_stock_symbols_values)
        stocks_data = format_date(stocks_data)

        StoreTicks(stocks_data, "op_stocks", "listofstockticks")
        
store_stocks_data()


