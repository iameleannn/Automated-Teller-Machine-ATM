# Automated-Teller-Machine-ATM

## Overview
This project is to simulate a scaled down version of an Automated Teller Machine (ATM) by using Object Orientation Principles (OOP) and their implementation in Python. VS Code is used for prefered IDE. 

![istockphoto-1072288242-612x612-1](https://user-images.githubusercontent.com/70336265/179187114-7304f6b8-c0f5-4b10-92bd-049115e13bde.jpeg)


# Limitations are placed in this scenerio. 

* Bank XYZ maintains many ATMs. Each ATM can only perform 4 operations: Check balance, Withdrawals, Transfers and Quit.
* ATM transactions can only start when the user's PIN is entered correctly. If the PIN is invalid, the card is returned.
* Each bank can has only 1 type of ATM card and each ATM card has access to both a customer's Savings and Current account (if any).
* Each customer of the bank by default has a savings account.
* Customers of Bank XYZ are allowed to own only 1 ATM card.
* Withdrawals operations are done either from the customer's Savings or Current account.
* Transfers operations are done either from Savings to Current account and vice versa from the same customer or from an account of Customer A to an account of Customer B (both customers must be account holders of Bank XYZ).
* Transfer transactions must not go through if the transfer account number is not existent or transferee has insufficient funds for transfer.


# Assumptions for Testing

1. Each customer object has either a Savings or Current account or both from when they personally opened the accounts at the physical bank.
2. There is only 1 bank and 1 Automated Teller Machine for testing to keep the scale small. All other objects such as customer, ATM cards and accounts are allowed to have multiples.
3. Each customer can only own 1 ATM card. 


# Scripts
*  additional_exceptions.py
*  customer.py
*  account.py
*  bank.py
*  atm_card.py
*  atm_transaction.py
*  atm.py
*  main_app.py
