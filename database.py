from models.user import *

def initialize(): 
    global currentUser 
    currentUser = User(0, 'default', 'default', 'default')

