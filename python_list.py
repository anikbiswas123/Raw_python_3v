
# a=["I","live","in","dhaka","since","2001"]
# print(a)
# person_name=["sumilon","anik","Liton","santo","sakib","monir","jaman","Shipu"]
# print(person_name)
#
# # list constructor
# b=list(("sumilion","joy bain","Ripon","likhon","potu"))
# print(b)

# mylist=list(("sumilon","Ripon","joya","tanbir islam","apu","melion","shipun"))
# print(mylist)

# friend_list=[]
#
# for i in range(7):
#     b=input("INput a value insert of list :")
#     friend_list.append(b)
# print(friend_list)

# number_list=[]

# for i in  range(10):
#     a=int(input("Input number in list :"))
#     number_list.append(a)
# print(number_list)
#
# sum=0
# for i in number_list:
#     sum=sum+i
# print("total summation of :",sum)

#LISt positive index

# listof=["shajhan","Billal","mirion","jamal","nazir","faruk"]
# print(listof[1])
# print(listof[-1])
# print(listof[1:5])

# b=["shajghan",["Rakib","hassan","Hossain"],"Billal",["sumilon","tanbir","joya"],"jamal","nazir"]
# print(b[1][0])
# print(b[1][1])
# print(b[1][2])
# print("Index number 3")
# print(b[3][0])
# print(b[3][1])
# print(b[3][2])
# print(b[5])

#nested indexing of list
# b=[["sakib all hassain","sumoy sarkar","liton das"],["imran","porish","mileon","kona","puja"],["sakib khan","apu biswas","Bubali","sabniur"],["squord","Bex","paran up"]]
#
# print(b[3][2])
# print(b[2][3])
# print(b[1][2])
# print(b[-4][-3])
# print(b[-3][-4:-1])
# print(b[-2][-1])

# list data insert / add
#
# fruits=["Banan","pranges"]
# print(fruits)
# fruits.append("cherry")
# print(fruits)
# fruits.insert(1,"watermelon")
# print(fruits)

# list extend

# list1=["apple","orange","chery"]
# list2=["watermelon","Banana","pineapple"]
# list1.extend(list2)
# print(list1)
# list1=["apple","orange","chery"]
# list1.extend(("watermelon","jakfruits","Banana"))
# print(list1)

# list1=["Banana","orange","fruits"]
# list1.extend(["pineapple","jijuk","melon","gavuse","etc"])
# print(list1)

#list values changes

# f_list=["Kamol","tushar","sumon sikdar ","sagor sikder","melon","topel","jerrf"]
# f_list[2]="tanbir islam"
# # print(f_list)
# print(f_list.clear())

# access list values using for loop

# a=["apple","Banana","oranges","guava"]
# for i in a:
#     print(i)

# list1=["apple","Banana",["watermelon","jinkfood","sweet"],"cherry",["lipul","h","j"],"poltye"]
#
# # for i in  list1:
# #     print(i)
# #     for j in i:
# #         print(j)
#
# for i in list1:
#     if type(i) is list:
#          for j in i:
#              print(j)
#     else:
#         print(i)

# person_list=["supti",["Imran","milke","jerry"],"potue",["karnel","janik ","Abooks"],"Rebbook",["sakib al hassain","liton","sumiya sarkhar","Rahman"]]
#
# # for i in person_list:
# #     print(i)
#
# for i in person_list:
#     if type(i) is list:
#         for j in i:
#             print(j)
#     else:
#         print(i)

# list length

# fruits_list=["Appple","Banana","cherry","watermelon","pianapple"]
# print(len(fruits_list))
# numbers=[2,4,7,9,4,7,8,9]
# print(len(numbers))
#
# fruits_list=["Apple","Banana","cherry","watermelon","pianapple"]
# if "Apple" in fruits_list:
#     print("yes!")
# else:
#     print("No!")
#
# if "sumilon" in fruits_list:
#     print("yes")
# else:
#     print("No")
# membership list
# if "sumilon" not in fruits_list:
#     print("not in")
# else:
#     print("in")
# if "apple" not in fruits_list:
#     print("not in")
# else:
#     print("yes!")

# fruits_list=["apple","cherry","watermelon","Banana"]
# list2=fruits_list.copy()
# print(list2)

# person_name=["sumilon biswas","Banana","pianapple","watermelon"]
# list3=person_name.copy()
# print(list3)

# fruits_list=["apple","Banana","komla",["watermelon","pianapple","chery"],"oranges"]
# b=[]
#
# for item in fruits_list:
#     # print(item)
#     if type(item) is list :
#         b=item.copy()
# print(b)

# fruits_list=["apple","Banana","komla",["watermelon","pianapple","cherry"],"orange"]
#
# b= []

# b=[20,10,30.5,15,12]
# b.sort()
# print(b)
#
# a=["Apple","Banana","Orange"]
# a.reverse()
# print(a)
#
# fruits_list=["apple","Banana","komla","watermelon","pianapple","cherry","orange"]
#
# fruits_list.sort(reverse=True,key=len)
# print(fruits_list)

# b = [20, 10, 30.5, 15, 12]
# print(sum(b))
# print(sorted(b))

# # zip function
# Roll=[101,102,103,104,105]
# name=["Rakib","sumilon","Ripon","jumal","Ripon"]
# print(list(zip(name,Roll)))
# # print(tuple(zip(name,Roll)))


# person_name=["sumilon","anik","shipon","Ripon"]
# sallary =[20000,30000,400000,40000]
# print(sum(sallary))
# Blood_g=['A+',"B+","B","A-"]
# post_title=["programer","learner","photographer","freelearncer"]
# sl=['01','02','03','04']
# print(list(zip(sl,person_name,sallary,Blood_g,post_title)))

# EX: taka auser input list input:12,35,9,56,24 output=24,35,9,56,24

# x=list(map(int,input("Enter some number :").split()))
# print(x)
# size=len(x)
# print(size-1)
# print(size[0])
# print(x[6])

#EX:take user input list 12,35,9,56,24 output=24,35,9,56,24

# x=list(map(int,input("Input some of number :").split()))
# print(x)
# size=len(x)
# temp=x[0]
# x[0]=x[size-1]
# x[size-1]=temp
# print(x)

# using list and make it uppercase
# person_name=["sumilon","mou","late","haron","Ripon"]
# per_name=[]
# for i in person_name:
#     per_name.append(i.upper())
# print(per_name)

#using list and inser other list make to it lowercase

# p_name=["SUMILON","APINA","MINKA","DULAL","ASIM"]
# insert_p=[]
#
# for item in p_name:
#     insert_p.append(item.lower())
#
# print(insert_p)

# p_name=["sumilon biswas anik","anik","tanbir islam","joya bain","Ripon gain","shopon gain"]
# update_name=[]
# for i in p_name:
#     update_name.append(i.capitalize())
# print(update_name)


