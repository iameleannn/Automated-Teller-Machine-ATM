from additional_exceptions import InvalidATMCard, InvalidPinNumber, AccountNotFound, InsufficientFunds, InvalidAccount

# Part 1 - The ATM itself (simulation menu)

def atm_app(atm): # that accepts an ATM object 
  while True:
    print("\nAvaliable options: \n1. Insert ATM card \n2. Quit Simulation")
    option = input("Enter an option: ")
    if option == '2': 
      print("Bye bye!\n")
      break 

    # allows the user to enter an ATM card number. 
    # If the ATM card number and pin number is valid, it moves on to the ATM Menu (part 2) otherwise it must show a message indicating which is invalid (either the card or the pin).  
    elif option == '1':
      try: 
        atmCardNumber = input("Enter a ATM card number: ")
        atm.check_card(atmCardNumber)
        atmPinInput = input("Enter a Pin Number: ")
        atm.check_pin(atmPinInput)

      except InvalidATMCard: 
        print("Invalid Card. Please take your card. \n")
      except InvalidPinNumber:
        print("Invalid pin. Please take your card.  \n")
      else: 
        atm_menu_sys(atm)



  
# Part 2 - ATM Menu
def atm_menu_sys(atm): # accepts the same ATM object as in part 1 
  while True: 
    print("\nAvaliable options: \n1. Check balance \n2. Withdraw Funds \n3. Transfer Funds \n4. Return Card")
    option = input("Enter a transaction option: ")

    if option == '1':  # check balance
      print("\nChoose Account: ")
      print("1. Current Account \n2. Savings Account")
      inputOption = input("Enter an account option: ")
      if inputOption == '1': 
        balanceStatement = atm.show_balance("savings") 
        print(balanceStatement)
      elif inputOption == '2':
        balanceStatement = atm.show_balance("current") 
        print(balanceStatement)
      else: 
        print("Input unknown.\n")
    
  
    elif option == '2': # withdrawal
      print("\nChoose Account: ")
      print("1. Current Account \n2. Savings Account")
      accountOption = input("Enter an account option: ")

      for i in range(3): 
        try: 
          
          accountWithdrawal = float(input("Enter an amount to withdraw: $"))

          if accountOption == '1':      # Current Account
            atm.transactions("withdrawal", accountWithdrawal, "current")
            print("Card Returned")
            accountWithdrawalBalance = atm.show_balance("current") 
            print(accountWithdrawalBalance)
            print()
            return
          elif accountOption == '2':    # Savings Account
            atm.transactions("withdrawal", accountWithdrawal, "savings")
            print("Card Returned")
            accountWithdrawalBalance = atm.show_balance("savings") 
            print(accountWithdrawalBalance)
            print()

            return
        except InsufficientFunds: 
          print("Funds insufficient. Please check funds available.\n")
          break
        except ValueError: 
          print("Value Error. Please enter positive numbers with maximum 2 decimal places.\n")
      
      
      
    elif option == '3': # transfer
      print("\nChoose Account: ")
      print("1. Current Account \n2. Savings Account")
      transferAccountOption = input("Enter an account option: ")
      
      for i in range(3):
        try: 
          transferAccountNumber = input("Enter the account number to transfer funds to: ")
          transferAccountAmount = float(input("Enter the amount to transfer: $"))
          
          if transferAccountOption == '1': # Current Account
            atm.transactions("transfer", transferAccountAmount, "current", transferAccountNumber)
            print("Card Returned")
            accountTransferredBalance = atm.show_balance("current") 
            print(accountTransferredBalance)
            return
          elif transferAccountOption == '2':  # Savings Account
            atm.transactions("transfer", transferAccountAmount, "savings", transferAccountNumber)
            print("Card Returned")
            accountTransferredBalance = atm.show_balance("savings") 
            print(accountTransferredBalance)
            return 
        except InvalidAccount: 
          print("Wrong account. Please check account input. \n")
          
        except AccountNotFound: 
          print("Wrong account. Please check account input.\n")
          
        except InsufficientFunds: 
          print("Funds insufficient. Please check funds available.\n")
          break 

        except ValueError: 
          print("Value Error. Please enter positive numbers with maximum 2 decimal places.\n")
          
        
    
    elif option == '4' :    # Return Card
      print("Card returned\n")
      return 
