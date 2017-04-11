# In Object Oriented Approach, when an object of a class is used as a local variable in another class,
# it is called as "uses-a" relationship or ASSOCIATION.

class Employee:
    def __init__(self,name,emp_id):
        self.name=name
        self.emp_id=emp_id
    def call_emergency(self, contact): # Here the object of class Contact is used as a local variable
        if contact.address == "Karnataka":
            print("Call Emergency to contact no:", contact.mobile_no)
class Contact:
    def __init__(self,address,mobile_no):
        self.address=address
        self.mobile_no=mobile_no
    
    

cntct1 = Contact("Karnataka", 1234)
cntct2 = Contact("Andhra", 1234)

emp1=Employee("Ajith",44)
emp2=Employee("Raj",28)

emp1.call_emergency(cntct1)
emp1.call_emergency(cntct2)