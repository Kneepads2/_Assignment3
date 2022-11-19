import time



accountNumberList = [123,777,2022,2013,]
accountNumberListLength = len(accountNumberList)
accountCreated = [1,0,0,0,0]
accountName = ["Dylan","","","",""]
accountROI = [10,10,8,6,4]
accountBalSavings = [10000,0,0,0,0]
accountBalChequing = [10000,0,0,0,0]


class Account:
    a = 0
    def __init__(self,accountNum,accountBal,accountBal2,accountName,accountROI,savings,chequing):
        self.accountNum = accountNum
        self.accountBal = accountBal
        self.accountBal2 = accountBal2
        self.accountName = accountName
        self.accountROI = accountROI
        self.savings = savings
        self.chequing = chequing
    
    def getAccountNumber(self):
        return ""
        
    def getBalance(self):
        return "Current balance in Savings Account: {:.2f}".format(self.accountBal) + " CAD\nCurrent balance in Chequing Account: {:.2f}".format(self.accountBal2) + " CAD"
    
    def getRateOfInterest(self):
        return "Account's rate of interest: "+str(self.accountROI)+ "%"
    
    def deposit(self):
        while True: 
            try:
                amount = float(input('\nHow much money would you like to deposit?  '))
                if (amount <0):
                    print("Cannot deposit negative amounts.")
                    raise ValueError
                    
                elif (amount > 0):
                    time.sleep(2)   
                break
            except ValueError:
                print('Cannot deposit this amount.\n')

        accountType = str(input("Which account are you depositing this money? Savings or Chequing?  "))
        if (accountType.upper() == "SAVINGS"):
            accountBalSavings[self.a] += amount
            print("Balance of Savings account: {:.2f}".format(accountBalSavings[self.a]) + " CAD")

        elif (accountType.upper() == "CHEQUING"):
            accountBalChequing[self.a] += amount
            print("Balance of Savings account: {:.2f}".format(accountBalChequing[self.a]) + " CAD")

        elif (accountType.upper() != "SAVINGS" or accountType.upper() != "CHEQUING"):
            while (accountType.upper() != "SAVINGS" or accountType.upper() != "CHEQUING"):
                accountType = str(input("That is not an option. Are you depositing into SAVINGS or CHEQUING?  "))
                
                if (accountType.upper() == "SAVINGS"):
                    accountBalSavings[self.a] += amount
                    print("Balance of Savings account: {:.2f}".format(accountBalSavings[self.a]) + " CAD")
                    break
                elif (accountType.upper() == "CHEQUING"):
                    accountBalChequing[self.a] += amount
                    print("Balance of Savings account: {:.2f}".format(accountBalChequing[self.a]) + " CAD")
                    break

    def withdraw(self):
        accountType = str(input("Which account are you withdrawing from? Savings or Chequing?  "))
        if (accountType.upper() == "SAVINGS"):
            print(self.savings.withdrawSavings())

        elif (accountType.upper() == "CHEQUING"):
            print(self.chequing.withdrawChequing())

        elif (accountType.upper() != "SAVINGS" or accountType.upper() != "CHEQUING"):
            while (accountType.upper() != "SAVINGS" or accountType.upper() != "CHEQUING"):
                accountType = str(input("That is not an option. Are you depositing into SAVINGS or CHEQUING?  "))
                
                if (accountType.upper() == "SAVINGS"):
                    print(self.savings.withdrawSavings())
                    break
                elif (accountType.upper() == "CHEQUING"):
                    print(self.chequing.withdrawChequing())
                    break
        while True: 
            try:
                amount = float(input('\nHow much money would you like to withdraw?  '))
                if (amount <0):
                    print("Cannot deposit negative amounts.")
                    raise ValueError
                    
                elif (amount > 0):
                    time.sleep(2)   
                break
            except ValueError:
                print('Cannot deposit this amount.\n')
        
        


class SavingsAccount(Account):
    def __init__(self,minimumBalance):
        self.minimumBalance = minimumBalance

    def withdrawSavings(self):
        print("it work")
        
class ChequingAccount(Account):
    def __init__(self,overdraftLimit):
        self.overdrarftLimit = overdraftLimit

    def withdrawChequing(self):
        print("it does mhm")

