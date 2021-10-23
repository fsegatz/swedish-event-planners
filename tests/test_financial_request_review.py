from models.financialrequest import *
import database
from ui.fmView import *


def main():
    database.initialize()
    atributes=["id 192", "Decoration" , "40 000" , "Need to buy new chandalier" , "Plz u owe me one", "Opened"]

    
    req1=FinancialRequest(database.id_counter.get_new(),atributes)
    req2=FinancialRequest(database.id_counter.get_new(),atributes)
    req3=FinancialRequest(database.id_counter.get_new(),atributes)

    database.financialRequest_List.append(req1)
    database.financialRequest_List.append(req2)
    database.financialRequest_List.append(req3)

    FinancialManagerView() 


main()