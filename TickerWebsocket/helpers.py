import time
from ticker import *
from sgqlc_app import endpoint, op_futures, op_indices, op_options, op_stocks


def format_date(date_list):
    for i in range(len(date_list)):
        date_list[i]['exchange_timestamp'] = None if date_list[i]['exchange_timestamp'] == "" else date_list[i]['exchange_timestamp'].strftime('%Y-%m-%d %H:%M:%S %z')

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
    # filtered_ticks = format_date(filtered_ticks)

    return filtered_ticks

def selectOperation(symbol_type):
    if symbol_type == "op_stocks":
        op = op_stocks
    elif symbol_type == "op_futures":
        op = op_futures
    elif symbol_type == "op_options":
        op = op_options
    elif symbol_type == "op_indices":
        op = op_indices
    else:
        print("Wrong operation!")
        op = None
    
    return op

def GetQuotes(nfo_symbols):
    symbols_count = 0
    nfo_symbols_list = []
    for i in range(len(nfo_symbols)):
        if symbols_count < len(nfo_symbols):
            print("symbols_count",symbols_count)
            try:
                nfo_quotes = kite.quote(nfo_symbols[symbols_count:symbols_count+500])
                nfo_symbols_list.append(nfo_quotes)                  
            except Exception as e: 
                print("Error occured: ", e) 

        
            time.sleep(1)           
            symbols_count += 500
        
    nfo_symbols_values = [v for d in nfo_symbols_list for k, v in d.items()]
    return nfo_symbols_values

def StoreTicks(symbol_data, symbol_type, listofsymbol):
    op_symbol = selectOperation(symbol_type)
    index_count = 0
    for d in range(len(symbol_data)):
        if index_count < len(symbol_data):
            try:
                symbolData = endpoint(op_symbol, {listofsymbol: symbol_data[index_count: index_count + 50]})
                
                if 'errors' in symbolData.keys():
                    for f in symbol_data[index_count: index_count + 50]:
                        symbolData1 = endpoint(op_symbol, {listofsymbol: f})
                        
                        if 'errors' in symbolData1.keys():
                            print(f)
                        else:
                            print(symbolData1) 
                else:
                    print(symbolData)

            except Exception as e:
                print(symbol_data[index_count: index_count + 50])
                print("Error occured: ", e)
            index_count += 50