import database
from datetime import datetime


class EventPlanning:
    def __init__(self, client_record_number, client_name, event_type, description, expected_attendees, planned_budget, start_date, end_date):
        self.id = ""
        self.creation_date = datetime.now()
        self.client_record_number = client_record_number
        self.client_name = client_name
        self.event_type = event_type
        self.description = description
        self.expected_attendees = expected_attendees
        self.planned_budget = planned_budget
        self.start_date = start_date
        self.end_date = end_date
        self.info_decoration = ""
        self.info_catering = ""
        self.info_documentation = ""
        self.info_music = ""
        self.info_graphic = ""
        self.info_technical = ""
        self.info_other = ""
        self.feasibility_review = ""
        self.financial_review  = ""
        self.status = ""
        return

class EventPlanning_Control:
    def append(self, eventplanning):
        length = len(database.eventPlanning_List)
        if (length == 0):
            eventplanning.id = 1
        else:
            eventplanning.id = database.eventPlanning_List[length-1].id + 1
        database.eventPlanning_List.append(eventplanning)
        return

    def show_current_eventplannings(self):
        return