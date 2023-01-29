"""
what's function
Ans: Dharon apner akta  kaj programer bivvno jiga bar bar projion pora ,,akhon jodie  apni bar akoi program
bar writing koron thala programer complexity onak bashi voba sohoj manage able kora ji naha main memory jigga bashi khaba
so ei problem  dur karo janno apni oi code ta function wrap ba bind korta paron,,..as a result when you  need code just
funcation call koron problem solve.....
more easy says:jakhon programmer maja maja akta kaj again and again kora projon just create a function and calling
again and again

1:function defination parte
def ar fullform= defination of function
functionName=function akta name dita hoba
()=paranthashes
:=colon
functionbody

2: function calling
just functionname()

# two type of function

1:return
2:non return

#:parameter
1:parameter type function
2:non parameter type function

"""
#Example:-01

# def summation():
#     print(1+1)
# summation()
#
# # substraction
#
# def substraction():
#     print(2-1)
#
# substraction()

# return function :-

# def summation():
#     return  1+1
#
# print(summation())
#
#
# def substraction():
#     return  2-1
# print(substraction())


# argument or parameters

# def shop(item1,item2):
#     print(item1,item2)
#
# shop("onuion","vegatable")
# shop("apple","orange")

"""
 notes: Astrerisks (*) parameter holo amon aktie parameterjar help amer akto argument akadak paramester ka
 functon votor receive  korta .Atie multo argument ka tuple hasive store kora 
"""
#
# def shop(*item):
#     print(*item)
#
# shop("apple","orange","Banana","watermelon","cherry","jherry")
#
# def name_show(*name):
#     print(*name)
#
# name_show("sumilon","nikor","Ronie","Mona bass","shipa","Ritu","jumel")


# * args argument 0r arbitraray positional argument

# def person(*info):
#     print(info)
#
# person("sumilon",21,"CSE","programer")
# person("nikor",25,"CSE","digital markter")
# person("joya bain",21,"CSE","chapa base")
# person("likhon",23,"CSE","bashi kotha bola")
# print(type(person()))

# def person(*info):
#     for i in info:
#         print(i)
#
# person("similon",21,"male","Dhaka","Barishal")

"""
keyword arguments :-
keyword argument ka specific vaba  bola daiya ja kono parametera kon values store hoba

keyword function use kora class maja oh oops concept use kora somoy
"""

# def person(p_name,p_address,p_gender,p_post):
#     print(p_name,p_address,p_gender,p_post)
#
# person(p_name="sumilon biswas",p_address="Dhanmondie",p_gender="male",p_post="programmer")
# person(p_name="liemon",p_address="Barishal",p_gender="male",p_post="salar")
#
# person(p_name="Rupa",p_address="patukhalie",p_gender="female",p_post="householder")
# person(p_name="Rakib islam",p_address="Dhaka",p_gender="male",p_post="student")

# def person(pName,pAddress,pContact,pPost,pProfession):
#     print(pName,pAddress,pContact,pPost,pProfession)
#
#
# person(pName="sumilon biswas anik",pAddress="Barishal",pContact="983784365",pPost="programmer",pProfession="student")
# person(pName="sumiya",pAddress="Barguna",pContact="8746743",pPost="it support engineer,",pProfession="house_holder")
#

# def employee(empName,empSalary,empAddress,empost):
#     print("employee name =",empName,"\nsalary =",empSalary,"\nEmployee address",empAddress,"\nemployee psot :",empost)
#
# employee(empName="sumilon biswas",empSalary=200000,empAddress="Dhanmondie",empost="programer")
# print("")
# employee(empName="anik",empSalary=24947,empAddress="Dhaka",empost="salar")
# print(" ")
# employee(empName="akash ",empSalary=3930448,empAddress="janie naha",empost="pHp developer")
#


# def Employee(e_name,e_address,e_phn,e_salary,e_post):
#     print("employee name ",e_name,"employee address :",e_address,"employee phone :",e_phn,"employee salary :",e_salary,"employee post",e_post)
#
# Employee(e_name="sumilon biswas",e_address="Dhanmondie",e_phn="656546",e_salary=399999,e_post="programmer")
#

"""
keyword + non keyword argument aksathay thiakal

"""

# def person(name,age,Gender,location):
#     print(name,age,Gender,location)
#
# person("Rakib",23,"male","dhaka")
# person("sumilon biswas anik",21,"male","uttra")
# person("komal",24,"male","mohaykhalie")
# person("nupor",24,"female","joynogor")
# print(" ")
# person("sanon",29,Gender="female",location="india")
# person(name="kirtiy",age=25,Gender="female",location="uttra city")

## **Kwargs argument
"""
 kwargs argument it's returns of  dictonary values 
 kwargs argument somoy dodulbe astersisk dita hoya 
"""

def person(**info):
    print(info)

person(name="sumilon",age=23,department="cse",Gender="male",loction="dhamondie-15")
