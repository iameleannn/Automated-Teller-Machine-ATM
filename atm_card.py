
class ATM_Card:
    # constructor that initializes the ATM card's number and owner via input parameters.
    def __init__(self, atmCardNumber, ownedBy):
        self.__atmCardNumber = atmCardNumber       # Private
        self.__ownedBy = ownedBy                   # Private
    
    # returns a list of the account types available for the customer
    def get_acct_types(self):
       acctTypes = []
       for account in  self.__ownedBy.get_accounts():
           acctTypes.append(account.get_accountType())
    
       return acctTypes

    # accepts an account type and returns the Account object of the customer.
    def access(self, accountType):
        for account in self.__ownedBy.get_accounts():
            if account.get_accountType() == accountType:
                return account
        return None
    
    # returns a string representation of the ATM card detailing the card's number and owner's name.
    def __str__(self):
        return f"Card Number: {self.__atmCardNumber} \nCard Owner Name: {self.__ownedBy.get_name()}"
        
    def get_atmCardNumber(self):
        return self.__atmCardNumber
    
    def get_ownedBy(self):
        return self.__ownedBy