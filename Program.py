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
#--------------------------------------------------

#----------------------Acount---------------------------------

class Account():
    def __init__(self,_accountNumber,_accountHolderName,_rateOfInterest,_currentBalance):
        self.accountNumber = _accountNumber
        self.accountHolderName = _accountHolderName
        self.rateOfInterest = _rateOfInterest
        self.currentBalance = _currentBalance

    def getAccountNumber(self): #Nothing in the assignment says the user decides the account number so im going to decide it
        return self.accountNumber

    def getAccountHolderName(self):
        return self.accountHolderName

    def getRateOfInterest(self):
        return str(self.rateOfInterest)+ "%"

    def getCurrentBalance(self):
        return str(self.currentBalance)+" CAD"

    def disposit(self):
        print("")

    def withdraw(self):
        print("")

#--------------BANK---------------------------------------------------------------        
class Bank(Account):
    
    def __init__(self,_bankName):
        self._bankName = ["Savings Account","Checquing Account","","",""]
        self.name = _bankName
        self.accountMenu = 2
        self.accountName = ""
        print(self.name)


    def openAccount(self):
        print("")

    def searchAccount(self,accountNum):
        
        if (accountNum == 141):
            self.accountName = "Checquing Account"
            self.a = 2
            print("Account number verified. Proceeding to Account Menu......")
            time.sleep(2)
            #Program.showAccountMenu() 
            #not possible


#--------PROGRAM------------------------------------------

class Program(Bank):
    def __init__(self):
        self.balance = [6000,7000,0,0,0]
        self.a = 0
        self.mainMenu = ""
        self.accountNum = 453215
        self.bank = Bank("Poo")

    def showMainMenu(self):
        print("\nTo open a new account, type 'OPEN'\nTo enter an existing account, type 'SEARCH'\nTo exit the program, type 'EXIT'\n")
        self.mainMenu = str(input("Enter your desired action: "))
        if (self.mainMenu.upper() == "OPEN"):
            Bank.openAccount()
            
        elif (self.mainMenu.upper() == "SEARCH"):
            while True: 
                      try:
                         self.accountNum = int(input('What is the account number of the account you wish to enter?  '))
                         if (self.accountNum == 141 or self.accountNum == 2022 or self.accountNum == 777):
                           print("Account number confirmed. Entering account.....")
                           time.sleep(2)
                           self.bank.searchAccount(self.accountNum)
                         break
                      except ValueError:
                         print('Unknown account number. Please try again.\n')
            
        elif (self.mainMenu.upper() == "EXIT"):
            print("Exiting program.........")
            time.sleep(1.2)
            quit()

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

        print("\nWelcome to your "+str(self.accountName))
        print("\nTo check your account balance, type 'BALANCE'\nTo deposit funds, type 'DEPOSIT'\nTo withdraw funds, type 'WITHDRAW'\nTo return to the main menu, type 'EXIT'\n")

        self.accountMenu = str(input("Enter your desired action: "))
        if (self.accountMenu.upper() != "EXIT" or self.accountMenu.upper() != "WITHDRAW" or self.accountMenu.upper() != "DEPOSIT" or self.accountMenu.upper() != "BALANCE"):
            while (self.accountMenu.upper() != "EXIT" or self.accountMenu.upper() != "WITHDRAW" or self.accountMenu.upper() != "DEPOSIT" or self.accountMenu.upper() != "BALANCE"):
                if (self.accountMenu.upper() == "WITHDRAW"):
                    while True: 
                      try:
                         withdraws = int(input('What is the account number of the account you wish to enter?  '))
                         if (withdraws <0):
                           time.sleep(2) 
                           print("Withdrawal confirmed.....")
                           self.balance[self.a] -=withdraws
                         break
                      except ValueError:
                         print('Not a valid value.\n')
                    break
#----
                elif(self.accountMenu.upper() == "DEPOSIT"):
                    print("")
                    break
#----
                elif (self.accountMenu.upper() == "BALANCE"):
                    print("Your account balance: "+self.balance[self.a])
                    while True:
                        self._action = str(input("\nAction complete. Would you like to continue interacting with your account? "))
                        if (self._action.upper() not in ('YES','Y','N','NO')):
                            print("Please enter 'YES' or 'NO'")
                        else:
                            break
                    if (self._action.upper() == "Y" or self._action.upper() == "YES"):
                        break
                    else:
                        

                elif (self.accountMenu.upper() == "EXIT"):
                    print("Returning to main menu....")
                    time.sleep(2)
                    self.showMainMenu()


    def run(self):
        p = Program()
        while True:
            if (self.mainMenu.upper() == "EXIT" ):
                print("Exiting program.......")
                time.sleep(1.2)
                quit()
                
            print(p.showMainMenu())
            if (self.mainMenu.upper() == "SEARCH"):
                print(p.showAccountMenu())
            if (self._action.upper() == "Y" or self._action.upper() == "YES" ):
                print(p.showAccountMenu)

#---------------Savings Account ---------------------------        
class SavingsAccount(Account):

    def __init__(self,_minimumBalance):
        self._minimumBalance = _minimumBalance

    def withdraw(self):
        print("")
#------------------- Checquing Account ---------------------------
class ChecquingAccount(Account):

    def __init__(self,_overdraftAllowed):
        self._overdraftAllowed = _overdraftAllowed

    def withdraw(self):
        print("")


p2 = Program()
print(p2.run())
