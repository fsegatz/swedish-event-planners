import sys, os

testdir = os.path.dirname(__file__)
parentdir = '..'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, parentdir)))

from models.eventRequest import *
import database

database.initialize()
database.currentUser.id = 1
database.currentUser.username = 'SCSO'
database.currentUser.password = 123
database.currentUser.position = 'SCSO'

atributes=[1,"Skynet","Doomsday","nine billion", 100000, 2022-10-12, 3048-10-12, "Destruction!", "Open"]
eventRequest_control=EventRequest_control()
eventRequest_control.create_eventRequest_test(atributes)


eventRequest_control.show_event_request_for_user()