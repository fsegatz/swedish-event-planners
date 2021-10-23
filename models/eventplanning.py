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
    def append(self, eventPlanning):
        eventPlanning.id = database.id_counter.get_new()
        database.eventPlanning_List.append(eventPlanning)
        return

    def print_eventplannings_list(self, eventPlanningsList):
        print("Current Events")
        if (len(eventPlanningsList) == 0):
            print("No Event available") 
        for index, ref in enumerate(eventPlanningsList):
            eventPlanning = eventPlanningsList[index]
            print(
                "[", index, "] "
                " | Client name: ", eventPlanning.client_name,
                " | Event type: ", eventPlanning.event_type,
                " | Event description: ", eventPlanning.description,
                " |\n"
                " | Date: ", eventPlanning.start_date, " - ", eventPlanning.end_date,
                " | Budget: ", eventPlanning.planned_budget,
                " | Attendees: ", eventPlanning.expected_attendees,
                " |\n"
                " | Decoration: ", eventPlanning.info_decoration,
                " | Catering: ", eventPlanning.info_catering,
                " | Documentation: ", eventPlanning.info_documentation,
                " | Music: ", eventPlanning.info_music,
                " | Graphics: ", eventPlanning.info_graphic,
                " | Technical: ", eventPlanning.info_technical,
                " | Other: ", eventPlanning.info_other,
                " |\n"
                )
        print("")
        return

    def show_current_eventplannings(self):
        eventPlanningsList = []
        for index, ref in enumerate(database.eventPlanning_List):
            eventPlanning = database.eventPlanning_List[index]
            if (eventPlanning.status != "archived"):
                eventPlanningsList.append(eventPlanning)
        self.print_eventplannings_list(eventPlanningsList)
        return eventPlanningsList

    def event_planning_select_from_list(self, eventPlanningsList):
        return

    def event_planning_info_edit_dialog(self, eventPlanning):
        return