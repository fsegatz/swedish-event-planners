def main():
    while True:
        clear()
        
        user=input("Enter username: ")
        password=input("Enter password: (pssst its 123)  ")

        if user=="CSO" and password=="123":cso_view()

        elif user=="SCSO" and password=="123":scso_view()

        elif user=="AM" and password=="123":am_view()

        elif user=="FM" and password=="123":fm_view()

        elif user=="SM" and password=="123":sm_view()

        elif user=="PM" and password=="123":pm_view()

        elif user=="HRTM" and password=="123":hrtm_view()

        elif user=="STM" and password=="123":stm_view()

        else:
            input("Wrong login try again u stopido")
    return




main()