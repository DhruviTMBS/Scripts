from ticker import *
from helpers import GetQuotes, StoreTicks, format_date


def format_indices_ticks(ticks):
    list_keys = ['instrument_token', 'timestamp', 'last_price']
    filtered_ticks = [{k: v for k, v in d.items() if k in list_keys} for d in ticks]
    
    for k in filtered_ticks:
        k["exchange_timestamp"] = k["timestamp"]
        del k["timestamp"]
    filtered_ticks = format_date(filtered_ticks)

    return filtered_ticks

def store_indices_data():
    while True:
        nfo_ind_symbols_values = GetQuotes(nfo_ind_symbols)
        
        print("nfo_ind_symbols",len(nfo_ind_symbols_values))
        indices_data = format_indices_ticks(nfo_ind_symbols_values)

        StoreTicks(indices_data, "op_indices", "listofindiceticks")

store_indices_data()


