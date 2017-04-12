# In python inheritance, when an object of child class is created, 
# the parent class constructor is called only if the child class 
# does not have its own constructor.Else the parent class constructor is not called.

# To invoke the parent class constructor and methods, we can use a magic method called super()

class Shelter:
    def __init__(self, shelter_for):
        self.shelter_for = shelter_for

class Tent(Shelter):
    def __init__(self, shelter_for, no_of_chairs, no_of_cots):
        super().__init__(shelter_for) # This is how we invoke super class constructor.
        self.no_of_chairs = no_of_chairs
        self.no_of_cots = no_of_cots

class Cage(Shelter):
    def __init__(self,shelter_for, lock_type):
        super().__init__(shelter_for)
        self.lock_type = lock_type