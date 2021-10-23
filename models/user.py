import database

class User:
    def __init__(self, id, username, password, position):
        self.id=id
        self.username=username
        self.password=password
        self.position=position
    def change_password(self, new_password):
        self.password = new_password

class User_Control:
    def create_user(self, user):
        database.user_List.append(user)
        return

    def get_user_entry_with_username(self, username): 
        user_List = [user for user in database.user_List if user and user.username.upper() == username.upper()]
        if(len(user_List) != 0):
            return user_List[0]
        return


    def login(self, username, password):
        user = self.get_user_entry_with_username(username)
        
        if (user and user.password == password):
            database.currentUser = user
            return True

        return False

    def fill_user_database(self):
        #Administration manager
        self.create_user(User(database.id_counter.get_new(), 'AM', '123', 'AM'))
        self.create_user(User(database.id_counter.get_new(), 'Mike', '123', 'AM'))

        #Human resource team member
        self.create_user(User(database.id_counter.get_new(), 'HRTM', '123', 'HRTM'))
        self.create_user(User(database.id_counter.get_new(), 'Simon', '123', 'HRTM'))
        self.create_user(User(database.id_counter.get_new(), 'Maria', '123', 'HRTM'))

        #Senior customer service officer
        self.create_user(User(database.id_counter.get_new(), 'SCSO', '123', 'SCSO'))
        self.create_user(User(database.id_counter.get_new(), 'Janet', '123', 'SCSO'))

        #Customer service officer
        self.create_user(User(database.id_counter.get_new(), 'CSO', '123', 'CSO'))
        self.create_user(User(database.id_counter.get_new(), 'Sarah', '123', 'CSO'))
        self.create_user(User(database.id_counter.get_new(), 'Sam', '123', 'CSO'))
        self.create_user(User(database.id_counter.get_new(), 'Judy', '123', 'CSO'))
        self.create_user(User(database.id_counter.get_new(), 'Carine', '123', 'CSO'))

        #Marketing team member
        self.create_user(User(database.id_counter.get_new(), 'MTM', '123', 'MTM'))
        self.create_user(User(database.id_counter.get_new(), 'David', '123', 'MTM'))
        self.create_user(User(database.id_counter.get_new(), 'Emma', '123', 'MTM'))

        #Financial manager
        self.create_user(User(database.id_counter.get_new(), 'FM', '123', 'FM'))
        self.create_user(User(database.id_counter.get_new(), 'Alice', '123', 'FM'))

        #Financial team member
        self.create_user(User(database.id_counter.get_new(), 'FTM', '123', 'FTM'))
        self.create_user(User(database.id_counter.get_new(), 'Fredrik', '123', 'FTM'))
        self.create_user(User(database.id_counter.get_new(), 'Sophia', '123', 'FTM'))

        #Production manager
        self.create_user(User(database.id_counter.get_new(), 'PM', '123', 'PM'))
        self.create_user(User(database.id_counter.get_new(), 'Jack', '123', 'PM'))
        
        #Service manager
        self.create_user(User(database.id_counter.get_new(), 'SM', '123', 'SM'))
        self.create_user(User(database.id_counter.get_new(), 'Natalie', '123', 'SM'))

        #Sub team Member
        self.create_user(User(database.id_counter.get_new(), 'STM', '123', 'STM'))

        #Photographer
        self.create_user(User(database.id_counter.get_new(), 'Tobias', '123', 'STM'))
        self.create_user(User(database.id_counter.get_new(), 'Magdalena', '123', 'STM'))

        #Audio specialis
        self.create_user(User(database.id_counter.get_new(), 'Antony', '123', 'STM'))
        self.create_user(User(database.id_counter.get_new(), 'Adam', '123', 'STM'))

        #Graphic designe
        self.create_user(User(database.id_counter.get_new(), 'Julia', '123', 'STM'))
        self.create_user(User(database.id_counter.get_new(), 'Raymond', '123', 'STM'))

        #Decoration team
        self.create_user(User(database.id_counter.get_new(), 'Magy', '123', 'STM'))
        self.create_user(User(database.id_counter.get_new(), 'Angelina', '123', 'STM'))
        self.create_user(User(database.id_counter.get_new(), 'Don', '123', 'STM'))
        self.create_user(User(database.id_counter.get_new(), 'Tom', '123', 'STM'))

        #Technical support
        self.create_user(User(database.id_counter.get_new(), 'Christian', '123', 'STM'))
        self.create_user(User(database.id_counter.get_new(), 'Nicolas', '123', 'STM'))
        self.create_user(User(database.id_counter.get_new(), 'Michael', '123', 'STM'))
        self.create_user(User(database.id_counter.get_new(), 'Robert', '123', 'STM'))

        #Chef
        self.create_user(User(database.id_counter.get_new(), 'Helen', '123', 'STM'))
        self.create_user(User(database.id_counter.get_new(), 'Diana', '123', 'STM'))
        self.create_user(User(database.id_counter.get_new(), 'Chris', '123', 'STM'))
        self.create_user(User(database.id_counter.get_new(), 'Daniel', '123', 'STM'))
        self.create_user(User(database.id_counter.get_new(), 'Marilyn', '123', 'STM'))      

        #Waiters/Waitresses
        self.create_user(User(database.id_counter.get_new(), 'Kate', '123', 'STM'))
        self.create_user(User(database.id_counter.get_new(), 'Lauren', '123', 'STM'))
        self.create_user(User(database.id_counter.get_new(), 'Johnny', '123', 'STM'))
        self.create_user(User(database.id_counter.get_new(), 'Meryl', '123', 'STM'))

        #Vice President
        self.create_user(User(database.id_counter.get_new(), 'VP', '123', 'VP'))
        self.create_user(User(database.id_counter.get_new(), 'Charlie', '123', 'VP'))
        
        return