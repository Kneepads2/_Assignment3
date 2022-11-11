import time

#ok so does Program inherit all the other classes or does Account do


class SavingsAccount:

    def __init__(self,_minimumBalance):
        self._minimumBalance = _minimumBalance

    def withdraw(self):
        print("")

class ChecquingAccount:

    def __init__(self,_overdraftAllowed):
        self._overdraftAllowed = _overdraftAllowed

    def withdraw(self):
        print("")

class Bank():
    i = 3
    def __init__(self,_bankName):
        self._bankName = ["Savings Account","Checquing Account","","",""]
        _bankName = self._bankName[3]
        return _bankName

    def openAccount(self):
        print("")

    def searchAccount(self):
        accountNum = str(input("What is the account number of the account you wish to enter? "))
        if (accountNum != 2):
            while (accountNum != 2):
                if (accountNum == 2):
                    print("")

class Program(Bank):
    def __init__(self):
        print("")

    def showMainMenu(self):
        print("\nTo open a new account, type 'OPEN'\nTo enter an existing account, type 'SEARCH'\nTo exit the program, type 'EXIT'\n")
        mainMenu = str(input("Enter your desired action: "))
        if (mainMenu.upper() != "OPEN" or mainMenu.upper() != "SEARCH" or mainMenu.upper() != "EXIT"):
            while (mainMenu.upper() != "OPEN" or mainMenu.upper() != "SEARCH" or mainMenu.upper() != "EXIT"):
                mainMenu = str(input("\nThat is not an action. Please enter a valid action: "))
                if (mainMenu.upper() == "OPEN"):
                    Bank.openAccount()
                    break

                elif (mainMenu.upper() == "SEARCH"):
                    Bank.searchAccount
                    break

                elif (mainMenu.upper() == "HELP"):
                    print("\nTo open a new account, type 'OPEN'\nTo enter an existing account, type 'SEARCH'\nTo exit the program, type 'EXIT'\n")

                elif (mainMenu.upper() == "EXIT"):
                    print("Exiting program.........")
                    time.sleep(1.2)
                    quit()
        elif (mainMenu.upper() == "OPEN"):
            Bank.openAccount()
            
        elif (mainMenu.upper() == "SEARCH"):
            Bank.searchAccount
            
        elif (mainMenu.upper() == "EXIT"):
            print("Exiting program.........")
            time.sleep(1.2)
            quit()
                
    def showAccountMenu(self):
        print("")

    def run(self):
        print("")

class Account(Program):
    def __init__(self,_accountNumber,_accountHolderName,_rateOfInterest,_currentBalance):
        self.accountNumber = _accountNumber
        self.accountHolderName = _accountHolderName
        self.rateOfInterest = _rateOfInterest
        self.currentBalance = _currentBalance

    def getAccountNumber(self):
        return self.accountNumber

    def getAccountHolderName(self):
        return self.accountHolderName

    def getRateOfInterest(self):
        return self.rateOfInterest

    def getCurrentBalance(self):
        return self.currentBalance

    def disposit(self):
        print("")

    def withdraw(self):
        print("")

p = Program()
print(p.showMainMenu())
