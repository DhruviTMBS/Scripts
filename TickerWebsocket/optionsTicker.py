from ticker import *
from helpers import GetQuotes, StoreTicks, format_ticks
from sgqlc_app import op_options, endpoint

def format_date_options(date_list):
    for i in range(len(date_list)):
        date_list[i]['exchange_timestamp'] = None if date_list[i]['exchange_timestamp'] == "" else date_list[i]['exchange_timestamp'].strftime('%Y-%m-%d %H:%M:%S %z')

    return date_list


def store_options_data():
    while True:
        nfo_opt_symbols_values = GetQuotes(nfo_opt_symbols)
        
        options_data = format_ticks(nfo_opt_symbols_values)
        options_data = format_date_options(options_data)
        print(options_data[:2])
        index_count = 0
        for d in range(len(options_data)):
            if index_count < len(options_data):
                optionData = endpoint(op_options, {"listofoptionsticks": options_data[index_count: index_count + 1500]})
                print(optionData)
                if 'error' in optionData.keys():
                    print(options_data[index_count: index_count + 1500])
                index_count += 1500


store_options_data()


