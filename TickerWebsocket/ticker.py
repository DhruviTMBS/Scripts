from kiteconnect import KiteConnect
from datetime import datetime
import time

API_KEY = '88bh1jr80qvugi6i'

API_SECRET = '1ryg9hlbj9dqezkx0jmw1k2qd391x25o'

kite = KiteConnect(api_key=API_KEY)

ACCESS_TOKEN = 'ZnvAblM0vQDb4UURnikGiujgxrVBH8HI'  # Valid Till 24 Hour

instruments = kite.instruments()
segments = set(map(lambda x: x['segment'], instruments))

all_instruments = [instrument for instrument in instruments if instrument['segment'] in ['INDICES', 'NFO-FUT', 'NSE', 'NFO-OPT'] if instrument['name'] not in ['', ' ', None]]

list_keys = ['instrument_token', 'tradingsymbol', 'name', 'expiry', 'strike', 'instrument_type', 'segment', 'exchange']
all_instruments = [{k: v for k, v in d.items() if k in list_keys} for d in all_instruments]

for i in range(len(all_instruments)):
    all_instruments[i]['expiry'] = None if all_instruments[i]['expiry'] == "" else all_instruments[i]['expiry'].strftime("%m/%d/%Y")


futures_instrument = [instrument for instrument in instruments if instrument['segment'] in ['NFO-FUT'] if instrument['name'] not in ['', ' ', None]]
stock_instrument = [instrument for instrument in instruments if instrument['segment'] in ['NSE'] if instrument['name'] not in ['', ' ', None]]
indices_instrument = [instrument for instrument in instruments if instrument['segment'] in ['INDICES'] if instrument['name'] not in ['', ' ', None]]
print(len(futures_instrument),len(stock_instrument), len(indices_instrument))

options_instruments = [instrument for instrument in instruments if instrument['segment'] in ['NFO-OPT'] if instrument['name'] not in ['', ' ']]

kite.set_access_token(ACCESS_TOKEN) 
nfo_opt_symbols = ["NFO:" + instrument["tradingsymbol"] for instrument in options_instruments]
nfo_fut_symbols = ["NFO:" + instrument["tradingsymbol"] for instrument in futures_instrument]
nfo_ind_symbols = ["BSE:" + instrument["tradingsymbol"] for instrument in indices_instrument]
nfo_stock_symbols = ["NSE:" + instrument["tradingsymbol"] for instrument in stock_instrument]
