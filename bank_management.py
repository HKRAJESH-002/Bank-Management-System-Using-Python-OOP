from abc import ABC, abstractmethod
from random import randint


class Customer(ABC):

    @abstractmethod
    def createaccount(self):
        pass

    @abstractmethod
    def authenticate(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def displaybalance(self):
        pass


class SavingAccount(Customer):

    def __init__(self):
        self.accounts = {}

    def createaccount(self, name, initialdeposit):

        accountnumber = randint(10000, 50000)

        self.accounts[accountnumber] = {
            "name": name,
            "balance": initialdeposit
        }

        print("\nAccount Created Successfully!")
        print("Account Number:", accountnumber)

    def authenticate(self, name, accountnumber):

        if accountnumber in self.accounts:

            if self.accounts[accountnumber]["name"] == name:
                print("\nAuthentication Successful")
                return True

        print("\nAuthentication Failed")
        return False

    def withdraw(self, accountnumber, amount):

        balance = self.accounts[accountnumber]["balance"]

        if amount > balance:
            print("\nInsufficient Balance")
        else:
            self.accounts[accountnumber]["balance"] -= amount
            print("\nWithdrawal Successful")
            self.displaybalance(accountnumber)

    def deposit(self, accountnumber, amount):

        self.accounts[accountnumber]["balance"] += amount

        print("\nDeposit Successful")
        self.displaybalance(accountnumber)

    def displaybalance(self, accountnumber):

        print(
            "Available Balance:",
            self.accounts[accountnumber]["balance"]
        )


bank = SavingAccount()

while True:

    print("\n===== BANK MENU =====")
    print("1. Create Account")
    print("2. Access Account")
    print("3. Exit")

    userchoice = int(input("Enter your choice: "))

    if userchoice == 1:

        name = input("Enter Name: ")
        deposit = int(input("Enter Initial Deposit: "))

        bank.createaccount(name, deposit)

    elif userchoice == 2:

        name = input("Enter Name: ")
        accountnumber = int(input("Enter Account Number: "))

        authenticated = bank.authenticate(
            name,
            accountnumber
        )

        if authenticated:

            while True:

                print("\n----- ACCOUNT MENU -----")
                print("1. Withdraw")
                print("2. Deposit")
                print("3. Display Balance")
                print("4. Logout")

                accountchoice = int(
                    input("Enter your choice: ")
                )

                if accountchoice == 1:

                    amount = int(
                        input("Enter Withdraw Amount: ")
                    )

                    bank.withdraw(
                        accountnumber,
                        amount
                    )

                elif accountchoice == 2:

                    amount = int(
                        input("Enter Deposit Amount: ")
                    )

                    bank.deposit(
                        accountnumber,
                        amount
                    )

                elif accountchoice == 3:

                    bank.displaybalance(
                        accountnumber
                    )

                elif accountchoice == 4:

                    print("Logged Out Successfully")
                    break

                else:
                    print("Invalid Choice")

    elif userchoice == 3:

        print("Thank You For Using Our Bank")
        break

    else:
        print("Invalid Choice")
