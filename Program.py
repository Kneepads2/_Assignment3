import time


accountNumberList = [123,777,2022,2013,141] #a list of my chosen account numbers, the user cannot choose their own account number
accountNumberListLength = len(accountNumberList) - 1 #length of that list
accountCreated = [1,0,0,0,0] #a verification variable. Used to determine if an account using the account numbers has been created
accountName = ["Dylan","","","",""] # a list of names 
accountROI = [10,13,8,6,4] #a list of the ROI for each account
accountBalSavings = [10000,1,0,0,0] #the starting balance of the savings and chequing
accountBalChequing = [10000,0,0,0,0]


class Account:
    a = 0 #a counter variable
    accountType = "" #used to determine if the user wishes to deposit/withdraw from the savings or chequing

    def __init__(self,accountNum,accountBal,accountBal2,accountName,accountROI,savings,chequing):
        self.accountNum = accountNum
        self.accountBal = accountBal
        self.accountBal2 = accountBal2
        self.accountName = accountName
        self.accountROI = accountROI
        self.savings = savings
        self.chequing = chequing
    
    def getAccountName(self): #used in showAccountMenu
        return "Account Holder: "+str(self.accountName)
    
    def getAccountNumber(self): #used in showAccountMenu
        return "Account number: "+str(self.accountNum)
        
    def getBalance(self): #used to display balance of both savings and chequing account
        return "Current balance in Savings Account: {:.2f}".format(self.accountBal) + " CAD\nCurrent balance in Chequing Account: {:.2f}".format(self.accountBal2) + " CAD"
    
    def getRateOfInterest(self): #shown in the 'BALANCE' section
        return "Account's rate of interest: "+str(self.accountROI)+ "%"
    
    def deposit(self): #deposit method
        while True: 
            try:
                amount = float(input('\nHow much money would you like to deposit?  '))
                if (amount <0): #i dont think its possible to deposit negative money in real life
                    print("Cannot deposit negative amounts.")
                    raise ValueError
                    
                elif (amount > 0):
                    time.sleep(2)   
                    break
            except ValueError:
                print('Cannot deposit this amount.\n')
        #all this below determines if the user wants to deposit in their savings or chequing
        self.accountType = str(input("Which account are you depositing this money? Savings or Chequing?  "))
        if (self.accountType.upper() == "SAVINGS"):
            self.accountBal += amount
            print("Balance of Savings account: {:.2f}".format(self.accountBal) + " CAD")

        elif (self.accountType.upper() == "CHEQUING"):
            self.accountBal2 += amount
            print("Balance of Chequing account: {:.2f}".format(self.accountBal2) + " CAD")

        elif (self.accountType.upper() != "SAVINGS" or self.accountType.upper() != "CHEQUING"):
            while (self.accountType.upper() != "SAVINGS" or self.accountType.upper() != "CHEQUING"):
                self.accountType = str(input("That is not an option. Are you depositing into SAVINGS or CHEQUING?  "))
                
                if (self.accountType.upper() == "SAVINGS"):
                    self.accountBal += amount
                    print("Balance of Savings account: {:.2f}".format(self.accountBal) + " CAD")
                    break
                elif (self.accountType.upper() == "CHEQUING"):
                    self.accountBal2 += amount
                    print("Balance of Chequing account: {:.2f}".format(self.accountBal2) + " CAD")
                    break
    #same as deposit                
    def withdraw(self):
        self.accountType = str(input("Which account are you withdrawing from? Savings or Chequing?  "))
        if (self.accountType.upper() == "SAVINGS"):
            while True: 
                try:
                 amount = float(input('\nHow much money would you like to withdraw?  '))
                 if (amount < 0):
                    print("Cannot withdraw negative amounts.")
                    raise ValueError
                
                 elif ((self.accountBal - amount) < self.savings):
                    print("Account balance cannot go below {:.2f}".format(self.savings)+" CAD")
                    raise ValueError
                    
                 else:
                    time.sleep(2)   
                    self.accountBal -= amount
                    print("Balance of Savings account: {:.2f}".format(self.accountBal) + " CAD")
                    break
                except ValueError:
                    print('Cannot withdraw this amount.\n')

        elif (self.accountType.upper() == "CHEQUING"):
            while True: 
                try:
                    amount = float(input('\nHow much money would you like to withdraw?  '))
                    if (amount < 0):
                        print("Cannot withdraw negative amounts.")
                        raise ValueError
                
                    elif ((self.accountBal2 - amount) < (self.chequing + self.accountBal2)):
                        print("Account balance cannot go below {:.2f}".format(0 - self.chequing)+" CAD")
                        raise ValueError
                    
                    else:
                        time.sleep(2)   
                        self.accountBal2 -= amount
                        print("Balance of Chequing account: {:.2f}".format(self.accountBal2) + " CAD")
                        break
                except ValueError:
                    print('Cannot withdraw this amount.\n')

        elif (self.accountType.upper() != "SAVINGS" or self.accountType.upper() != "CHEQUING"):
            while (self.accountType.upper() != "SAVINGS" or self.accountType.upper() != "CHEQUING"):
                self.accountType = str(input("That is not an option. Are you depositing into SAVINGS or CHEQUING?  "))
                
                if (self.accountType.upper() == "SAVINGS"):
                    while True: 
                     try:
                        amount = float(input('\nHow much money would you like to withdraw?  '))
                        if (amount < 0):
                          print("Cannot withdraw negative amounts.")
                          raise ValueError
                
                        elif ((self.accountBal - amount) < self.savings):
                            print("Account balance cannot go below {:.2f}".format(self.savings)+" CAD")
                            raise ValueError
                    
                        else:
                            time.sleep(2)   
                            self.accountBal -= amount
                            print("Balance of Savings account: {:.2f}".format(self.accountBal) + " CAD")
                            break
                     except ValueError:
                        print('Cannot withdraw this amount.\n')
                    break
                    
                elif (self.accountType.upper() == "CHEQUING"):
                    while True: 
                        try:
                            amount = float(input('\nHow much money would you like to withdraw?  '))
                            if (amount < 0):
                                print("Cannot withdraw negative amounts.")
                                raise ValueError
                
                            elif ((accountBalChequing[self.a] - amount) < (self.chequing + accountBalChequing[self.a])):
                                print("Account balance cannot go below {:.2f}".format(0 - self.chequing)+" CAD")
                                raise ValueError
                    
                            else:
                                time.sleep(2)   
                                accountBalChequing[self.a] -= amount
                                print("Balance of Chequing account: {:.2f}".format(self.accountBal2) + " CAD")
                                break
                        except ValueError:
                            print('Cannot withdraw this amount.\n')
                    break
        
