import database
from ui.stmView import SubTeamMemberView
from ui.csoView import CustomerServiceOfficerView
from ui.pmView import ProductionManagerView
from ui.smView import ServiceManagerView
from ui.scsoView import SeniorCustomerServiceOfficerView
from ui.fmView import FinancialManagerView
from ui.amView import AdministrationManagerView

def mainView():

    if database.currentUser.position=="CSO": CustomerServiceOfficerView()
    elif database.currentUser.position=="SCSO": SeniorCustomerServiceOfficerView()
    elif database.currentUser.position=="AM": AdministrationManagerView()
    elif database.currentUser.position=="FM": FinancialManagerView()
    elif database.currentUser.position=="SM": ServiceManagerView()
    elif database.currentUser.position=="PM": ProductionManagerView()
    elif database.currentUser.position=="HRTM": 
        #hrtm_view() 
        pass
    elif database.currentUser.position=="STM": SubTeamMemberView()
    else: raise NameError('Position has no main view')
    return
