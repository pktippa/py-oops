# Polymorphism - One method can have different versions.
# We can override the methods of parent class in the child class.
# The method to be called is decided automatically depending on the object on which the method is invoked.
class Animal:
    def eat(self, food):
        print("Animal eats food ", food)
    def sleep(self, hours):
        print("Animal sleep for ", hours, " hours")

class Dog(Animal):
    def eat(self, food): # This method is overriden
        print("Dog eats food ", food)
        # we can also call the parent class method here using super()
        # super().eat(food)
    def barks(self, sound):
        print("Dog is barking ", sound)

class Lion(Animal):
    def roars(self, sound):
        print("Lion roars ", sound)

dog = Dog()
dog.eat("Chicken") # this invokes the overridden method rather than the parent class method.
dog.sleep(4)
dog.barks("Mediumly")
lion=Lion()
lion.eat("Goat") # this will call the parent class method.
lion.sleep(9)
lion.roars("Loudly")