class SavingsAccount(Account):
    def __init__(self,minimumBalance):
        self.minimumBalance = minimumBalance

    #withdraws money from savings account
    def withdrawSavings(self):
        while True: 
            try:
                amount = float(input('\nHow much money would you like to withdraw?  '))
                if (amount < 0):
                    print("Cannot withdraw negative amounts.")
                    raise ValueError
                
                elif ((accountBalSavings[self.a] - amount) < self.minimumBalance):
                    print("Account balance cannot go below {:.2f}".format(self.minimumBalance)+" CAD")
                    raise ValueError
                    
                else:
                    time.sleep(2)   
                    accountBalSavings[self.a] -= amount
                    break
            except ValueError:
                print('Cannot withdraw this amount.\n')
        
class ChequingAccount(Account):
    def __init__(self,overdraftLimit):
        self.overdraftLimit = overdraftLimit
    #withdraws cash from chequing account
    def withdrawChequing(self):
        while True: 
            try:
                amount = float(input('\nHow much money would you like to withdraw?  '))
                if (amount < 0):
                    print("Cannot withdraw negative amounts.")
                    raise ValueError
                
                elif ((accountBalChequing[self.a] - amount) < (self.overdraftLimit + accountBalChequing[self.a])):
                    print("Account balance cannot go below {:.2f}".format(0 - self.overdraftLimit)+" CAD")
                    raise ValueError
                    
                else:
                    time.sleep(2)   
                    accountBalChequing[self.a] -= amount
                    break
            except ValueError:
                print('Cannot withdraw this amount.\n')

