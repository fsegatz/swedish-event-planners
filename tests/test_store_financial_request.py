import sys, os
testdir = os.path.dirname(__file__)
parentdir = '..'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, parentdir)))

from models.staffrequest import *
import database


def main():
    database.initialize()

    atributes=["id 192", "Decoration" , "40 000" , "Need to buy new chandalier" , "Plz u owe me one", "Opened"]

    req=StaffRequest(database.id_counter.get_new(),atributes)
    database.staffRequest_List.append(req)
    if req in database.staffRequest_List: print("it worked!")
    else: print("it did not work!! :,(")

main()