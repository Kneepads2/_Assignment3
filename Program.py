import time

#

#----------------------Acount---------------------------------

class Account():
    def __init__(self,_accountNumber,_accountHolderName,_rateOfInterest,_currentBalance):
        self.accountNumber = _accountNumber
        self.accountHolderName = _accountHolderName
        self.rateOfInterest = _rateOfInterest
        self.currentBalance = _currentBalance
        self.deposits = 0
        self.withdraws = 0
        

    def getAccountNumber(self): #Nothing in the assignment says the user decides the account number so im going to decide it
        return "Account Number: "+str(self.accountNumber)

    def getAccountHolderName(self):
        return "Account Holder: "+str(self.accountHolderName)

    def getRateOfInterest(self):
        return "The rate of interest: "+str(self.rateOfInterest)+ "%"

    def getCurrentBalance(self):
        return "Your account balance: {:.2f}".format(self.currentBalance)+" CAD"

    def withdraw(self):
        while True: 
            try:
                self.withdraws = float(input('\nHow much money would you like to withdraw?  '))
                if (self.deposits <0 or (self.currentBalance - self.withdraws) < 0):
                    raise ValueError
                elif (self.withdraws > 0):
                    time.sleep(2) 
                    print("Withdrawal confirmed.....")
                    self.currentBalance -=self.withdraws
                    print("Your new balance is: "+str(self.currentBalance)+" CAD")
                    print("Action complete. Returning to account menu...")
        
                break
            except ValueError:
                print('Not a valid value.\n')

    def deposit(self):
        while True: 
            try:
                self.deposits = float(input('\nHow much money would you like to deposit?  '))
                if (self.deposits <0):
                    print("Please enter a number above zero.")
                    raise ValueError
                    
                elif (self.deposits > 0):
                    time.sleep(2) 
                    print("Deposit confirmed.....")
                    self.currentBalance +=self.deposits
                    print("Your new balance is: "+str(self.currentBalance)+" CAD")
                    print("Action complete. Returning to account menu...\n")
                    
                break
            except ValueError:
                print('Not a valid value. Amount might be below zero or you\'re requesting to withdraw more than you have.\n')

#---------------Savings Account ---------------------------        

class SavingsAccount(Account):

    def __init__(self,_minimumBalance,_currentBalance):
        self._minimumBalance = _minimumBalance
        
        
        self.deposits_Savings = 0
        self.withdraws_Savings = 0

    def withdraw_Savings(self):
        print("")

    def deposit_Savings(self):
        print("")


#------------------- Checquing Account ---------------------------
class ChecquingAccount(Account):

    def __init__(self,_overdraftAllowed):
        self._overdraftAllowed = _overdraftAllowed

    def withdraw(self):
        print("")

#--------------BANK---------------------------------------------------------------        
class Bank(SavingsAccount,ChecquingAccount,Account):
    
    def __init__(self,_bankName):
        self._bankName = ["Savings Account","Checquing Account","","",""]
        self.name = _bankName
        
        self.accountMenu = 2
        self.accountName = ""
        self.accountNum = 14
        self.accountNumberList = [141,2022,777,2013,2077]
        self.accountVerification = [0,0,0]
        self.i = 0
        self.a = 0
        self.holderName = ["","",""]
        self.accountType = ""
        self.accounts = [SavingsAccount(5000,44000)]




    def openAccount(self):
        print("-----------------------------\nAccount creation menu\n")
        self.holderName[self.i] = str(input("Please enter your name: "))
        print("Your account number is "+str(self.accountNumberList[self.i])+"\n")
        time.sleep(3)
        print("Sending you back to the main menu....\n------------------------------------")
        self.accountVerification[self.i] = 1
        self.i +=1


    def searchAccount(self,accountNum):
        self.accountNum = accountNum
        if (self.accountNum == 141):
            self.accountName = "Checquing Account"
            self.a = 2
            print("Account number verified. Proceeding to Account Menu......\n")
            time.sleep(2)
            #Program.showAccountMenu() 
            #not possible
            return ""

#--------PROGRAM------------------------------------------

class Program(Bank):
    def __init__(self):
        self.balance = [0,0,0,44000,20000]
        self.mainMenu = ""
        self.accountMenu = ""
        self.accountNum = 0
        self.accountName = ""
        self.accountVerification = [0,0,0]
        self.bank = Bank("")
        self.a = 0
        
        self.ac = Account(141,"Soap",13,self.balance[self.a])
        super(Program,self).__init__()

    def showMainMenu(self):
        print(self.i)
        print("\nTo open a new account, type 'OPEN'\nTo enter an existing account, type 'SEARCH'\nTo exit the program, type 'EXIT'\n")
        self.mainMenu = str(input("Enter your desired action: "))
        if (self.mainMenu.upper() == "OPEN"):
            if (self.i == 2):
                self.showMainMenu()
                print("You cannot have more than five accounts. Please try another action.")
            else:
                self.bank.openAccount()
                self.showMainMenu()
                self.accountVerification[self.i] = 1
                self.i +=1

