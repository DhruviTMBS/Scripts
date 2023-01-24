from ticker_schema import ticker_schema
from sgqlc.endpoint.http import HTTPEndpoint
from insertTickerData import Operations
from ticker import *
import json

url = "https://rough-shape-6577.fly.dev/v1/graphql"
headers = {"x-hasura-admin-secret": "verystrongsecret"}

op_master = Operations.mutation.master_mutation
op_indices = Operations.mutation.indices_mutation
op_stocks = Operations.mutation.stock_mutation
op_futures = Operations.mutation.futures_mutation
op_options = Operations.mutation.options_mutation

endpoint = HTTPEndpoint(url,headers)

# count = 0
# for i in range(len(all_instruments)):
#     if count < len(all_instruments):
#         data = endpoint(op_master,{"listofticks": all_instruments[count:count+1500]})
#         count += 1500
#         print(data)