#User Story:
# "A ProductionManager and ServiceManager should be able to access a list of event plannings. "

## !!! not working !! ##

import sys, os
testdir = os.path.dirname(__file__)
parentdir = '..'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, parentdir)))

from models.user import User_Control
from models.eventplanning import *
import database

def main():
    database.initialize()
    user_Control = User_Control()
    user_Control.fill_user_database()
    user_Control.login("STM", "123")

    eventPlanning_Control = EventPlanning_Control()
    for i in range(5):
        client_record_number = "12"
        client_name = "John"
        event_type = "Birthday party"
        description = "John wants SEB to organise the birthday party of his grandmother Elisabeth who turns 99 years old"
        expected_attendees = 99
        planned_budget = 2500
        start_date = "2021-12-24 10:00"
        end_date = "2021-12-24 20:00"
        
        eventPlanning_Control.append(EventPlanning(client_record_number, client_name, event_type, description, expected_attendees, planned_budget, start_date, end_date))

    eventPlanning_Control.show_current_eventplannings()

    return

main()