account1 = Account(accountNumberList[0],accountBalSavings[0],accountBalChequing[0],accountName[0],accountROI[0],5000,5000)
account2 = Account(accountNumberList[1],accountBalSavings[1],accountBalChequing[1],accountName[1],accountROI[1],5000,5000)
account3 = Account(accountNumberList[2],accountBalSavings[2],accountBalChequing[2],accountName[2],accountROI[2],5000,5000)
account4 = Account(accountNumberList[3],accountBalSavings[3],accountBalChequing[3],accountName[3],accountROI[3],5000,5000)
account5 = Account(accountNumberList[4],accountBalSavings[4],accountBalChequing[4],accountName[4],accountROI[4],5000,5000)
accountList = [account1,account2,account3,account4,account5]
#a list of accounts 
     
class Bank(Account):
    i = 0
    def __init__(self,bankNum):
        
        self.bankNum = bankNum
        self.accountCreated = accountCreated
    
    #the open account method. Unfortunately there is an error that I cannot identify
    # It forces self.i back to 0 each time it runs so meaning, you can only make 1 new account, meaning there will be only a total of two active accounts     
    def openAccount(self):
    
        self.i +=1
        print("\n====================\nAccount creation menu\n")
        accountName[self.i] = str(input("Please enter your name: "))
        print("Your account number is "+str(accountNumberList[self.i])+"\n")
        print("Sending you back to the main menu....\n==========================")
        time.sleep(3)
        accountCreated[self.i] = 1
        
        print(self.i)
        

    def searchAccount(self):
        self.a = 0
        while (self.a < accountNumberListLength):
            if (self.bankNum == accountNumberList[self.a] and accountCreated[self.a] == 1):
                print("Account number verified. Proceeding to account menu....")
                break
            else:
                self.a +=1
            
                       
class Program(Bank,Account):
    def __init__(self):
        
        self.mainMenu = "" #used to determine if the user wants to open an account, select an account, or leave
        self.bank = Bank(0) 
        self.accountNum = 0

    #the main menu
    def showMainMenu(self):
        print("\n=============================\nTo open a new account, type 'OPEN'\nTo enter an existing account, type 'SEARCH'\nTo exit the program, type 'EXIT'\n")
        self.mainMenu = str(input("Enter your desired action: "))
        if (self.mainMenu.upper() == "OPEN"):
            if (self.i <4):#this is the limit of how many accounts can be created. Only 4 new accounts can be made
                Bank(self.accountNum).openAccount()
                self.showMainMenu()
            else:
                print("Too many accounts created. Returning to main menu.....")
                self.showMainMenu()

#------            
        elif (self.mainMenu.upper() == "SEARCH"):
            while True: 
                      try:
                         self.accountNum = int(input('What is the account number of the account you wish to enter?  '))
                         Bank(self.accountNum).searchAccount()
                         while (self.a < 4):#this loop will scan through the list until it meets the condition below
                            if (self.accountNum == accountNumberList[self.a] and accountCreated[self.a] == 1):
                                self.showAccountMenu()
                                break   
                                
                            else:
                                self.a +=1
                             
                      except ValueError:
                         print('Unknown account number. Please try again.\n')
                      break  
#-----            
        elif (self.mainMenu.upper() == "EXIT"):
            print("Exiting program.........")
            time.sleep(1.2)
            quit()
