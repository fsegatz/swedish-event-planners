import database

class UserView:
    def print_username(self):
        print("Welcome ", database.currentUser.username.capitalize())
        return