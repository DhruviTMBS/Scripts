from ticker import *
from helpers import GetQuotes, StoreTicks, format_ticks, format_date

def store_futures_data():
    while True:
        nfo_fut_symbols_values = GetQuotes(nfo_fut_symbols)
        
        print("nfo_fut_symbols",len(nfo_fut_symbols_values))
        futures_data = format_ticks(nfo_fut_symbols_values)
        futures_data = format_date(futures_data)

        StoreTicks(futures_data, "op_futures", "listoffuturesticks")
        
store_futures_data()


