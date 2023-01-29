
# mylist=[2,3,4,5,6,7,8,9]
#
# # def is_greaterthen_5(a):
# #     return  a > 5
# def is_lessthan_5(a):
#      return  a < 5
#
# myfilter=tuple(filter(is_lessthan_5,mylist))
#
# print(myfilter)
#
# nums = [5, 10, 23, 64, 42, 53, 93, 2, 0, -14, 6, -22, -13]
#
# #filter all the odd number in the list
#
# # dis_odd_num=list(filter(lambda x :x%2 !=0 ,nums))
# # print("this is number of list odd number =",dis_odd_num)
#
# # filter all the even number in the list
# dis_even_num=list(filter(lambda x: x % 2 ==0,nums))
# print("this is list that so even number me.",dis_even_num)

# numbers=[3,4,5,9,7,6,77,88,93,85,90,-12,-19,65,54]
#
# #filter all the the ood number in the list
#
# dis_odd_num=list(filter(lambda x : x % 2 !=0,numbers))
# # print(dis_odd_num)
# numbers=[3,4,5,9,7,6,77,88,93,85,90,-12,-19,65,54]
#
#
# dis_mylist=list(filter(lambda x :x%2==0,numbers))
# print(dis_mylist)
#
# books = [
#
#    {"Title":"Angels and Demons", "Author":"Dan Brown", "Price":500},
#
#    {"Title":"Gone Girl", "Author":"Gillian Flynn", "Price":730},
#
#    {"Title":"The Silent Patient", "Author":"Alex Michaelidis", "Price":945},
#
#    {"Title":"Before I Go To Sleep", "Author":"S.J Watson", "Price":400}
#
#    ]
#
# def func(book):
#
#    if book["Price"] > 500:
#
#        return True
#
#    else:
#
#        return False
#
# filtered_object = filter(func, books)
#
# for d in filtered_object:
#
#    print(dict(d)["Title"])

# Books = [
#     {"Title":"angele Bamones","Author":"Dan Brrowrd","prices":500},
#     {"Title":"Gony gail","Authorits":"John Doie","prices":760},
#     {"Title":"book pites","Authority":"Rabin son","prices":990},
#     {"Title":"Hard working win the game","Authority":"ppipes jos","prices":450}
# ]
#
# def myfunction(Books):
#     if Books["prices"] > 500:
#         return True
#     else:
#         return  False
#
# object_Dict=filter(myfunction,Books)
#
# for d in object_Dict:
#     print(dict(d)["Title"])

Books =[
        {"Title":"padman","Author":"Guido cherry","prices":500}
       ]