
class Students():


    def __init__(self, firstname, lastname, accountnumber, iban):
        self.firstname = firstname
        self.lastname = lastname
        self.__accountnumber = accountnumber
        self.__iban = iban
        
    def get_name(self):
        return self.firstname, self.lastname
        
    def bank_account(self):
        
        return self.__accountnumber, self.__iban



lisa = Students("Lisa", "Klein", "RZ1230", "AT123123")
annalisa = Students("Annalisa", "Hober", "UJ234", "AT5564456")
melanie = Students("Melanie", "Hermann", "ZT119", None)
