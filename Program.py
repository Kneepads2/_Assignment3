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

# i realize that i couldve added the saving and checquing accounts into Account but then what would be the point of the ChecuqingAccount and SavingsAccount? It could just for initializing but theres no point then
#I was considering adding a feature where after the user does something in an account, it'll ask them if they want to continue making changes to their account or would they like to return to the main menu or leave but not required for the assignment so scrapped it
#--------------------------------------------------

#----------------------Account---------------------------------

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
                if (self.withdraws <0 or (self.currentBalance - self.withdraws) < 0):
                    raise ValueError
                elif (self.withdraws > 0):
                    time.sleep(2) 
                    print("Withdrawal confirmed.....")
                    self.currentBalance -=self.withdraws
                    print("Your new balance is: "+str(self.currentBalance)+" CAD")
                    print("Action complete. Returning to account menu...")
        
                break
            except ValueError:
                print('Cannot withdraw this amount.\n')

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
                print('Cannot deposit this amount.\n')

#---------------Savings Account ---------------------------        

class SavingsAccount(Account):

    def __init__(self,_minimumBalance,_accountNumSaving,currentBalSaving):
        self._minimumBalance = _minimumBalance
        self.currentBalSaving = currentBalSaving
        
        
        self.deposits_Savings = 0
        self.withdraws_Savings = 0
    

    def withdraw_Savings(self):
        while True: 
            try:
                self.withdraws_Savings = float(input('\nHow much money would you like to withdraw?  '))
                if (self.withdraws_Savings <0 or (self.currentBalSaving - self.withdraws_Savings) < self._minimumBalance):
                    print("Account balance must always remain above 5000 CAD.")
                    raise ValueError
                elif (self.withdraws_Savings > 0):
                    time.sleep(2) 
                    print("Withdrawal confirmed.....")
                    self.currentBalSaving -=self.withdraws_Savings
                    print("Your new balance is: "+str(self.currentBalSaving)+" CAD")
                    print("Action complete. Returning to account menu...")
        
                break
            except ValueError:
                print('Cannot withdraw this amount. \n')
        

    def deposit_Savings(self):
        while True: 
            try:
                self.deposits_Savings = float(input('\nHow much money would you like to deposit?  '))
                if (self.deposits_Savings <0):
                    print("Please enter a number above zero.")
                    raise ValueError
                    
                elif (self.deposits_Savings > 0):
                    time.sleep(2) 
                    print("Deposit confirmed.....")
                    self.currentBalance +=self.deposits_Savings
                    print("Your new balance is: "+str(self.currentBalance)+" CAD")
                    print("Action complete. Returning to account menu...\n")
                    
                break
            except ValueError:
                print('Cannot withdraw this amount.\n')


#------------------- Checquing Account ---------------------------
class ChecquingAccount(Account):

    def __init__(self,_overdraftAllowed,_accountNumChecque,_accountBalChecque):
        self._overdraftAllowed = _overdraftAllowed
        self.deposits_Checque = 0
        self.accountBalCheque = _accountBalChecque
        self.withdraws_Checque = 0

    def withdraw_Checque(self):
        while True: 
            try:
                self.withdraws_Checque = float(input('\nHow much money would you like to withdraw?  '))
                if (self.withdraws_Checque <0 or (self.accountBalCheque - self.withdraws_Checque) < self._overdraftAllowed):
                    raise ValueError
                elif (self.withdraws_Checque > 0):
                    time.sleep(2) 
                    print("Withdrawal confirmed.....")
                    self.accountBalCheque -=self.withdraws_Checque
                    print("Your new balance is: "+str(self.accountBalCheque)+" CAD")
                    print("Action complete. Returning to account menu...")
        
                break
            except ValueError:
                print('Cannot withdraw this amount. \n')
    
    def deposit_Checque(self):
        while True: 
            try:
                self.deposits_Checque = float(input('\nHow much money would you like to deposit?  '))
                if (self.deposits_Checque <0):
                    print("Please enter a number above zero.")
                    raise ValueError
                    
                elif (self.deposits_Checque > 0):
                    time.sleep(2) 
                    print("Deposit confirmed.....")
                    self.accountBalCheque +=self.deposits_Checque
                    print("Your new balance is: "+str(self.accountBalCheque)+" CAD")
                    print("Action complete. Returning to account menu...\n")
                    
                break
            except ValueError:
                print('Cannot deposit this amount.\n')

#--------------BANK---------------------------------------------------------------        
class Bank(SavingsAccount,ChecquingAccount,Account):
    
    def __init__(self,a,i):
        self._bankName = ["Savings Account","Checquing Account","","",""]
        
        self.accountMenu = 2
        self.accountName = "Dylan"
        self.accountNum = 14
        self.accountNumberList = [141,2022,777,2013,2077]
        self.accountROI = [13,14,10,11,12]

        self.accountVerification = [0,0,0]
        self.i = i
        self.a = a
        self.holderName = ["","",""]
        self.accountType = ""
        self.accounts = [SavingsAccount(5000,44000,"Dylan")]




    def openAccount(self):
        print("\n====================\nAccount creation menu\n")
        self.holderName[self.i] = str(input("Please enter your name: "))
        print("Your account number is "+str(self.accountNumberList[self.i])+"\n")
        time.sleep(3)
        print("Sending you back to the main menu....\n==========================")
        self.accountVerification[self.i] = 1
        self.i +=1


    def searchAccount(self,accountNum):
        self.accountNum = accountNum
        if (self.accountNum == 141):
            self.accountName = "Checquing Account"
            self.a = 0
            print("Account number verified. Proceeding to Account Menu......\n")
            time.sleep(2)
            #Program.showAccountMenu() 
            #not possible
            return ""

