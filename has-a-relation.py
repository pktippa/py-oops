# In Object Oriented Approach, it is possible to have relationships between classes. 
# When an object of a class becomes the instance variable of another class, it is known as "has-a" relationship or AGGREGATION.
# If ClassA 'has-a' ClassB, then ClassB aggregates ClassA
class Employee:
    def __init__(self,name,emp_id,contact):
        self.name=name
        self.emp_id=emp_id
        self.contact=contact # this is where the instance variable of Contact class is getting created.

class Contact:
    def __init__(self,address,mobile_no):
        self.address=address
        self.mobile_no=mobile_no

cntct1 = Contact("Karnataka", 1234)
cntct2 = Contact("Andhra", 1234)

emp1=Employee("Ajith",44,cntct1)
emp2=Employee("Raj",28,cntct2)

print(emp1.contact.address)
emp2_contact=emp2.contact
print(emp2_contact.address)
print(emp2.contact.mobile_no)