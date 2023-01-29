
# craete a function

# def myfun():
#     print("HI !")
#
# myfun()

# def myfun(name):
#     print(f"hi.!{name}")
#
# myfun("sumilon biswas anik")

# function * args

# def myfunction(a,b,*args):
#     print(a)
#     print(b)
#     print(args)
#     print(type(args))
#
# myfunction('sumilon',"biswas","likhon","shipon","shopon","Ritu","sabbir","jibon ")

# def myfunction(*n):
#     print(n)
#
# myfunction("sumilon",'Tanbir',"nayem islam","Ranku","shipon","milon","likhon")
#
# def person_list(**n):
#     print(n)
#
# person_list(name="sumilon biswas",Roll=25,department="CSE",location="Dhaka")
# person_list(name="anik",Roll=23,department="cse",location="Dhaka")
#
# person_list(name="lemion",Roll=25,department="EEE",location="Dhaka")

# std_list={}
# def student_info(**info):
#     for keys,item in info.items():
#
#         std_list[keys]=item
#
#     print(std_list)


# student_info(name="sumilon biswas",Roll=21,department="CSE means(computer secinece and engireening)",hobby="Readding book")
# print("\n")
# student_info(nam="anika Rahmane",Roll=25,department="EEE",hobby="sing song")
# print("\n")
#
# student_info(name="Rakib Hassan",Roll=27,department="CSE",hobby="travale")
# print("\n")
# student_info(name="tanbir islam",Roll=33,department="cse",hobby="dicussion bussiness ")
# print("\n")
# student_info(name="noyon islam", Roll=27,department="cse" ,hobby="developer")


# std_list={}
# #add date of dictionary
# def student_information(**n):
#     for keys , item in n.items():
#         std_list[keys]=item
#
#     print(std_list)
#
# #seaching data in dictionary
# def seach(rn):
#     for keys,item in std_list.items():
#         if std_list[keys].Roll == rn:
#             print(std_list[keys],[item])
#     else:
#         print("Invalid information ")
#
# student_information(name="sumilon biswas",Roll=21,department="CSE means(computer secinece and engireening)",hobby="Readding book")
# print("\n")
# student_information(nam="anika Rahmane",Roll=25,department="EEE",hobby="sing song")
# print("\n")
#
# student_information(name="Rakib Hassan",Roll=27,department="CSE",hobby="travale")
# print("\n")
# student_information(name="tanbir islam",Roll=33,department="cse",hobby="dicussion bussiness ")
# print("\n")
# student_information(name="noyon islam", Roll=27,department="cse" ,hobby="developer")
#
# print("searching data")
# seach(25)

#
# std_list=[]
#
# def add_std_info(*n):
#         std_list.append(n)
# print(std_list)
#
# add_std_info("sumilon",32,"cse")
# print("\n")
# add_std_info("anik",25,"EEE")
# print("\n")
# add_std_info("sumiya",27,"CSE")
#
# from functools import partial
#
# def addition(a,b):
#         return  a+b
#
# res=partial(addition,20,30)
# print(res(20,2))