# User Story
# "The system should be able to permanently store 
# event plannings (client_record_number, client_name, event_type, description, expected_attendees, 
# planned_budget, start_date, end_date, info_decoration, info_catering, info_documentation, info_music, 
# info_graphic, info_technical, info_other, feasibility_review, financial_review, status)."

# Needed to import rom parent directory
import sys, os
testdir = os.path.dirname(__file__)
parentdir = '..'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, parentdir)))

from models.eventplanning import *

def main():
    client_record_number = "12"
    client_name = "John"
    event_type = "Birthday party"
    description = "John wants SEB to organise the birthday party of his grandmother Elisabeth who turns 99 years old"
    expected_attendees = 99
    planned_budget = 2500
    start_date = "2021-12-24 10:00"
    end_date = "2021-12-24 20:00"

    eventplanning = EventPlanning(client_record_number, client_name, event_type, description, expected_attendees, planned_budget, start_date, end_date)

    if( eventplanning.event_type == event_type):
        print("EventPlanning was created at", eventplanning.creation_date)
    else:
        print("EventPlanning instanciation doesn't work")

    return
main()