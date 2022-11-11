import time


class Account:
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

class Bank:
    i = 3
    def __init__(self,_bankName):
        self._bankName = ["Savings Account","Checquing Account","","",""]
        _bankName = self._bankName[i]
        return _bankName

    def openAccount(self):
        print("")

    def searchAccount(self):
        print("")

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

class Program(Account,Bank,ChecquingAccount,SavingsAccount):
    def __init__(self):
        print("")

    def showMainMenu(self):
        print("\nTo open a new account, type 'OPEN'\n To search for an existing account, type 'SEARCH'\n To exit the program, type 'EXIT'\n")
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

p = Program()
print(p.showMainMenu())
