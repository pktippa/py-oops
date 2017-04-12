# isinstance(obj, classinfo) is a built-in function in Python which returns true if argument obj is an object of argument classinfo. Else, it returns false.
class Employee:
    def __init__(self, role, id):
        self.role = role
        self.id = id

class Contact:
    def __init__(self, name, mobile):
        self.name = name
        self.mobile = mobile

e1=Employee("Developer", 123)
e2=Employee("Tester",456)
c1=Contact("Ajith",789)
c2=Contact("Raj",908)
list_to_process = [e1, c1, c2, e2]
for obj in list_to_process:
    if isinstance(obj, Employee): print("Employee role", obj.role, " id ", obj.id) # Checking whether the instance 'obj' is of type class Employee or not
    if isinstance(obj, Contact): print("Contact name", obj.name, " mobile ", obj.mobile) # Same as above, but checking for Contact