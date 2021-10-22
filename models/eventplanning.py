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

    def print_eventplannings_list(self, eventplannings_list):
        print("Current Events")
        if (len(eventplannings_list) == 0):
            print("No Event available") 
        for index, ref in enumerate(eventplannings_list):
            eventplanning = eventplannings_list[index]
            print(
                "[", index, "] "
                " | Client name: ", eventplanning.client_name,
                " | Event type: ", eventplanning.event_type,
                " | Event description: ", eventplanning.description,
                " |\n"
                " | Date: ", eventplanning.start_date, " - ", eventplanning.end_date,
                " | Budget: ", eventplanning.planned_budget,
                " | Attendees: ", eventplanning.expected_attendees,
                " |\n"
                " | Decoration: ", eventplanning.info_decoration,
                " | Catering: ", eventplanning.info_catering,
                " | Documentation: ", eventplanning.info_documentation,
                " | Music: ", eventplanning.info_music,
                " | Graphics: ", eventplanning.info_graphic,
                " | Technical: ", eventplanning.info_technical,
                " | Other: ", eventplanning.info_other,
                " |\n"
                )
        print("")
        return

    def show_current_eventplannings(self):
        eventplannings_list = []
        for index, ref in enumerate(database.eventPlanning_List):
            eventplanning = database.eventPlanning_List[index]
            if (eventplanning.status != "archived"):
                eventplannings_list.append(eventplanning)
        self.print_eventplannings_list(eventplannings_list)
        return eventplannings_list
