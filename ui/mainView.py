import database
from ui.stmView import stm_view
from ui.csoView import CustomerServiceOfficerView
from ui.pmView import ProductionManagerView
from ui.smView import sm_view
from ui.scsoView import SeniorCustomerServiceOfficerView
from ui.fmView import FinancialManagerView
from ui.amView import AdministrationManagerView

def mainView():

    if database.currentUser.position=="CSO": CustomerServiceOfficerView()
    elif database.currentUser.position=="SCSO": SeniorCustomerServiceOfficerView()
    elif database.currentUser.position=="AM": AdministrationManagerView()
    elif database.currentUser.position=="FM": FinancialManagerView()

    elif database.currentUser.position=="SM":
        sm_view()
        pass
    elif database.currentUser.position=="PM": ProductionManagerView()
    elif database.currentUser.position=="HRTM":
        #hrtm_view()
        pass
    elif database.currentUser.position=="STM":
        stm_view()
        pass
    else:
        raise NameError('Position has no main view')
    return
