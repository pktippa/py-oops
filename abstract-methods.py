# In OOP, we can create abstract methods. A class which has an abstract method cannot be instantiated. 
# Similarly, a sub class of an abstract class cannot be instantiated unless it overrides the abstract method.

# abc - Abstract Base class
# ABCMeta - Inbuilt special class
# abstractmethod - Indicator to specify method is abstract.
from abc import ABCMeta, abstractmethod
class Employee(metaclass=ABCMeta):
    @abstractmethod # Indicating the abstractmethod
    def salary(self):
        pass
    def perforimg_task(self, task_name):
        return "Perfroms " + task_name + " tasks"

class Teacher(Employee):
    def salary(self):
        return 100

class Mentor(Employee):
    def salary(self):
        return 75

t1=Teacher()
print("Teacher", t1.perforimg_task("teaching"), "and earns ", t1.salary())
m1=Mentor()
print("Mentor", m1.perforimg_task("mentoring"), "and earns ",m1.salary())

# Another example of multi level inheritance implementation of abstract methods.
class Parent(metaclass=ABCMeta):
    def __init__(self): 
        self.num=5
    @abstractmethod
    def show(self):
        pass
    
class Child(Parent):  # Here we have not override the show method, but the GrandChild which is sub class for Child overriden it.
    def __init__(self):
        super().__init__()
        self.var=10
 
class GrandChild(Child):
    def show(self): # This is where we override the show method of Parent class.
        print(self.num)
        print(self.var)
        print("This is possible") 
        
obj=GrandChild()  
obj.show()