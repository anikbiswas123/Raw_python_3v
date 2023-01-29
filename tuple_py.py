
"""
what's is tuple?
Ans: tuple is collection of object it separted by comma,It ways to smillary way to list list.manin differences
tuple is immuteable .which is list is imute

syntax=
nameoftuple=()

"""
#
# namelist=("Rakib","sabbir","Rajon","tonmay")
# print(namelist)
# print(type(namelist))
# number=(15,16,5,12.5,9,10)
# print(number)
# print(type(number))

# constructor use kora tuble insert kora ji
# b=tuple(("sumilon","anik",",maniu","shipa","likhon","herry"))
# print(b)

# ciketer=(("tammim","Rahman","sakib","soumy sarker","lition das","Afife"))
# print(ciketer)

#nested tuple

# a=(
#     ("Rakib",25,"lalbag"),
#     ("Rashid",34,"Agimpur"),
#     ("Ratull",26,"kamranmgirchar"),
#     ("tonmoy",24,"Bogura")
# )
# print(a)

"""
jodie akhono tuple maja data ka change/add/delect kora ji naha

tuba jodi kakhonono kora lagh frist tuple ta covert list korta the tuple dat add kora jaba
# """
"""
tuple dynmaic data add kora ji naha eita list convert kora nita hoy
then abar tuple convert kora ji....
 
"""
# fruits=("apple","Oranges","Banana")
# b=list(fruits)
# b.append("cherry")
# fruits=tuple(b)
# print(fruits)

# fname=("sumilon","Tanbir islam","joya bain","sagor")
# name=list(fname)
# name.append("Rakib")
# fname=tuple(name)
# print(fname)
#
# plasces=("Dhaka","Dhanmondie","Mohmmadpur","green road","mirpur")
# a=list(plasces)
# a.append("Barisal")
# plasces=tuple(a)
# print(plasces)

# tuple values access using loop

# a=("apple","Orange","Banana")
#
# for i in a:
#     print(i)

"""
 nested tuple access looping
"""
# print( " ")
# info=(
#      ("rakib",25,"student","Dhaka"),
#      ("onie",27,"student","chandipur"),
#      "Ratul",
#       ("Rashid",26,"student","Sador gahat")
#     )
#
# for i in info:
#     if type(i) is tuple:
#          for j in i:
#              print(j)
#
#     else:
#         print(i)

# info=(
#     ("Rakib",26,"Dhaka"),
#     ("oni",25,"chandpur"),
#     "shiopon",
#     ["sumilon",23,"Barisal"]
#
# )
#
# for i in info:
#     if type(i) is tuple:
#         for j in i:
#             print(j)
#     elif type(i) is list :
#           for j in i:
#               print(j)
#     else:
#         print(i)