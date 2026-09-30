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