#-----
        elif (self.mainMenu.upper() != "OPEN" or self.mainMenu.upper() != "SEARCH" or self.mainMenu.upper() != "EXIT"):
            while (self.mainMenu.upper() != "OPEN" or self.mainMenu.upper() != "SEARCH" or self.mainMenu.upper() != "EXIT"):
                self.mainMenu = str(input("\nThat is not an action. Please enter a valid action: "))
                if (self.mainMenu.upper() == "OPEN"):
                    if (self.i <4):
                        Bank(self.accountNum).openAccount()
                        self.showMainMenu()
                    else:
                        print("Too many accounts created. Returning to main menu.....")
                        self.showMainMenu()
                    break

                elif (self.mainMenu.upper() == "SEARCH"):
                    while True: 
                      try:
                         self.accountNum = int(input('What is the account number of the account you wish to enter?  '))
                         Bank(self.accountNum).searchAccount()
                         while (self.a < 4):
                            if (self.accountNum == accountNumberList[self.a] and accountCreated[self.a] == 1):
                                self.showAccountMenu()
                                break   
                                
                            else:
                                self.a +=1

                      except ValueError:
                         print('Unknown account number. Please try again.\n')
                      break

                elif (self.mainMenu.upper() == "HELP"):
                    print("\nTo open a new account, type 'OPEN'\nTo enter an existing account, type 'SEARCH'\nTo exit the program, type 'EXIT'\n")

                elif (self.mainMenu.upper() == "EXIT"):
                    print("Exiting program.......")
                    time.sleep(1.2)
                    quit()
#-------------------------------------------------------ACCOUNT MENU------------------------------------------------------
    def showAccountMenu(self):
        print("\n=========================================\n"+"Account Holder: "+str(accountName[self.a])+"\n"+str(accountList[self.a].getAccountNumber()))
        print("\nTo check your account balance, type 'BALANCE'\nTo deposit funds, type 'DEPOSIT'\nTo withdraw funds, type 'WITHDRAW'\nTo return to the main menu, type 'EXIT'\n")

        self.accountMenu = str(input("Enter your desired action: "))

        if(self.accountMenu.upper() == "DEPOSIT"):
                    accountList[self.a].deposit() # deposit cash
                    time.sleep(3)
                    self.showAccountMenu()

        elif (self.accountMenu.upper() == "WITHDRAW"):
                    
                    accountList[self.a].withdraw() #withdraw cash
                    time.sleep(3)
                    self.showAccountMenu()

        elif (self.accountMenu.upper() == "BALANCE"):
                
                    print(accountList[self.a].getBalance()) #displays the ROI and balance
                    print(accountList[self.a].getRateOfInterest())
                    
                    time.sleep(3)
                    print("Action complete. Returning to account menu...")
                    self.showAccountMenu()

        elif (self.accountMenu.upper() == "EXIT"):
                    print("Returning to main menu....")
                    time.sleep(2)
                    self.showMainMenu()
                    self.a = 0

#--------
        elif (self.accountMenu.upper() != "EXIT" or self.accountMenu.upper() != "WITHDRAW" or self.accountMenu.upper() != "DEPOSIT" or self.accountMenu.upper() != "BALANCE"):
            while (self.accountMenu.upper() != "EXIT" or self.accountMenu.upper() != "WITHDRAW" or self.accountMenu.upper() != "DEPOSIT" or self.accountMenu.upper() != "BALANCE"):
                self.accountMenu = str(input("Not a valid action. Please try again:  "))
                if (self.accountMenu.upper() == "WITHDRAW"):
                
                    accountList[self.a].withdraw()
                    time.sleep(3)
                    self.showAccountMenu()
                    break
#----
                elif(self.accountMenu.upper() == "DEPOSIT"):
                    accountList[self.a].deposit()
                    time.sleep(3)
                    self.showAccountMenu()
                    break   
#----
                elif (self.accountMenu.upper() == "BALANCE"):
                    print(accountList[self.a].getBalance())
                    print(accountList[self.a].getRateOfInterest())
                    self.showAccountMenu()
                    break
#-----
                elif (self.accountMenu.upper() == "EXIT"):
                    print("Returning to main menu....")
                    time.sleep(2)
                    self.showMainMenu()
                    self.a = 0
                    break
        return ""
        
    def run(self):
        p = Program()
        print("\n========================\n\nWelcome to the Official Bank of Dylan")   # :)    
        print(p.showMainMenu())

p2 = Program()
print(p2.run())
