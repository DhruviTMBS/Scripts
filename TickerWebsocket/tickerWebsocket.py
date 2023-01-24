from kiteconnect import KiteTicker
from ticker import *
from sgqlc_app import op_indices, op_stocks, op_futures, endpoint

# ##################################################### Kite Websocket ############################################
# # Initialise
kws1 = KiteTicker(API_KEY, ACCESS_TOKEN)
kws2 = KiteTicker(API_KEY, ACCESS_TOKEN)
kws3 = KiteTicker(API_KEY, ACCESS_TOKEN)

def format_date(date_list):
    for i in range(len(date_list)):
        date_list[i]['exchange_timestamp'] = None if date_list[i]['exchange_timestamp'] == "" else date_list[i]['exchange_timestamp'].strftime('%Y-%m-%d %H:%M:%S %z')

    return date_list

def format_ticks(ticks):
    list_keys = ['instrument_token', 'exchange_timestamp', 'last_price', 'volume_traded', 'oi']
    filtered_ticks = [{k: v for k, v in d.items() if k in list_keys} for d in ticks]
    filtered_ticks = format_date(filtered_ticks)
    for k in filtered_ticks:
        k["open_interest"] = k["oi"]
        del k["oi"]

    return filtered_ticks



def on_ticks1(ws, ticks):
    # Callback to receive ticks.
    print("ticks1", len(ticks))

    list_keys = ['instrument_token', 'exchange_timestamp', 'last_price']
    filtered_ticks_indices = [{k: v for k, v in d.items() if k in list_keys} for d in ticks]
    filtered_ticks_indices = format_date(filtered_ticks_indices)

    data = endpoint(op_indices,{"listofindiceticks": filtered_ticks_indices})

def on_ticks2(ws, ticks):
    # Callback to receive ticks.
    print("ticks2", len(ticks))
    
    filtered_ticks_futures = format_ticks(ticks)
    data = endpoint(op_futures,{"listoffuturesticks": filtered_ticks_futures})

def on_ticks3(ws, ticks):
    # Callback to receive ticks.
    print("ticks3",len(ticks))
    filtered_ticks_stocks = format_ticks(ticks)
    print(filtered_ticks_stocks[0])

    data = endpoint(op_stocks,{"listofstockticks": filtered_ticks_stocks})
    
    
def on_connect1(ws, response):
    # Callback on successful connect.
    # Subscribe to a list of instrument_tokens.
    print("connecting kws1")
    ws.subscribe(indices_instrument)
    
    # Set RELIANCE to tick in `full` mode.
    ws.set_mode(ws.MODE_FULL, indices_instrument)
    
    kws2.connect()

def on_connect2(ws, response):
    # Callback on successful connect.
    # Subscribe to a list of instrument_tokens.
    print("connecting kws2")
    ws.subscribe(futures_instrument)
    
    # Set RELIANCE to tick in `full` mode.
    ws.set_mode(ws.MODE_FULL, futures_instrument)
    kws3.connect()

def on_connect3(ws, response):
    # Callback on successful connect.
    # Subscribe to a list of instrument_tokens.
    print("connecting kws3")
    ws.subscribe(stock_instrument)
    
    # Set RELIANCE to tick in `full` mode.
    ws.set_mode(ws.MODE_FULL, stock_instrument)
    

def on_close(ws, code, reason):
    # On connection close stop the main loop
    # Reconnection will not happen after executing `ws.stop()`
    print("closing kws", reason)
    ws.connect()

# # kws Assign the callbacks.
kws1.on_ticks = on_ticks1
kws2.on_ticks = on_ticks2
kws3.on_ticks = on_ticks3

kws1.on_connect = on_connect1
kws2.on_connect = on_connect2
kws3.on_connect = on_connect3

kws1.on_close = on_close
kws2.on_close = on_close
kws3.on_close = on_close

kws1.connect()