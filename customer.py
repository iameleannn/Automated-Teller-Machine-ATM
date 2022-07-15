# customer.py (10 marks)
# This script represents the Customer object therefore it has class called Customer and its properties are:
# Attributes:
# They are all private variables
# name - customer's name
# address - customer's address
# date of birth - customer's date of birth in datetime format (DD-MMM-YYYY)
# list of accounts - a list of accounts a customer can have, maximum is 2. Savings and/or
# Current account/s.
# Methods:
# __init()__ - constructor that initializes the customer's name, address and date of birth
# from input parameters and leave the lists as empty lists.
# owns() - accepts an Account object and adds it to the list.
# __str__() - returns string representation of the Customer object detailing the name,
# address and date of birth.
# getters for name and list of accounts

import random
from datetime import datetime
# to change date time from string to datetime format
# %b - month in mmm,  %d - day, %Y - year 

class Customer:
    def __init__(self, name, address, dob):  # all 4 attributes are private
        self.__name = name
        self.__address = address
        self.__dob = datetime.strptime(dob,'%d-%b-%Y' ) # dob means date of birth
        self.__accounts = []     # list of accounts
        randomDigits = random.randrange(0, 9999)
        self.__id = name + "{:04d}".format(randomDigits)
     
        
 # accepts an Account object and adds it to the list.
    def owns(self, account)   : 
        self.__accounts.append(account)
            
    
     # returns string representation of the Customer object detailing the name,
     # address and date of birth.
    def __str__(self): 
      return f"Name: {self.__name}\nAddress: {self.__address}\nDate Of Birth: {self.__dob.strftime('%d-%b-%Y')}"
  
    # getters for name and list of accounts
    def get_name(self):
        return self.__name
    
    def get_accounts(self):
        return self.__accounts

    def get_id(self):
        return self.__id