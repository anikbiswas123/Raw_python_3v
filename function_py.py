
# structured of function
"""
function has two part
1) function creation 0r function defination
2) function calling
def=defination of function

#function defination
def functionName():
    function body

#function calling
functionName()
two types of function
1) return types
2)non returns types
"""

#example

#function defination
#non  return type function
def summation():
    print(1+1)
#function calling
summation()

# #return types function
# def summation2():
#     return  1+2
#
# print(summation2())

#argument and paraeteres :-

# def shop(item1,item2):
#     print(item1,item2)
#
# shop("onuion","leimon")

# args Argument:- (arbitrary positional argumentes)

# def shop(*item):
#     print(*item)
#
# shop("apple ","Banan","leimon","watermelon")
#
# def person(*info):
#     print(info)
#
# person("sumilon biswas",21,"student ","CSE","Diu","programmer")
# print(type(person()))
#
# def person(**info):
#     print(info)
#     print(type(info))
#
# person(name="sumilon",age=21,deparment="cse",university="DIU")
# person(name="Rakib",age=23,department="cse",university="DIu")

# EX-03

# def person(*info):
#     for i in info:
#         print(i)
# person("python",23,"programming","neaderland")

#
# # amer chaila argument aspecific vaba bola dita pare
#
# def person(p_name,p_age,p_deprt,p_languages):
#     print(p_name,p_age,p_deprt,p_languages)
#
# person(p_name="sumilon biswas",p_age=23,p_deprt="CSE",p_languages="computer programing languages ")
# person(p_name="Rakib hassan vai",p_age=26,p_deprt="CSE",p_languages="it support engineering")
# person(p_name="Ripon sarker",p_age=28,p_deprt="CSE",p_languages="SQ engineering")
# person(p_name="Rimie",p_age=25,p_deprt="CSE",p_languages="python developer")
# person(p_name="sumi",p_age=27,p_deprt="CSE",p_languages="java developer")
#
# def person(**info):
#     for i ,j in info.items():
#         print(i,j)
#
# person(name="Rakib islam",age=34,Gender="male",location="dhaka")

# def shop(item1,item2):
#     print(item1,item2)
#
# shop("onion","potu")
# shop("cherry","watermelon")
# shop("apple","oranges")

# args arguments :-(arbitrary positional arguments)

# def shop(*item):
#     print(item)
#
# shop("apply","cherry","watermelon","orangs","lemion")
#
# def shop(*item):
#     print(item)
#
# shop("apple","banana","jerry","cherry","watermelon")

# exaple:- 03

# def person(*info):
#     print(info)
#
# person("sumilon","21","male","CSE","Dhaka")
#
# def employee(*info):
#     print(info)
#
# employee("sumilon","23","python developer","reading book")
# employee("anika","23","php developer","dance")
# employee("Rofices","23","python","eating food")

def person(*info):
    for i in info:
        print(i)
person("Ration",23,"teacher","Dhaka university")
person("lemion",24,"student","Khulna university")
person("likhon",24,"student","patukhali university")
