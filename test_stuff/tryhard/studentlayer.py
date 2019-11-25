class Students:

    def __init__(self, firstname, lastname, __term):
        self.firstname = firstname
        self.lastname = lastname
        self.__term = __term

    def increase_term(self):
        if self.__term >= 9:
            return
        self.__term = self.__term + 1

    def get_term(self):
        return self.__term

    def get_lastname(self):
        return self.lastname

    def get_firstname(self):
        return self.firstname


erik = Students("Erik", "Ficker", 1)

