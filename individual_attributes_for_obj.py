# Python allows you to create attributes dynamically as well. Whenever you try to assign a value to an attribute, 
# it checks if the attribute is already present. If present, the attribute is assigned, else the attribute is created!!
class Employee:
    def __init__(self):
        self.name = None
        self.age = None
    
    def set_employee_details(self, emp_name, emp_age):
        self.age = emp_age
        self.name = emp_name

developer=Employee()
developer.set_employee_details("Raj", 28)
# Creating attribute for developer object
# Note:In Python, though it is possible to create individual attributes for objects of a class, it is not encouraged as per OOP principles.
developer.title = "Developer"
# The above code is not a good practice.