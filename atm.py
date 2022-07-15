# represents the Automated Teller Machine itself and has a class called ATM

# need access to the Withdrawal and Transfer classes from the atm_transction.py 
from atm_transaction import Withdrawal, Transfer
from bank import Bank
from additional_exceptions import InvalidATMCard, InvalidAccount

class ATM: 
  # The attribute current card is set to None
  def __init__(self, atmLocation, managedBy):
    self.atmLocation = atmLocation
    self.managedBy = managedBy
    self.__currentCard = None           # Private

    # accessor methods for current card attribute.
  def get_currentCard(self):
    return self.__currentCard 

  def set_currentCard(self, currentCard):
    self.__currentCard = currentCard

# accepts transaction type, amount, account type and transfer account number which has a default value of None via input parameters. 
# 
  def transactions(self, transactionType, amount, accountType, transferAccountNumber = None):
    accountFrom = self.__currentCard.access(accountType)
    if transactionType == "withdrawal":
      withdrawal = Withdrawal(amount)
      return withdrawal.withdraw(accountFrom)
    else:
      transfer = Transfer(amount)
      accountTo = self.managedBy.get_acct(transferAccountNumber)
      if accountFrom.get_accountNumber() == transferAccountNumber:
        raise InvalidAccount
      return transfer.update(accountFrom, amount, accountTo)
    

  # checks if the user has 1 or 2 accounts. Returns True if there is 2 otherwise returns False        
  def check_accts(self):
    listOfAccounts = self.__currentCard.get_accountType()
    if len(listOfAccounts) == 2: 
      return True
    else:
      return False 

  # accepts a user's pin number and checks with the bank if it is valid. Returns status of the check from the bank.  
  def check_pin(self, pin): # input pin
    customer = self.__currentCard.get_ownedBy()
    return self.managedBy.authorize_pin(customer, pin)

  # accepts a ATM card number and checks with the bank if the card is a valid card. 
  # If it is valid, the current card attribute is set to this ATM card object and returns True but if the card is invalid, raise an InvalidATMCard exception.
  def check_card(self, atmCardNumber): # input card number
    atmCards = self.managedBy.atmCards
    for atmCard in atmCards:
      if atmCard.get_atmCardNumber() == atmCardNumber:
        self.__currentCard = atmCard
        return True
    raise InvalidATMCard
  
  # accepts an Account type and returns a string message detailing the current balance of the requested account of that customer.
  def show_balance(self, accountType):
    accountFrom = self.__currentCard.access(accountType)
    latestBalance = accountFrom.check_accountBalance()
    return f"Your {accountType} account has a balance of ${latestBalance:.2f}"







  


    