account1 = Account(123,5000,5000,"Dylan",12,SavingsAccount(5000),ChequingAccount(5000))
account2 = Account(777,0,0,"",5,SavingsAccount(5000),ChequingAccount(5000))
accountList = [account1,account2]
     
class Bank(Account):
    
    def __init__(self,bankNum):
        
        self.bankNum = bankNum
        
        self.accountCreated = accountCreated
        super
        
    def searchAccount(self):
        while (self.a < accountNumberListLength):
            if (self.bankNum == accountNumberList[self.a] and accountCreated[self.a] == 1):
                self.a = 0
                print("Account number verified. Proceeding to account menu....")
                break
            else:
                self.a +=1
            print(self.bankNum)
                
            
        
class Program(Bank,Account):
    def __init__(self):
        
        self.mainMenu = ""
        self.accountVerified = 0
        self.bank = Bank(0)


    def showMainMenu(self):
        print("\n=============================\nTo open a new account, type 'OPEN'\nTo enter an existing account, type 'SEARCH'\nTo exit the program, type 'EXIT'\n")
        self.mainMenu = str(input("Enter your desired action: "))
        if (self.mainMenu.upper() == "OPEN"):
            print("")

#------            
        elif (self.mainMenu.upper() == "SEARCH"):
            while True: 
                      try:
                         self.accountNum = int(input('What is the account number of the account you wish to enter?  '))
                         Bank(self.accountNum).searchAccount()
                         if (accountCreated[self.a]== 1):
                           self.showAccountMenu()
                              
                         else:
                            Bank(self.accountNum).searchAccount()
                            raise ValueError
                             
                           
                         break
                      except ValueError:
                         print('Unknown account number. Please try again.\n')
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
                    
                    break

                elif (self.mainMenu.upper() == "SEARCH"):
                    while True: 
                      try:
                         self.accountNum = int(input('What is the account number of the account you wish to enter?  '))
                         Bank(self.accountNum).searchAccount()
                         if ( accountCreated[self.a]== 1):
                             self.showAccountMenu()  
                         else:
                            Bank(self.accountNum).searchAccount()
                            raise ValueError 

                         break
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
        
        print("\n=========================================\nAccount Holder: Dylan\nAccount number: "+str(accountNumberList[self.a]))
        print("\nTo check your account balance, type 'BALANCE'\nTo deposit funds, type 'DEPOSIT'\nTo withdraw funds, type 'WITHDRAW'\nTo return to the main menu, type 'EXIT'\n")

        self.accountMenu = str(input("Enter your desired action: "))

        if(self.accountMenu.upper() == "DEPOSIT"):
                    accountList[self.a].deposit()
                    time.sleep(3)
                    self.showAccountMenu()

        elif (self.accountMenu.upper() == "WITHDRAW"):
                    
                    accountList[self.a].withdraw()
                    time.sleep(3)
                    self.showAccountMenu()

        elif (self.accountMenu.upper() == "BALANCE"):
                
                    print(accountList[self.a].getBalance())
                    print(accountList[self.a].getRateOfInterest())
                    
                    time.sleep(3)
                    print("Action complete. Returning to account menu...")
                    self.showAccountMenu()

        elif (self.accountMenu.upper() == "EXIT"):
                    print("Returning to main menu....")
                    time.sleep(2)
                    self.showMainMenu()

#--------
        elif (self.accountMenu.upper() != "EXIT" or self.accountMenu.upper() != "WITHDRAW" or self.accountMenu.upper() != "DEPOSIT" or self.accountMenu.upper() != "BALANCE"):
            while (self.accountMenu.upper() != "EXIT" or self.accountMenu.upper() != "WITHDRAW" or self.accountMenu.upper() != "DEPOSIT" or self.accountMenu.upper() != "BALANCE"):
                self.accountMenu = str(input("Not a valid action. Please try again:  "))
                if (self.accountMenu.upper() == "WITHDRAW"):
                
                    Account(accountNumberList[self.a],accountBalSavings[self.a],accountBalChequing[self.a],accountName[self.a],accountROI[self.a],SavingsAccount(5000),ChequingAccount(5000)).withdraw()
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
                    break
        return ""
        
    def run(self):
        p = Program()
        print("\n========================\n\nWelcome to the Official Bank of Dylan")       
        print(p.showMainMenu())

p2 = Program()
print(p2.run())
