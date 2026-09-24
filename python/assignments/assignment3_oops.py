# Common / Custom Exception Class 

class PayrollError(Exception):
    pass
    
#Employee payroll class
class EmployeePayroll: 
    emp_count=0
    def __init__(self,emp_id, emp_name, emp_salary):
        if not isinstance(emp_id,int):
            raise PayrollError("Employee Id must be a number")
            
        if emp_id<=0:
            raise PayrollError("Employee Id must be positive and greater than 0")
            
        if emp_salary<=0:
            raise PayrollError("Employee salary must be greater than 0")

        self.emp_id=emp_id
        self.emp_name=emp_name
        self.emp_salary=emp_salary
        EmployeePayroll.emp_count+=1
            
    def calculate_tax(self):
        return self.emp_salary*0.10
                
    def calculate_net_salary(self):
        return self.emp_salary-self.calculate_tax()
        
    def bonus(self):
        return self.emp_salary*0.10

    # Decorator for increasing bonus
    def increase_bonus(function):
        def dec_wrapper(self):
            extra_bonus = function(self)
            return extra_bonus * 2
        return dec_wrapper
    
    # Decorator
    @increase_bonus
    def special_bonus(self):
        return self.bonus()
        
    def display(self):
        print("ID: ", self.emp_id)
        print("Name: ", self.emp_name)
        print("Salary INR: ", self.emp_salary)
        print("Tax INR: ", self.calculate_tax())
        print("Net Salary: ", self.calculate_net_salary())

    @classmethod
    def employee_total(cls):
        print("Total Number of Employees: ", cls.emp_count)

    @staticmethod
    def valid_salary(salary):
        return isinstance(salary, (int, float)) and salary > 0
        


# creating employee objects here
e1=EmployeePayroll(69,"Pavan",50000)
e2=EmployeePayroll(70,"Hari",60000)
e3=EmployeePayroll(80,"Saharika",70000)

#display employee
e1.display()
print("----------------------------")
e2.display()
print("----------------------------")
e3.display()
print("----------------------------")

#udpate Pavan salary
e1.emp_salary=80000
print("Pavan Salary is updates with bonus:")
e1.display()
print("----------------------------")
print()
print("--Accessing class variable--")
EmployeePayroll.employee_total()
print()
print("--Accessing static methods--")
print(EmployeePayroll.valid_salary(10000))
print(EmployeePayroll.valid_salary(-10000))
print("----------------------------")
print()
print("Default Bonus (10%):", e1.bonus())
print("Bonus after decorator (20%):", e1.special_bonus())