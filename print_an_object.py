# Python has a built method called __str__(self), which will called automatically when we print an object.
# __str__(self) must return a String, so for other datatypes we need to do type casting
class Employee:
    def __init__(self):
        self.__name = None
        self.__age = None
    
    def set_age(self, emp_age):
        self.__age = emp_age
    
    def get_age(self):
        return self.__age
    
    def set_name(self, emp_name):
        self.__name = emp_name
    
    def get_name(self):
        return self.__name
    
    # __str__(self) 
    def __str__(self):
        return(self.__name+ " " + (str)(self.__age))
developer=Employee()
developer.set_name("Raj")
developer.set_age(28)
print(developer)
