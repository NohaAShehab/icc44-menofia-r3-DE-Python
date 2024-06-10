# # %%
# counter = 0  # global variable
#
#
# class Employee:
#     def __init__(self, id, name, salary):
#         # id , name , salary --> instance variables
#         self.id = id
#         self.name = name
#         self.salary = salary
#         global counter
#         counter += 1
#
#     def display(self):  # instance methods
#         print(f"Employee ID: {self.id}, Name: {self.name}, Salary: {self.salary}")
#
#     # destructor
#     def __del__(self):
#         print("---- this function is called when object is deleted----")
#         global counter
#         counter -= 1
#
#
# print(counter)
# emp1 = Employee(1, "John", 5000)
# emp2 = Employee(2, "Jack", 6000)
# emp3 = Employee(3, "Abc", 9000)
# print(counter)
#
# del emp1
# print(counter)


#***************************************************
class Employee:
    empcount = 0
    def __init__(self, id, name, salary):
        # id , name , salary --> instance variables
        self.id = id
        self.name = name
        self.salary = salary
        Employee.empcount += 1

    def display(self):  # instance methods
        print(f"Employee ID: {self.id}, Name: {self.name}, Salary: {self.salary}")

    # destructor
    def __del__(self):
        Employee.empcount -= 1
        print("---- this function is called when object is deleted----")
