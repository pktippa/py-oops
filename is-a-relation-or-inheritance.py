# Types of inheritance
# 1. Single-level Inheritance
# 2. Multi-level Inheritance
# 3. Heirarchical Inheritance
# 4. Multiple Inheritance

class Employee:
    def salary(self):
        return 100;

class Developer(Employee):
    def developing(self):
        print("salary for developer : ", self.salary())

class Tester(Employee):
    def testing(self):
        print("Salary for tester: ", self.salary())

developer=Developer()
developer.developing()
tester=Tester()
tester.testing()
