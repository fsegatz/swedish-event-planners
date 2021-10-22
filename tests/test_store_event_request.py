#"The system should be able to permanently store event requests (client_record_number, client_name. event_type,
# expected_number_attendees. expected_budget, start_date, end_date, priorities, feasibility_review, financial_review, status)."
#from models.eventRequest import EventRequest

# Needed to import rom parent directory
import sys, os
testdir = os.path.dirname(__file__)
parentdir = '..'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, parentdir)))

import database
from models.eventRequest import *

def main():
    database.initialize()

    req=EventRequest(database.id_counter.get_new())
    database.eventRequest_List.append(req)
    if req in database.eventRequest_List: print("it worked!")
    else: print("it did not work!! :,(")

main()