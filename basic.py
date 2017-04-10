# Defining a class
class Employee:
    # The Constructor method, refer readme for self object
    def __init__(self):
        # Creating properties for the class.
        self.name = None
        self.age = None
        self.salary = None

ajith=Employee()
ajith.age = 30
ajith.name = "Ajith V"
ajith.salary = 50000

print("Ajith's Age is : ", ajith.age)