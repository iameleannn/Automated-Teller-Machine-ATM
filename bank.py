import random
from customer import Customer
from additional_exceptions import InvalidPinNumber, AccountNotFound
 

class Bank:
    def __init__(self, bankCode, bankAddress):
        self.__bankCode = bankCode
        self.__bankAddress = bankAddress
        self.atms = []            # list
        self.customers = []       # list
        self.atmCards = []        # list
        self.customerMap = {}     # dict
        self.pinNumberMap = {}    # dict

    
# the bank must be able to add a Customer object and their pin number.
# Each customer's record is stored as a dictionary {} consisting of the keys listed below. Each customer's record must be stored in the list of customers. 
# How you name your keys is up to you. a unique customer id that is a combination of the customer's name and a random string of 4 digit numbers. 
# Eg: Tom4851
# the customer object
# the customer pin number
    def add_customer(self, customer, pinNumber):
        uniqueID = customer.get_id()
        self.customerMap[uniqueID] = customer
        self.customers.append(customer)
        self.pinNumberMap[uniqueID] = pinNumber
        

# accepts an atmCard object and stores it in the list of atm cards.
    def manages(self, atm_cards):
        self.atmCards.append(atm_cards)

# accepts an ATM object and stores it in the list of ATMs.
    def maintains(self, ATM):
        self.atms.append(ATM)


# accepts a customer's object and pin number as input parameters,
# checks that the customer's pin number is valid. Returns a True if the pin number is valid
# otherwise raises a InvalidPinNumber exception.
    def authorize_pin(self, customer, customerPin):
        uniqueID = customer.get_id()
        if self.pinNumberMap[uniqueID] == customerPin:
            return True
        else:
            raise InvalidPinNumber           
            

# accepts an account number as input parameter and check if the account
# number is valid. Returns an Account object if the account number is valid otherwise raises a
# AccountNotFound exception.
    def get_acct(self, accountNumber):
        for customer in self.customers:
            accounts = customer.get_accounts()
            for account in accounts:
                if account.get_accountNumber() == accountNumber:
                    return account
                else:
                    raise AccountNotFound

                    
                    
            