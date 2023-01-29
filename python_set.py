
# decribe of python set

# a={"Rakib","sumilon","tanbir islam","jahudal","komal"}
#
# print(a)
#
# a={"Rakib","sumilon","tanbir islam","jahudal","sumilon","komal"}
# print(a)
#
# aa=set(("Rakib","hasan","topu"))
# print(aa)
#
# a = {"Rakib","Hasan",("jerin","student",88),2,3.5}
#
# for i in a:
#     if type(i) is tuple:
#         for j in i:
#            print(j)
#     else:
#         print(i)
#
# print(a)
#
# # aa={"Ripon","shipon",("sumilon","student",21,"Diu","cse"),"tumol","miron","janto"}
# #
# # for i in aa:
# #     if type(i) is tuple:
# #         for j in i:
# #             print(j)
# #     else:
# #         print(i)
# #
# # print(aa)

# b={"apple","orange","banana"}
# print(b)
# b.add("watermelon")
# print(b)
# b.add("cherry")
# print(b)


# set join /concaterate

# fruits={"apple","watermelon","cherry"}
# abb={"cherry","juknfruits","lipuon"}
# fruits.update(abb)
# print(fruits)

# friend1={"anik","tanbir","joya"}
# friend2={"sagor","lipu","tupon"}
# friend1.update(friend2)
# print(friend1)


#union set

# A={1,2,3,5,8}
# B={2,6,7,8}
# c=A | B
# print(c)

# friends_name={"sumilon","anika","jibon","tanbir"}
# friends_name1={"sumilon","shok","jinbon","joya bain"}
# Result=friends_name | friends_name1
# print(Result)

# #intersection
#
# # a={1,2,3,5,8}
# # b={2,6,7,8}
# # c= a & b
# # print(c)
#
# friend_name={"sumilon","anik","jibona","liton"}
# friend_name1={"sumilon","anik","labonay","pakhi"}
#
# Result=friend_name & friend_name1
# print(Result)

# friend_name={"sumilon","anik","jibona","liton"}
# friend_name1={"sumilon","anik","labonay","pakhi"}
# union=friend_name | friend_name1
# print(union)

# # Differences set
# a={1,2,3,5,6,7}
# b={2,4,6,8}
# finall_res= a - b
# print(finall_res)

# num1={2,4,6,8}
# num2={1,2,3,5,6,7}
# result=num1 - num2
# print(result)

#symmetic differences
#
# a={1,2,3,5,6,7}
# b={2,4,6,8}
# print(a^b)