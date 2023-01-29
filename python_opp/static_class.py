# class student:
#     def  __init__(self,fname,lastname,department,age):
#         self.fname=fname
#         self.lastname=lastname
#         self.department=department
#         self.age=age
#     def display_show(self):
#         print(f"Frist name {self.fname} lastname {self.lastname} Department {self.department} age {self.age}")
#
#
#     @classmethod
#     def create_static_class(cls):
#         return student("smith","john","computer secience && engineering",23)
# std=student.create_static_class()
# print(std.department)
# print(std.lastname)

# class employee:
#     def __init__(self,emp_Id,emp_name,salary,post):
#         self.emp_id=emp_Id
#         self.emp_name=emp_name
#         self.salary=salary
#         self.post=post
#
#     def displayshow(self):
#         print(f"Employee sl : {self.emp_id} \n employee name :{self.emp_name} \n salary :{self.salary} \n employee post :{self.post}")
#
#     @classmethod
#     def create_callMethod(cls):
#         return  employee("01","sumilon",200000,"programer")
# emp=employee.create_callMethod()
# print(emp.emp_name)
# print(emp.salary)
# print(emp.__dict__)

#static method

# class TemperatureConverter:
#     @staticmethod
#     def celsius_to_fahrenheit(c):
#         return 9 * c /5 +32
#     @staticmethod
#     def fahrenheit_to_celsius(f):
#         return  5 * ( f- 32)/5
# f=TemperatureConverter.celsius_to_fahrenheit(86)
# fq=TemperatureConverter.fahrenheit_to_celsius(40)
# print(f)
# print(fq)

import  math
class circle:
    def __init__(self,redies):
        self.redies= redies
    def area(self):
        return  math.pi * self.redies **2

cir=circle(70)
output=cir.area()
print(f"Result of {output}")

from pprint import pprint


class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError('name cannot be empty')
        self._name = value

    @name.deleter
    def name(self):
        del self._name

pprint(Person.__dict__)





