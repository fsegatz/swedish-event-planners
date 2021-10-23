import sys, os
testdir = os.path.dirname(__file__)
parentdir = '..'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, parentdir)))

from models.staffrequest import *
import database
from ui.smView import *


def main():
    database.initialize()

    ServiceManagerView().create_staff_request() #start with enter 0
    if database.staffRequest_List: print("it worked!")
    else: print("it did not work!! :,(")

main()