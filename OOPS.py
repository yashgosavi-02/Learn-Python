# class - template used to create objects
# object - unique entity

# maps real world entities
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getSalary(self):
        print(self.salary)

emp1 = Employee("Rohan", 3455)
print(emp1.name)
print(emp1.salary)
emp1.getSalary()

