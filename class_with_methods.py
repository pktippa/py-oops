class Monkey:
    def __init__(self):
        self.breed=None
        self.color=None
    
    # Method declared in the class.
    def ride_cycle(self):
        if(self.breed=="Chimpanzee"):
            print("Rides cycle on a rope")
        else:
            print("Rides cycle")

    def eat_banana(self, monkey_breed):
        self.breed = monkey_breed

chimpu=Monkey()
chimpu.breed="Chimpanzee"
chimpu.color="Brown"
# Invoking the method from the object created.
chimpu.ride_cycle()

monky = Monkey()
# Always remember that in a method since 'self' is not a keyword, no matter what variable is used, 
# the first parameter is always considered as the implicit reference to the object used.
monky.eat_banana("Baboon")

print("Breed of monkey who eat banana : ", monky.breed)