#--------PROGRAM------------------------------------------

class Program(Bank,SavingsAccount,ChecquingAccount):
    def __init__(self,a,i):
        self.balance = [0,0,0,44000,20000]
        self.mainMenu = ""
        self.accountMenu = ""
        self.accountNum = 0
        self.accountName = ""
        self.accountVerification = [0,0,0]
        self.bank = Bank(0,0)
        

        Bank.__init__(self,a,i)
        self.ac = Account(141,"Dylan",13,self.balance[self.a])

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
                         if (self.accountNum == 141  or self.accountNum == 2022  or self.accountNum == 777  or self.accountNum == 2013 or self.accountNum == 2077):
                           print("Account number confirmed. Entering account.....")
                           time.sleep(2)
                           self.bank.searchAccount(self.accountNum)
                           if (self.accountNum == 141):
                            self.a = 0
                            self.ac = Account(141,"Dylan",13,self.balance[self.a])
                            self.showAccountMenu()

                           elif (self.accountNum == 2022):
                            self.a = 1
                            self.ac = Account(2022,"Dylan",14,self.balance[self.a]) 
                            self.showAccountMenu()

                           elif (self.accountNum == 777):
                            self.a = 2
                            self.ac = Account(777,"Dylan",10,self.balance[self.a]) 
                            self.showAccountMenu()

                           elif (self.accountNum == 2013):
                            self.a = 3 
                            self.ac = SavingsAccount(5000,self.accountNumberList[self.a],self.balance[self.a])
                            self.showAccountMenu()

                           elif (self.accountNum == 2077):
                            self.a = 4 
                            self.ac = ChecquingAccount(-5000,self.accountNumberList[self.a],self.balance[self.a])
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
                         if (self.accountNum == 141 or self.accountNum == 2022 or self.accountNum == 777 or self.accountNum == 2013 or self.accountNum == 2077):
                           print("Account number confirmed. Entering account.....")
                           time.sleep(2)
                           self.bank.searchAccount(self.accountNum)
                           if (self.accountNum == 141):
                            self.a = 0
                            self.ac = Account(141,"Dylan",13,self.balance[self.a])
                            self.showAccountMenu()
                           elif (self.accountNum == 2022):
                            self.a = 1
                            self.ac = Account(2022,"Dylan",14,self.balance[self.a]) 
                            self.showAccountMenu()
                           elif (self.accountNum == 777):
                            self.a = 2
                            self.ac = Account(777,"Dylan",10,self.balance[self.a]) 
                            self.showAccountMenu()
                           elif (self.accountNum == 2013):
                            self.a = 3 
                            self.ac = SavingsAccount(5000,self.accountNumberList[self.a],self.balance[self.a])
                            self.showAccountMenu()
                           elif (self.accountNum == 2077):
                            self.a = 4 
                            self.ac = ChecquingAccount(-5000,self.accountNumberList[self.a],self.balance[self.a])
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
 #-----   ------------------------            
    def showAccountMenu(self):

        print("\n=========================================\nAccount Holder: Dylan\nAccount number: "+str(self.accountNumberList[self.a]))
        print("\nTo check your account balance, type 'BALANCE'\nTo deposit funds, type 'DEPOSIT'\nTo withdraw funds, type 'WITHDRAW'\nTo return to the main menu, type 'EXIT'\n")

        self.accountMenu = str(input("Enter your desired action: "))

        if(self.accountMenu.upper() == "DEPOSIT"):
                    if (self.accountNum == 2013):
                        self.ac.deposit_Savings()
                        time.sleep(3)
                        self.showAccountMenu()
                    elif (self.accountNum == 2077):
                        self.ac.deposit_Checque()
                        time.sleep(3)
                        self.showAccountMenu
                    else:
                        self.ac.deposit()
                        time.sleep(3)
                        self.showAccountMenu()

        elif (self.accountMenu.upper() == "WITHDRAW"):
                    if (self.accountNum == 2013):
                        self.ac.withdraw_Savings()
                        time.sleep(3)
                        self.showAccountMenu()
                    elif (self.accountNum == 2077):
                        self.ac.withdraw_Checque()
                        time.sleep(3)
                        self.showAccountMenu()
                    else:
                        self.ac.withdraw()
                        time.sleep(3)
                        self.showAccountMenu()

        elif (self.accountMenu.upper() == "BALANCE"):
                
                    print(Account(self.accountNumberList[self.a],self.accountName,self.accountROI[self.a],self.balance[self.a]).getCurrentBalance())
                    print(Account(self.accountNumberList[self.a],self.accountName,self.accountROI[self.a],self.balance[self.a]).getRateOfInterest())  
                    
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
                    if (self.accountNum == 2013):
                        self.ac.withdraw_Savings()
                        time.sleep(3)
                        self.showAccountMenu
                    elif (self.accountNum == 2077):
                        self.ac.withdraw_Checque()
                        time.sleep(3)
                        self.showAccountMenu
                    else:
                        self.ac.withdraw()
                        time.sleep(3)
                        self.showAccountMenu()
                    break
#----
                elif(self.accountMenu.upper() == "DEPOSIT"):
                    if (self.accountNum == 2013):
                        self.ac.deposit_Savings()
                        time.sleep(3)
                        self.showAccountMenu
                    elif (self.accountNum == 2077):
                        self.ac.deposit_Checque()
                        time.sleep(3)
                        self.showAccountMenu
                    else:
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

        p = Program(0,0)
        print("\n\nWelcome to the Official Bank of Dylan")       
        print(p.showMainMenu())
            
        return ""
           



p2 = Program(0,0)
print(p2.run())
