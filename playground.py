class Employee:
    def __init__(self, name, email, salary):
        self.name = name  # public
        self._email = email  # protected
        self.salary = salary

    def display(self):
        print(f"name{self.name} , _email={self._email} , salary={self.__salary}")

    @property
    def netSalary(self):
        return self.__salary * .8

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        print("--- setter called ----")
        if isinstance(salary, int) or isinstance(salary, float) and salary > 0:
            self.__salary = salary
        else:
            raise TypeError("salary must be an integer or float")


emp = Employee("fff", "fff", 444)
print("-----")

from abc import ABC, abstractmethod


class Book:
    pass

b = Book()
print(isinstance(b, object))

res = type('iti')


class Employee:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    # override
    def __str__(self):
        pass