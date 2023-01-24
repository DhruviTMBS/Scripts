
from ticker import all_instruments
from sgqlc_app import op_master, endpoint


def store_master_data():
    count = 0
    for i in range(len(all_instruments)):
        print("Master Count:", count)
        if count < len(all_instruments):
            masteData = endpoint(op_master,{"listofticks": all_instruments[count:count+1500]})
            count += 1500

store_master_data()