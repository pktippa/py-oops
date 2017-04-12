# To raise an exception, you can use the 'raise' keyword. 
# Note that you can only raise an object of the Exception class or its subclasses. 
# Exception is an inbuilt class in python.
# To raise subclasses of Exception(custom Exception) we have to create our own custom Class.
# We can also pass message along with exception so that exception handling is consistent.

class Employee:
    def __init__(self, salary):
        self.salary_lower_limit = 100
        self.salary_upper_limit = 200
        self.salary = salary

class HumanResource:
    def pay_salary(self, employee):
        if(employee.salary < employee.salary_lower_limit): raise LowSalaryException(employee) # Raising Custom Exceptions
        elif(employee.salary > employee.salary_upper_limit): raise HighSalaryException(employee)
        else:
            print("Employee is satisfied with given salary.")

class LowSalaryException(Exception):
    def __init__(self, employee):
        # Building the custom message
        message = "Given Salary is "+ str(employee.salary) + "is too low. Salary  range should be between " + str(employee.salary_lower_limit) + "and" + str(employee.salary_upper_limit)
        # Passing the message to super class
        super().__init__(message)
        
class HighSalaryException(Exception):
    def __init__(self, employee):
        message = "Given Salary is "+ str(employee.salary) + "is too High. Salary  range should be between " + str(employee.salary_lower_limit) + "and" + str(employee.salary_upper_limit)
        super().__init__(message)

try:
    employee=Employee(50)
    human_resource=HumanResource()
    human_resource.pay_salary(employee)
except LowSalaryException as e:
    print(e)
except HighSalaryException as e:
    print(e)
except:
    print("Some other error.")