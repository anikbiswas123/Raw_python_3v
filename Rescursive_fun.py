#
# def count(number):
#
#     if number == 3:
#         return  number
#     else:
#         return  count(number+1)+1
#
# print(count(1))
#
# '''
#   (num+1) +1 = 1+1+1=3
#    (2+1)= 3+1 = 4

# '''

# def factorial(num):
#     if num == 1:
#         return 1
#     else:
#         return num * factorial(num-1)
#
# # Result=factorial(5)
# Result=factorial(1)
# print("this is factorial number =",Result)


# nested function

# def Bangladesh():
#
#     print("Hi! Bangladesh")
#     def Rajshahie():
#         print("Python is awasome programing languages !")
#     Rajshahie()
#
# Bangladesh()

# def employee(Emp_name,salary):
#
#     def full_salaryOf_yaer():
#         return  salary * 12
#     print(f"empolyee name is {Emp_name} and yearlyfully salary {full_salaryOf_yaer()}")
#
# employee("sumilon biswas anik",5000)

def empolyee_information(emp_name,salary=0,hours=0,hour_base_pay=0):
    def full_year_salary():
        return  salary * 12
    def hours_base_salary():
        return hour_base_pay * hours

    yield full_year_salary()
    yield hours_base_salary()

empolyee_information("anika",salary=2000)
empolyee_information("anika Rehaman",hours=10,hour_base_pay=250)




