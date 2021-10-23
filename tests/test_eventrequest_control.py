import sys, os

testdir = os.path.dirname(__file__)
parentdir = '..'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, parentdir)))

from models.eventrequest import *
import database

database.initialize()
database.currentUser.id = 1
database.currentUser.username = 'SCSO'
database.currentUser.password = 123
database.currentUser.position = 'SCSO'

atributes=[1,"Skynet","Doomsday","nine billion", 100000, 2022-10-12, 3048-10-12, "Destruction!", "Open"]
eventRequest_Control=EventRequest_Control()
eventRequest_Control.create_event_request(atributes)


print(*eventRequest_Control.get_event_request_for_user())
