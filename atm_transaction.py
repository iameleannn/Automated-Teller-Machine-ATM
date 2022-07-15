from datetime import datetime
from abc import ABC, abstractmethod

# ATM_Transaction class is an abstract class and has the following properties:
# constructor that initializes the transaction's date & time (timestamp), 
# transaction type and amount (default value of 0) via input parameters. 
# In addition, incrementm the transaction id by 1 
# (Hint: declare transaction id as a static variable that initially starts from 0).
class ATM_Transaction(ABC):
    transactionID = 0

    def __init__(self, transactionDate, transactionType, transactionAmount = 0):
        self.transactionDate = transactionDate
        self._transactionType = transactionType        # protected
        self._transactionAmount = transactionAmount    # protected
        ATM_Transaction.transactionID += 1

# accepts the customer's Account object, amount (monetary value) and a transfer account object    
    @abstractmethod
    def update(self, accountFrom, amount, accountTo):
        pass
        

# initializes the transaction's date & time (timestamp) by using one of the datatime functions and transaction type set to 'withdrawal' . 
# The attribute amount is initialized via input parameters.    
class Withdrawal(ATM_Transaction):
    def __init__(self, amount):
        super().__init__(datetime.now(), 'withdrawal', amount)

# function that updates the customer's Account object with the funds to be withdrawn. 
# Returns the status of the transaction.
    def update(self, accountFrom, amount, accountTo):
        return accountFrom.debit(self._transactionAmount)

# accepts an Account object and calls the update() function with the appropriate parameters. 
# Returns the status of the update() function.   
    def withdraw(self, account):
        self.update(account, 0, None)
        
    
  
# constructor that initializes the transaction's date & time (timestamp) 
# by using one of the datatime functions and transaction type set to 'transfer' . 
# The attribute amount via input parameters.
class Transfer(ATM_Transaction):
    def __init__ (self, amount):   
        super().__init__(datetime.now(), 'transfer', amount)

    def update(self, accountFrom, amount, accountTo):
        accountFrom.debit(amount)
        accountTo.credit(amount)
        return True

