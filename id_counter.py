class Id_counter():
    def __init__(self):self.__id=0
    def get_new(self): 
        self.__id += 1
        return str(self.__id)
