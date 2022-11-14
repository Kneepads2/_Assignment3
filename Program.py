import time
#-----------------------------more accessible journal i guess
#ok so does Program inherit all the other classes or does Account do
# What is Account supposed to do??? Nothing is explained about it. I have no idea what its purpose is. Am I supposed to print it so the user can know the details of their account?
#
#TODO figure that out
#class Bnana:
 #def init(self)
 #def poo(self,pay)
 
 #class Hapr:
  #def init(self)
  #def re(self,pay2)
   #self.pay2 =pay2
   #self.tree = Salary(self.pay2)
   
#This is confusing. So ok this is what im doing. 
#  Im going to run showself.mainMenu 
#  then i will type in SEARCH which will take me to the method searchAccount from Bank
#  then i will input an account number which will take me to showAccountMenu
#  BUT the problem is once im at the searchAccount, i cannot go back to showAccountMenu because it belongs to Program
#  #BUT Program is above Bank and Bank is inheriting Program meaning i cannot use showAccountMenu. I could put them in separate modules and import them but that would get rid of the inheritance stuff so..
#  therefore searchAccount is pointless. In the assignment, it says searchAccount and the Select Account are the same thing so im lost

#I was considering adding a feature where after the user does something in an account, it'll ask them if they want to continue making changes to their account or would they like to return to the main menu or leave but not required for the assignment so scrapped it
#--------------------------------------------------

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

#--------------BANK---------------------------------------------------------------        
class Bank(Account):
    
    def __init__(self,_bankName):
        self._bankName = ["Savings Account","Checquing Account","","",""]
        self.name = _bankName
        self.accountMenu = 2
        self.accountName = ""
        self.accountNum = 14


    def openAccount(self):
        print("")

    def searchAccount(self,accountNum):
        self.accountNum = accountNum
        if (self.accountNum == 141):
            self.accountName = "Checquing Account"
            self.ac = Account(141,"Soap",13,6700)
            self.a = 2
            print("Account number verified. Proceeding to Account Menu......\n")
            time.sleep(2)
            #Program.showAccountMenu() 
            #not possible
            return ""


#--------PROGRAM------------------------------------------

class Program(Bank,Account):
    def __init__(self):
        self.balance = [0,0,0,44000,20000]
        self.a = 0
        self.mainMenu = ""
        self.accountMenu = ""
        self.accountNum = 453215
        self.accountName = ""
        self.bank = Bank("Poo")
        self.ac = Account(141,"Soap",13,self.balance[self.a])

    def showMainMenu(self):
        print("\nTo open a new account, type 'OPEN'\nTo enter an existing account, type 'SEARCH'\nTo exit the program, type 'EXIT'\n")
        self.mainMenu = str(input("Enter your desired action: "))
        if (self.mainMenu.upper() == "OPEN"):
            Bank.openAccount()
#------            
        elif (self.mainMenu.upper() == "SEARCH"):
            while True: 
                      try:
                         self.accountNum = int(input('What is the account number of the account you wish to enter?  '))
                         if (self.accountNum == 141 or self.accountNum == 2022 or self.accountNum == 777):
                           print("Account number confirmed. Entering account.....")
                           time.sleep(2)
                           self.bank.searchAccount(self.accountNum)
                           if (self.accountNum == 141):
                            self.ac = Account(141,"Dylan",13,self.balance[self.a])
                            self.a = 0
                           elif (self.accountNum == 2022):
                            self.ac = Account(2022,"Dylan",14,self.balance[self.a]) 
                            self.a = 1
                           elif (self.accountNum == 777):
                            self.a = 2
                            self.ac = Account(777,"Dylan",10,self.balance[self.a]) 
                           self.showAccountMenu()
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
                         if (self.accountNum == 141 or self.accountNum == 2022 or self.accountNum == 777):
                           print("Account number confirmed. Entering account.....")
                           time.sleep(2)
                           self.bank.searchAccount(self.accountNum)
                           if (self.accountNum == 141):
                            self.ac = Account(141,"Dylan",13,self.balance[self.a])
                            self.a = 0
                           elif (self.accountNum == 2022):
                            self.ac = Account(2022,"Dylan",14,self.balance[self.a]) 
                            self.a = 1
                           elif (self.accountNum == 777):
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
           

#---------------Savings Account ---------------------------        
class SavingsAccount(Program,Bank,Account):

    def __init__(self,_minimumBalance):
        self._minimumBalance = _minimumBalance
        self.deposits_Savings = 0
        self.withdraws_Savings = 0

    def withdraw_Savings(self):
        print("")

    def deposit_Savings(self):
        print("")


#------------------- Checquing Account ---------------------------
class ChecquingAccount(Program,Bank,Account):

    def __init__(self,_overdraftAllowed):
        self._overdraftAllowed = _overdraftAllowed

    def withdraw(self):
        print("")


p2 = Program()
print(p2.run())
