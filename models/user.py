class User():
    def __init__(self, id, username, password, position):
        self.id=id
        self.username=username
        self.password=password
        self.position=position
    def ChangePassword(self, new_password):
        self.password = new_password