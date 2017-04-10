class Table: 
    def __init__(self):
      self.no_of_legs=4
      self.glass_top=None
      self.wooden_top=None

    def identify_rate(self):
      if(self.glass_top==True):
        rate=20000
      elif(self.wooden_top==True):
        rate=30000
      else:
        rate=0
      return rate

dining_table=Table()
dining_table.glass_top=False
dining_table.wooden_top=True
print("Rate of dining table:",dining_table.identify_rate())

# Instance Variable	no_of_legs, glass_top, wooden_top are the instance variables
# Reference Variable	dining_table is a reference variable which refers to a Table object
# Local Variable	rate is a local variable which is created when identify_rate() method is invoked on Table object
