import sys, os
testdir = os.path.dirname(__file__)
parentdir = '..'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, parentdir)))

from models.user import User_Control
from models.financialrequest import *
import database
from ui.fmView import *


def main():
    database.initialize()
    user_Control = User_Control()
    user_Control.fill_user_database()   

    atributes=["id 192", "Decoration" , "40 000" , "Need to buy new chandalier" , "Plz u owe me one", "Opened"]

    
    req1=FinancialRequest(database.id_counter.get_new(),atributes)
    req2=FinancialRequest(database.id_counter.get_new(),atributes)
    req3=FinancialRequest(database.id_counter.get_new(),atributes)

    database.financialRequest_List.append(req1)
    database.financialRequest_List.append(req2)
    database.financialRequest_List.append(req3)

    FinancialManagerView() 


main()