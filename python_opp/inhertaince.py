# class person:
#     # def __init__(self,name):
#     #     self.name=name
#     def greets(self):
#         return (f"person name  is :")
# class employee(person):
#     def __init__(self,name,job_tittle,salary):
#
#          self.name=name
#          self.job_tittle=job_tittle
#          self.salary=salary
#     def greets(self):
#         return (f"person salary   is :{self.salary}")
#
# emp=employee("sumilon","python developer",30000)
# print(emp.greets())
# print(isinstance(emp,employee))
# print(issubclass(employee,person))
#
# #method overridding

# class employee:
#     def __init__(self,name,base_pay):
#         self.name=name
#         self.base_pay=base_pay
#     def get_pay(self):
#         return self.base_pay
#
# class salary_emp(employee):
#     def __init__(self,name,base_pay,increment_pay):
#         self.name=name
#         self.base_pay=base_pay
#         self.increment_pay=increment_pay
#     def get_pay(self):
#         return  self.base_pay + self.increment_pay
# emp=salary_emp("john",5000,1500)
# print(emp.get_pay())

# import re
#
# class Parser:
#     def __init__(self, text):
#         self.text = text
#
#     def email(self):
#         match = re.search(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+', self.text)
#         if match:
#             return match.group(0)
#         return None
#
#     def phone(self):
#         match = re.search(r'\d{3}-\d{3}-\d{4}', self.text)
#         if match:
#             return match.group(0)
#         return None
#
#     def parse(self):
#         return {
#             'email': self.email(),
#             'phone': self.phone()
#         }
#
# # s = 'Contact us via 408-205-5663 or email@test.com'
# # parser = Parser(s)
# # print(parser.parse())
#
# class UKparse(Parser):
#
#     def phone(self):
#         match=re.search(r'(\+\d{1}-\d{3}-\d{3}-\d{4})',self.text)
#         if match:
#             return  match.group(0)
#         return  None
#
# s='Contact me via +1-650-453-3456 or email@test.co.uk'
# paraes=UKparse(s)
# print(paraes.parse())

# class Employee:
#     def __init__(self,name,base_pay,bonus):
#         self.name=name
#         self.base_pay=base_pay
#         self.bonus=bonus
#     def get_pay(self):
#         return self.base_pay + self.bonus
#
# class  salaryEmployee:
#     def __init__(self,name,base_pay,bonus,salar_increment):
#         super().__init__(name,base_pay,bonus)
#         self.salar_increment = salar_increment
#     def get_pay(self):
#        return super().get_pay() + self.salar_increment
#
# employee=salaryEmployee("john",6000,1500,2000)
# print(employee.get_pay())

# class Employee:
#     def __init__(self, name, base_pay, bonus):
#         self.name = name
#         self.base_pay = base_pay
#         self.bonus = bonus
#
#     def get_pay(self):
#         return self.base_pay + self.bonus
#
#
# class SalesEmployee(Employee):
#     def __init__(self, name, base_pay, bonus, sales_incentive):
#         super().__init__(name, base_pay, bonus)
#         self.sales_incentive = sales_incentive
#
#     def get_pay(self):
#         return super().get_pay() + self.sales_incentive
#
#
# if __name__ == '__main__':
#     sales_employee = SalesEmployee('John', 5000, 1000, 2000)
#     print(sales_employee.get_pay())  # 8000

# class  Employee:
#     def __init__(self,name,base_pay,bonus):
#         self.name=name
#         self.base_pay=base_pay
#         self.bonus=bonus
#     def get_pay(self):
#         return  self.base_pay + self.bonus
# class salaryEmployment(Employee):
#     def __init__(self,name,base_pay,bonus,salary_incentive):
#         super().__init__(name,base_pay,bonus)
#         self.salary_incentive=salary_incentive
#     def get_pay(self):
#         return  super().get_pay() + self.salary_incentive
# if __name__=='__main__':
#     salEmployee=salaryEmployment("john",6000,500,2000)
#     print(salEmployee.get_pay())

class Employee:
    def __init__(self,name,base_pay,bonus):
        self.name=name
        self.base_pay=base_pay
        self.bonus=bonus
    def get_pay(self):
        return  self.base_pay + self.bonus

class salaryOfemployee(Employee):
    def __init__(self,name,base_pay,bonus,salary_incentive):
        super().__init__(name,base_pay,bonus)
        self.salary_incentive=salary_incentive

    def get_pay(self):
        return super().get_pay() + self.salary_incentive

sal=salaryOfemployee("smith",6000,700,500)
print(sal.get_pay())
