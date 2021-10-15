import database

def mainView():

    if database.currentUser.position=="CSO":
        #cso_view()
        pass
    elif database.currentUser.position=="SCSO":
        #scso_view()
        pass
    elif database.currentUser.position=="AM":
        #am_view()
        pass
    elif database.currentUser.position=="FM":
        #fm_view()
        pass
    elif database.currentUser.position=="SM":
        #sm_view()
        pass
    elif database.currentUser.position=="PM":
        #pm_view()
        pass
    elif database.currentUser.position=="HRTM":
        #hrtm_view()
        pass
    elif database.currentUser.position=="STM":
        #stm_view()
        pass
    else:
        raise NameError('Position has no main view')
    return
