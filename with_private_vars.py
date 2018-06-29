# Variables which should not be accessed outside a class are called private variables.
# In Python you can easily create private variables by prefixing it with a double underscore ( __ )

# Whenever you create a private variable, python internally changes its name as _ClassName__variableName.
# For example, here __salary is actually internally stored as _Trainer__salary.

# Methods used to set values are called as 'mutator' methods and methods used to get values are called as 'accessor' methods!

class Trainer:
    def __init__(self):
        self.name=None
        self.__salary=1000
    def set_salary(self,salary):
        self.__salary=salary
    def get_salary(self):
        return self.__salary
lion_trainer=Trainer()
lion_trainer.name="Mark"
# You can set a private variable using obj._Trainer__salary. Ex: lion_trainer._Trainer__salary = 2000
# But this is not a right way, the correct way is to use mutator methods.
lion_trainer.set_salary(2000)
print("Lion's trainer is", lion_trainer.name)
# You can also access the private variable using obj._Trainer__salary. Ex: print("Salary of Trainer" , lion_trainer._Trainer__salary)
# But this is not a right way, the correct way is to use accessor methods.
print("His salary is Rs.", lion_trainer.get_salary())
