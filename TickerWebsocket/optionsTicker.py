from ticker import *
from sgqlc_app import op_options, endpoint
import time


def format_date(date_list):
    # import pdb;pdb.set_trace()
    for i in range(len(date_list)):
        date_list[i]['exchange_timestamp'] = None if date_list[i]['exchange_timestamp'] == "" else date_list[i]['exchange_timestamp'].strftime('%Y-%m-%d %H:%M:%S.%f %z')

    return date_list

def format_ticks(ticks):
    list_keys = ['instrument_token', 'timestamp', 'last_price', 'volume', 'oi']
    filtered_ticks = [{k: v for k, v in d.items() if k in list_keys} for d in ticks]
    
    rem_list = ['timestamp', 'volume', 'oi']
    for k in filtered_ticks:
        k["exchange_timestamp"] = k["timestamp"]
        k["volume_traded"] = k["volume"]
        k["open_interest"] = k["oi"]

        [k.pop(key) for key in rem_list]
    filtered_ticks = format_date(filtered_ticks)

    return filtered_ticks

def store_options_data():
    while True:
        opt_count = 0
        nfo_opt_symbols_list = []
        for i in range(len(nfo_opt_symbols)):
            print(opt_count)
            if opt_count < len(nfo_opt_symbols):
                try:
                    nfo_opt_quotes = kite.quote(nfo_opt_symbols[opt_count:opt_count+500])
                    nfo_opt_symbols_list.append(nfo_opt_quotes)                  
                except Exception as e:    
                    print("Error occured: ", e) 
            
                time.sleep(1)           
                opt_count += 500
        
        nfo_opt_symbols_values = [v for d in nfo_opt_symbols_list for k, v in d.items()]

        index_count = 0
        options_data = format_ticks(nfo_opt_symbols_values)
        for d in range(len(options_data)):
            if index_count < len(options_data):
                optionData = endpoint(op_options, {"listofoptionsticks": options_data[index_count: index_count + 1500]})
                index_count += 1500

store_options_data()