#------            
        elif (self.mainMenu.upper() == "SEARCH"):
            while True: 
                      try:
                         self.accountNum = int(input('What is the account number of the account you wish to enter?  '))
                         if ((self.accountNum == 141 and self.accountVerification[self.i] == 1) or (self.accountNum == 2022 and self.accountVerification[self.i] == 1) or (self.accountNum == 777 and self.accountVerification[self.i] == 1) or self.accountNum == 2013 or self.accountNum == 2077):
                           print("Account number confirmed. Entering account.....")
                           time.sleep(2)
                           self.bank.searchAccount(self.accountNum)
                           if (self.accountNum == 141 and self.accountVerification[self.i] == 1):
                            self.a = 0
                            self.ac = Account(141,"Dylan",13,self.balance[self.a])
                            
                            self.showAccountMenu()
                           elif (self.accountNum == 2022 and self.accountVerification[self.i] == 1):
                            self.a = 1
                            self.ac = Account(2022,"Dylan",14,self.balance[self.a]) 
                            self.showAccountMenu()
                           elif (self.accountNum == 777 and self.accountVerification[self.i] == 1):
                            self.a = 2
                            self.ac = Account(777,"Dylan",10,self.balance[self.a]) 
                            self.showAccountMenu()
                           elif (self.accountNum == 2013):
                            self.a = 3 
                            self.ac = SavingsAccount(self.balance[self.a])
                            
                           
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
                    if (self.i == 2):
                        self.showMainMenu
                        print("You cannot have more than five accounts. Please try another action.")
                    else:
                        self.bank.openAccount()
                        self.showMainMenu
                        self.i += 1
                    break

                elif (self.mainMenu.upper() == "SEARCH"):
                    while True: 
                      try:
                         self.accountNum = int(input('What is the account number of the account you wish to enter?  '))
                         if (self.accountNum == 141 or self.accountNum == 2022 or self.accountNum == 777):
                           print("Account number confirmed. Entering account.....")
                           time.sleep(2)
                           self.bank.searchAccount(self.accountNum)
                           if (self.accountNum == 141 and self.accountVerification[self.i] == 1):
                            self.ac = Account(141,"Dylan",13,self.balance[self.a])
                            self.a = 0
                            self.showAccountMenu
                           elif (self.accountNum == 2022 and self.accountVerification[self.i] == 1):
                            self.ac = Account(2022,"Dylan",14,self.balance[self.a]) 
                            self.a = 1
                            self.showAccountMenu
                           elif (self.accountNum == 777 and self.accountVerification[self.i] == 1):
                            self.a = 2
                            self.ac = Account(777,"Dylan",10,self.balance[self.a]) 
                            self.showAccountMenu()
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
 #-----   ------------------------            
    def showAccountMenu(self):

        print("\n=========================================\n"+str(self.ac.getAccountHolderName())+"\n"+str(self.ac.getAccountNumber()))
        print("\nTo check your account balance, type 'BALANCE'\nTo deposit funds, type 'DEPOSIT'\nTo withdraw funds, type 'WITHDRAW'\nTo return to the main menu, type 'EXIT'\n")

        self.accountMenu = str(input("Enter your desired action: "))

        if(self.accountMenu.upper() == "DEPOSIT"):
                    self.ac.deposit()
                    time.sleep(3)
                    self.showAccountMenu()

        elif (self.accountMenu.upper() == "WITHDRAW"):
                    self.ac.withdraw()
                    time.sleep(3)
                    self.showAccountMenu()

        elif (self.accountMenu.upper() == "BALANCE"):
                    print(self.ac.getCurrentBalance())
                    print(self.ac.getRateOfInterest())
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
                    time.sleep(3)
                    self.showAccountMenu()
                    self.ac.withdraw()
                    break
#----
                elif(self.accountMenu.upper() == "DEPOSIT"):
                    self.ac.deposit()
                    time.sleep(3)
                    self.showAccountMenu()
                    break
                    
#----
                elif (self.accountMenu.upper() == "BALANCE"):
                    print(self.ac.getCurrentBalance())
                    print(self.ac.getRateOfInterest())
                    time.sleep(3)
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
               
        print(p.showMainMenu())
            
        return ""
           



p2 = Program()
print(p2.run())
