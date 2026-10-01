class BankAccount:
    def login(self):
        print("login sucessfull")

    def check_balance(self):
        print("Balance: INR 50000")

class SavingsAccount(BankAccount):
    def calculate_interest(self):
        print("Interest earned: INR 5000")
print("--1-Single Inheritance----")
account=SavingsAccount()
account.login()
account.check_balance()
account.calculate_interest()