import time

class Account:
    def __init__(self,accountNum,accountBal,accountName,accountROI,savings,chequing):
        self.accountNum = accountNum
        self.accountBal = accountBal
        self.accountName = accountName
        self.accountROI = accountROI
        self.savings = savings
        self.chequing = chequing
    
    def getAccountNumber(self):
        return ""
        
    def getBalance(self):
        return "Your account balance: "+str(self.accountBal) + " CAD"
    
    def getRateOfInterest(self):
        return "Account's rate of interest: "+str(self.accountROI)+ " %"
    
    def deposit(self):
        amount = int(input("How much would you like to deposit?  "))
        accountType = str(input("Which account are you depositing this money? Savings or Chequing?  "))
        
    
class SavingsAccount:
    def __init__(self,minimumBalance):
        self.minimumBalance = minimumBalance
        
class ChequingAccount:
    def __init__(self,overdraftLimit):
        self.overdrarftLimit = overdraftLimit

account1 = Account(123,5000,"Dylan",12,SavingsAccount(5000),ChequingAccount(5000))
accountList = [account1]
accountListLength = len(accountList)

     
class Bank(Account):
    def __init__(self,bankNum):
        self.a = 0
        self.bankNum = bankNum
        
    def searchAccount(self):
        while (self.a < accountListLength):
            if (self.bankNum != accountList[self.a]):
                self.accountVerified = 1
                self.a += 1
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
                         if (self.accountVerified == 1):
                           self.showAccountMenu()    
                           
                         else:
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
                         self.bank.searchAccount()
                         if (self.accountVerified == 1):
                             self.showAccountMenu()  
                         else:
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
    def showAccountMenu(self):
        print("bababooey")
        
    def run(self):
        p = Program()
        print("\n\nWelcome to the Official Bank of Dylan")       
        print(p.showMainMenu())

p2 = Program()
print(p2.run())
