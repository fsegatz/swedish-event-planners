from ui.userView import UserView
from clear import clear
from models.eventplanning import EventPlanning_Control
from models.staffrequest import StaffRequest_Control
from models.financialrequest import FinancialRequest_Control
from models.subteamtask import *

class ProductionManagerView(UserView):
    def __init__(self):
        while(True):
            clear()
            self.print_username()
            print("Production Manager Main View")
            print("------------------------")
            print("[0] Logout")
            print("[1] Create subteam task")
            print("[2] Show current events")
            print("[3] Create staff request")
            print("[4] Create financial request")
            print("[5] Show current financial request")

            key = input("Please choose option: ")
            if(key == '0'): break
            elif(key == '1'): self.create_subteam_task()
            elif(key == '2'): self.show_current_events()
            elif (key== "3"): self.create_staff_request()
            elif key == "4": self.create_financial_request()
            elif key == "5": self.show_current_financial_requests()

        return

    def show_current_events(self):
        eventPlanning_Control = EventPlanning_Control()
        eventPlanning_Control.show_current_eventplannings()
        
        while (True):
            clear()
            eventPlanningsList = eventPlanning_Control.show_current_eventplannings()
            if(len(eventPlanningsList) == 0):
                print("[0] Return")
                key = input("Please choose option: ")
                if (key == '0'): break
            else:
                print("[0] Return")
                print("[1] Edit event info")
                key = input("Please choose option: ")
                if (key == '0'): break
                elif (key == '1'): 
                    eventPlanning = self.event_planning_select_from_list(eventPlanningsList)
                    eventPlanning = self.event_planning_info_edit_dialog(eventPlanning)
        return
    
    def event_planning_select_from_list(self, eventPlanningsList):
        eventPlanning_Control = EventPlanning_Control()
        
        clear()
        eventPlanning_Control.print_eventplannings_list(eventPlanningsList)

        while(True):

            key = input("Enter index of subteam task that should be commented, or c to cancel: ")
            if (key.lower() == 'c'): 
                eventPlanning = None
                break
            elif (key.isnumeric() and int(key) < len(eventPlanningsList)):
                eventPlanning = eventPlanningsList[int(key)]
                break
            else: print("No valid input")

        return eventPlanning

    def event_planning_info_edit_dialog(self, eventPlanning):

        eventPlanning_Control = EventPlanning_Control()
            
        # Add event to a list, so that print_eventplannings_list function can be reused
        eventPlanningList = []
        eventPlanningList.append(eventPlanning)

        while(True):
            clear()
            eventPlanning_Control.print_eventplannings_list(eventPlanningList)
            print("[0] Return")
            print("[1] Edit decoration info")
            print("[2] Edit documentation info")
            print("[3] Edit music info")
            print("[4] Edit graphics info")
            print("[5] Edit technical info")
            print("[6] Edit other info")
            key = input("Please choose option: ")
            if (key == '0'): 
                break

            if ((not key.isnumeric()) or int(key) > 6): 
                continue

            comment = input("Please enter comment: ")
            if(not self.verify_input()):
                continue

            if (key == '1'): eventPlanning_Control.set_comment_of_eventplanning_with_id(eventPlanning.id, 'decoration', comment)
            elif (key == '2'): eventPlanning_Control.set_comment_of_eventplanning_with_id(eventPlanning.id, 'documentation', comment)
            elif (key == '3'): eventPlanning_Control.set_comment_of_eventplanning_with_id(eventPlanning.id, 'music', comment)
            elif (key == '4'): eventPlanning_Control.set_comment_of_eventplanning_with_id(eventPlanning.id, 'graphics', comment)
            elif (key == '5'): eventPlanning_Control.set_comment_of_eventplanning_with_id(eventPlanning.id, 'technical', comment)
            elif (key == '6'): eventPlanning_Control.set_comment_of_eventplanning_with_id(eventPlanning.id, 'other', comment)
        return