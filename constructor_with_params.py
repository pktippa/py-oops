class Employee:
    def __init__(self, emp_name, emp_age):
        self.name = emp_name
        self.age = emp_age

# We can pass parameters to the constructor and set the instance variables values.
developer=Employee("Raj", 28)
print("Employee name : ", developer.name, " age: ", developer.age)