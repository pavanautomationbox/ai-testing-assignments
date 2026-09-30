#single inheritance
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

print("--2-Multiple Inheritance----")
class Developer:
    def write_code(self):
        print("Developer code complete.")

class Tester:
    def test_application(self):
        print("Tested application.")

class Sdet(Developer,Tester):
    def automate_tests(self):
        print("test automation completed.")

sdet=Sdet()
sdet.write_code()
sdet.test_application()
sdet.automate_tests()
        
print("--3-Multilevel Inheritance----")
class Employee:
    def login(self):
        print("logged in sucessful")

class Developer(Employee):
    def write_code(self):
        print("Developer writes code")

class SeniorDeveloper(Developer):
    def review_code(self):
        print("Senior developer review the code")

senior_emp=SeniorDeveloper()
senior_emp.login()
senior_emp.write_code()
senior_emp.review_code()

print("--4-Hierarchical Inheritance----")
class BankAccount:
    def login(self):
        print("login successful.")
    def check_balance(self):
        print("balance is: INR 100000")

class Savings(BankAccount):
    def calculate_interest(self):
        print("interest earned: INR 10000")

class Current(BankAccount):
    def overdraft(self):
        print("overdraft balance: INR 25000")

print("------------Savings Account----------------")
savings=Savings()
savings.login()
savings.check_balance()
savings.calculate_interest()
print("------------Current Account----------------")
current=Current()
current.login()
current.check_balance()
current.overdraft()

print("--5-Real-Time Security Platform Example----")
