
#function

"""
    structured of function

    two part of function
    1:functine difinection
    2:function calling

1:functine difinection
    keyword||function_name||parensthis||colon

    def function_name():
            Block of code
function calling
  function()


"""

# def myfunction():
#     print("HI! python programing most populare in the world")
#
# myfunction()
#
# #Example:
# def summation():
#     print(1+1)
#
# summation()
# def substraction():
#     print(2-1)
#
# substraction()

## return function

# def summation():
#     return "python is best programing languages"
#
# print(summation())
# a=True
# b=True
# c=True
#
# if (a == True) and (b == True) and \
#         (c == True):
#           print("Continuation of statements")

# a=10
# b=20
# c=30
# if(a==10)and(b==20) and \
# (c==30):
#     print("all condition is true!")

# print(20+20)
# print(20-10)
# print(20*10)
# print(20/10)

# def shop(*name):
#     print(name)
#
# shop("onion","pasta","metton","kisher")
# print(type(shop()))
#
# def person(*info):
#     for i in info:
#         print(i)
#
# person("Sumilon","21","male","Dhaka")

# def employee(*details):
#     for item in details:
#         print(item)
#
# employee("sumilon",45,"male","dhaka","cse")
# print("===================")
# employee("tanbir islam",22,"male","dhaka","cse")
# print("==========================")
# employee("joya bain",23,"male","dhaka","cse")

def person(per_name,per_age,per_gen,per_local):
    print(per_name," ",per_age," ",per_gen," ",per_local)

person(per_name="sumilon biswas anik",per_age=21,per_gen="male",per_local="Dhaka")
person(per_name="omie",per_age=23,per_gen="male",per_local="Dhanmondie")