# When we want to access a method without an object, you can use the @staticmethod
# @staticmethod makes the method immediately below it a static method.
# A static method does not belong to the object and hence does not have the `self` attribute.
# In other words the first parameter is NOT considered as an implicit reference to the object
# and hence it cannot access the self attributes of an object of its class.

class Employee:
    __no_of_employees = 0
    def __init__(self, emp_name, emp_age):
        self.name = emp_name
        self.age = emp_age
    def employee_login(self):
        Employee.__no_of_employees += 1
    @staticmethod
    def get_total_employees():
        return Employee.__no_of_employees
# We can pass parameters to the constructor and set the instance variables values.
raj=Employee("Raj", 28)
raj.employee_login()
pradeep=Employee("Pradeep", 27)
pradeep.employee_login()
kumar=Employee("Kumar", 27)
kumar.employee_login()
print("Total employees logged in via classname : ", Employee.get_total_employees())
# Static methods can be accessed/invoked using object reference
# But its a good practice to invoke a static method using class name.
print("Total employees logged in reference variable : ", kumar.get_total_employees())
