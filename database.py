from models.user import *
from id_counter import Id_counter

def initialize(): 
    global currentUser 
    currentUser = User(0, 'default', 'default', 'default')

    #Counter to ensure new id to all instances
    global id_counter
    id_counter=Id_counter() 
    
    #Storage for subteam tasks
    global subTeamTask_List
    subTeamTask_List = []

    #Storage for event requests
    global eventRequest_List
    eventRequest_List = []
    
    #Storage for event plannings
    global eventPlanning_List
    eventPlanning_List = []
