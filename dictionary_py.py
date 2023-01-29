
#Dictionary


# a ={
#     "cartoon1":"mina",
#     "cartoon2":"Doremon",
#     "cartoon3":"chinchar",
#     "cartoon4":"tom and jerry",
#     }
# print(type(a))
# print(a)
# print(a.keys())
# print(a.values())

#mixed key

# c={
#     "name":"sumilon biseas anik",
#     "age":34,
#     100:"full marks",
#     5.7:"his heights"
# }
# print(c)

# d=dict({"name":"sumilon biseas","age":22,"height":5.5,"department":"cse"})
# print(d)

#nested_dict

# student={
#     1:{"name":"sumilon biswas","age":20,"sex":"male"},
#     2:{"name":"shampu","age":45,"sex":"female"},
#     3:{"name":"Rakib","age":29,"sex":"male"},
#     4:{"name":"tanbir islam","age":22,"sex":"male"}
# }
# print(student)
# print(student[3])
# print(student[3]["name"])
# print(student[1]["name"])
# print(student[1]["sex"])
# print(student[3]["sex"])
# print(student[4]["name"])
#
# a={
#     "name1":"Rakib",
#     "name2":"hassan",
#     "name3":"Ratul"
# }
# a["name4"]="sumilon biswas anik"
# print(a)

# criketer_list={
#     "name1":"sakib all hasan",
#     "name2":"mash",
#     "name3":"dependable",
#     "name4":'"client killer'
# }
# criketer_list["name5"]="power hiter"
# print(criketer_list)
#
# team_list={
#
#     "name1":"Rakib hassan vai",
#     "name2":"sumilon biswas anik",
#     "name3":"shafin",
#     "name4":"amin sir"
# }
# team_list["name5"]="jerry haq"
# print(team_list)

# team_list={
#
#     "name1":"Rakib hassan vai",
#     "name2":"sumilon biswas anik",
#     "name3":"shafin",
#     "name4":"amin sir"
# }
# # del  team_list["name2"]
# # print(team_list)
# team_list.pop("name2")
# print(team_list)


#Dictionary data access  for loop using

# a={"name":"Rakib","age":34,"place":"Dhaka"}
#
# # for i in a:
# #     print(i)
# # for i in a:
# #     print(a[i])
# for i in a:
#     print(a[i])
#
# friend_list={"name1":"anik","name2":"akash","name3":"monju","name4":"Rubel","name5":"Hassan","name6":"tanbir"}
#
# for i in friend_list.items():
#     print(i)

#nested Dictonary

# employee={
#     1:{"name":"sumilon biswas","age":20,"profession":"student"},
# #     2:{"name":"shipon","age":30,"profession":"Doctor"},
# #     3:{"name":"likhon","age":24,"profession":"teacher"}
# # }
# #
# # # print(employee)
# #
# # # for i , j in employee.items():
# # #     print(employee[i])
# # #     print("================")
# # #     print(j)
# #
# # for i in employee:
# #     if type(i) is dict:
# #         for j in i:
# #             print(j)
# # print(employee[i])
#
# # take user input

# n = int(input("How many personl information do you want to add :"))
# person={}
# for item in  range(n):
#     key=input("Input a key :")
#     values=input("Input a values :")
#     person.update({key:values})
#
# print(person)

n=int(input("Input number of information :"))
person={}
for item in range(n):
    key=input("Input keys :")
    values=input("Input values :")
    person.update({key:values})

print(person)


