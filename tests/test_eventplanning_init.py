import sys, os

testdir = os.path.dirname(__file__)
parentdir = '..'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, parentdir)))

from models.eventrequest import EventRequest_Control
from models.eventplanning import *
from clear import clear 
import database

database.initialize()
database.currentUser.id = 2
database.currentUser.username = "AM"
database.currentUser.password = "123"
database.currentUser.position = 'AM'

eventRequest_Control=EventRequest_Control()

atributes=[69,"Skynet","Doomsday","nine billion human lifes", 100000, 2022-10-12, 3048-10-12, "Destruction!"]
eventRequest_Control.create_event_request(atributes, assigned2="AM", status="Finalized", feasibility_review="10/10 would do agin", financial_review="Alright")

event_request_data=eventRequest_Control.get_info_for_event_plan(id="1")
eventRequest_Control.archived_event_request(id="1")

if eventRequest_Control.get_event_request_for_user():
    print("not working")

eventPlanning_Control=EventPlanning_Control()
eventPlanning=EventPlanning(event_request_data[0], event_request_data[1], event_request_data[2], event_request_data[3], event_request_data[4], event_request_data[5], event_request_data[6], event_request_data[7])
eventPlanning_Control.append(eventPlanning)

if database.eventPlanning_List:
    print("it worked!")

