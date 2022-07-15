from additional_exceptions import InsufficientFunds 

class Account:
    # constructor that initializes the account type and owner from the child classes 
    # and sets the account balance to zero.
    def __init__(self, accountType, owner):
        self.__accountType = accountType
        self.__owner = owner    # Customer Object
        self.__accountBalance = 0.0
    
    # returns the current balance of the account. 
    # This doubles up as a getter for the balance attribute.
    def check_accountBalance(self):
        return self.__accountBalance 
    
    # 1 setter for the balance attribute 
    # 2 getters for owner and account type
    def set_accountBalance(self, accountBalance):
        self.__accountBalance = accountBalance
        
    def get_owner(self):
        return self.__owner
        
    def get_accountType(self):
        return self.__accountType
    
    # accepts a monetary amount (be it of type integer or float or string ), 
    # converts it to type float . Raise a ValueError if the monetary amount is <= 0 or 
    # the amount has more than 2 decimal places. Return True otherwise
    def __validate_amount(self, amount): # private method
        amount = float(amount)
        decimalPlaces = len(str(amount).split(".")[1])
        if decimalPlaces > 2 or amount <= 0:
            raise ValueError
        else:    
            return True
    
    
    # debit() - accepts an amount, checks it then subtracts it from the balance. 
    # Returns True if there is enough funds for the debit otherwise, 
    # raise an InsufficientFunds exception (the balance remains unchanged).
    def debit(self, amount):
        self.__validate_amount(amount) # Accepts and Checking
        if amount <= self.__accountBalance: 
            self.__accountBalance -= float(amount)
            return True 
        else: 
            raise InsufficientFunds
            
        
    # accepts an amount, checks it then adds it to the balance.
    def credit(self, amount):
        self.__validate_amount(amount)
        self.__accountBalance += float(amount)
        
    
    
# The Savings_Account and Current_Account classes inherit the parent class Account   
# account number - private variable. The account number of the respective account
# owner - a Customer object 
# account type - value is 'savings' for Savings_Account account or 'current' for Current_Account account.

# constructor that initializes the account number and owner from input parameters and 
# initializes the Account parent class
# with the respective account type (either 'savings' or 'current' ) and owner ( Customer object).
class Savings_Account(Account):
    def __init__(self, accountNumber, owner):
        super().__init__('savings', owner)
        self.__accountNumber = accountNumber
    
# getters for the account number variable   
    def get_accountNumber(self):
        return self.__accountNumber
    
class Current_Account(Account):
    def __init__(self, accountNumber, owner):
        super().__init__('current', owner)
        self.__accountNumber = accountNumber 
    
    
# getters for the account number variable   
    def get_accountNumber(self):
        return self.__accountNumber 
    
        
        
