import database
from datetime import datetime
from clear import clear

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
        eventPlanning = None
        clear()
        self.print_eventplannings_list(eventPlanningsList)

        while(True):

            key = input("Enter index of subteam task that should be commented, or c to cancel: ")
            if (key.lower() == 'c'): break
            elif (key.isnumeric() and int(key) < len(eventPlanningsList)):
                eventPlanning = eventPlanningsList[int(key)]
                break
            else: print("No valid input")

        return eventPlanning

    def event_planning_info_edit_dialog(self, eventPlanning):
        #search for event planning in db with same id
        for index, ref in enumerate(database.eventPlanning_List):
            buf = database.eventPlanning_List[index]
            if (eventPlanning.id == buf.id):
                break
            
        # Add event to a list, so that print_eventplannings_list function can be reused
        eventPlanningList = []
        eventPlanningList.append(eventPlanning)

        while(True):
            clear()
            self.print_eventplannings_list(eventPlanningList)
            print("[0] Return")
            print("[1] Edit decoration info")
            print("[2] Edit catering info")
            print("[3] Edit documentation info")
            print("[4] Edit music info")
            print("[5] Edit graphics info")
            print("[6] Edit technical info")
            key = input("Please choose option: ")
            if (key == '0'): break
            if ((not key.isnumeric()) or int(key) > 6): 
                continue
            comment = input("Please enter comment: ")
            if (key == '1'): database.eventPlanning_List[index].info_decoration = comment
            elif (key == '2'): database.eventPlanning_List[index].info_catering = comment
            elif (key == '3'): database.eventPlanning_List[index].info_documentation = comment
            elif (key == '4'): database.eventPlanning_List[index].info_music = comment
            elif (key == '5'): database.eventPlanning_List[index].info_graphics = comment
            elif (key == '6'): database.eventPlanning_List[index].info_technical = comment
        
        return