# Python allows a class to inherit multiple classes. This is also called as "Multiple Inheritance".
# Here the Dog class inherits both Animal and Pet class.
# When both the parent classes have same variables or methods, the class is determined from left to right.
# For example, in Dog(Animal, Pet): the methods are considered from left to right. 
# That means if a method is not there in Animal class, only then it checks in the Pet class. 
# Hence tommy.eat() would invoke Animal class eat method

class Animal:
    def eat(self):
        print("animal eating")
    def sleep(self):
        print("animal sleeping")
class Pet:
    def be_loyal(self):
        print("Pet being loyal")
    def eat(self):
        print("pet eating")        
        
class Dog(Animal,Pet):
    pass

tommy=Dog()
tommy.eat() # This will call Animal class eat method, since Animal is the left most one.
tommy.be_loyal()
tommy.sleep()