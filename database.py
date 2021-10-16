from models.user import *

def initialize(): 
    global currentUser 
    currentUser = User(0, 'default', 'default', 'default')

    #Storage for subteam tasks
    global subTeamTask_List
    subTeamTask_List = []

