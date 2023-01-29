# class person:
#     name=""
#     agre=''
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def greets(self):
#         print(f"Hi! It's is {self.name}")
#
# person=person("sumilon biswas anik",29)
# print(person.name)
# print(person.age)
# print(person.greets())
# print(person.__dict__)
#
# class person:
#     counter=0
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         self.counter +=1
#
#     def greet(self):
#         print(f"my name is {self.name} and age {self.age}")
#
# person1=person("sumilon",67)
# print(person1.greet())
# person2=person("anika",67)
# print(person2.greet())
#
#
# print(person.counter)

class Person:
    counter = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.counter += 1

    def greet(self):
        return f"Hi, it's {self.name}."

p=Person("sumilon",56)
p1=Person("sarabonie",67)
p3=Person("summon khan",90)

print(Person.counter)

