
# def function1():
#     print("please! subscribe my channel !")
#
# function2=function1
# del  function1
# function2()

# def decl(func1):
#     def nowexcet():
#         print("Executing now !")
#         func1()
#         print("Excuted function")
#     return  nowexcet
#
# def  who_is_herry():
#     print("Herry is a good programer.")
#
# display_dect=decl(who_is_herry)
#
# display_dect()


# Python program to illustrate functions
# # can be passed as arguments to other functions
# def shout(text):
#     return text.upper()
#
#
# def whisper(text):
#     return text.lower()
#
#
# def greet(func,func1):
#     # storing the function in a variable
#     greeting = func("""Hi, I am created by a function passed as an argument.""")
#     greeting2=func1("Hi! Bangladesh cricket is very bad time spend of!")
#     print(greeting)
#     print(greeting2)
#
#
#
# greet(whisper,shout)

def addition(x,y):
    return  x + y
def substruction(x,y):
    return x-y
def multipaltion(a):
    return a * a
def division(a,b):
    return a / b

def get_finall_result(funch1,funch2,funch3,funch4):

    result1=addition(20,20)
    result2=substruction(30,10)
    result3=multipaltion(20)
    result4=division(50,40)

    print("======================")
    print("Result is addition :",result1)
    print("Result is substraction :",result2)
    print("Result is multpaltion :",result3)
    print("Result is division :",result4)


    def now_excuted():
        print("program now excuted.....")

    return now_excuted

display_funct=get_finall_result(addition,substruction,multipaltion,division)

display_funct()

print("=========================")

def meassages():
    print("Hard working always successfull in life !")
def hello_word():
    print("hello world is frist program in all programing languages.")
def show_display():
    print("successfully in life ..!")

def full_information_fun(fun1,fun2,fun3):
    fun1()
    fun2()
    fun3()
    def now_excuted():
        print("now programing is excuted for this time...!")

display_for_all=full_information_fun(meassages,hello_word,show_display)
display_for_all()



