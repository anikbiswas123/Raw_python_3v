#
# class cartoon:
#     series='TV serises'
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#
# obj1=cartoon("Doremon",10)
# obj2=cartoon("shirchare",5)
# print(obj1.name)
# print(obj1.age)
# print("++===============")
# print(obj2.name)
# print(obj2.age)

# class person():
#     def __init__(self,p_name,p_address,p_contact,p_salary,p_post):
#         self.p_name=p_name
#         self.p_address=p_address
#         self.p_contact=p_contact
#         self.p_salary=p_salary
#         self.p_post=p_post
#     def get_full_summary(self):
#         return  f"person name :{self.p_name} \n person address {self.p_address} \n person contsct {self.p_contact} \n person salary {self.p_salary} \n person post {self.p_post}"
#
#
# person1=[
#           person("sumilon","Dhanmodie","08474887488",30000,"python developer"),
#           person("Rakib Hossain","Kam Rangchar","847457633",2500,"python developper"),
#           person('Efa',"Dhaka utra","7764643",2000,"python developer"),
#           person("lipa","Barisal","74646433",1500,"php developer"),
#           person("Akash","Mohammdapur","7486433",20000,"php developer"),
#           person("monu","farm_gate","46436322",20000,"Asp.net developer")
#         ]
#
# # for person in person1:
# #     if person.p_salary > 15000:
# #         print(person.get_full_summary())
# #         print("===================")
#
# for person in  person1:
#     if person.p_salary <= 15000:
#         print(person.get_full_summary())
#         print("=====================")

# class  person():
#     def __init__(self,name):
#         self.name=name
#
#     def say_hi(self):
#         print(f"my name is ",self.name)
#
# person=person("sumilon")
# person.say_hi()

# class employee():
#     def __init__(self,emp_name):
#         self.emp_name=emp_name
#     def get_show(self):
#         print(f"employee name is ",self.emp_name)
#
# emp=employee("Rakib hossain")
# emp.get_show()


class employee():
    def __init__(self):
        print("Employee class created !")
    def __del__(self):
        print("Destructored called")
def  create_object():
    print("create object class")
    obj=employee()
    print("funnctons end")
    return  obj
print("printed create object fuctios ")
ob=create_object()
print("program end!")
print("thanks you program ")

