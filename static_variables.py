# Any variable you create inside the class directly is treated as a 
# common variable to all the objects of the class. 
# Such variables are called as static variables.

class Employee:
    __no_of_employees = 0
    def __init__(self, emp_name, emp_age):
        self.name = emp_name
        self.age = emp_age
    def employee_login(self):
        Employee.__no_of_employees += 1
    def get_total_employees(self):
        return Employee.__no_of_employees
# We can pass parameters to the constructor and set the instance variables values.
raj=Employee("Raj", 28)
raj.employee_login()
pradeep=Employee("Pradeep", 27)
pradeep.employee_login()
kumar=Employee("Kumar", 27)
kumar.employee_login()
# Getting the static variable values from refernce variable is not the right way.
# Rather use static methods, have a look at static_methods.py
print("Total employees logged in : ", kumar.get_total_employees())
