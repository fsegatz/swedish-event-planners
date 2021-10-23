import sys, os
testdir = os.path.dirname(__file__)
parentdir = '..'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, parentdir)))

from models.staffrequest import *
import database
from ui.smView import *
from ui.pmView import *


def main():
    database.initialize()

    ServiceManagerView().create_staff_request() #start with enter 0
    if database.staffRequest_List: input("it worked with ServiceManagerView!")
    else: input("it did not work with ServiceManagerView!! :,(")

    ProductionManagerView().create_staff_request() #start with enter 0
    if database.staffRequest_List: input("it worked with ProductionManagerView!")
    else: input("it did not work with ProductionManagerView!! :,(")

main()