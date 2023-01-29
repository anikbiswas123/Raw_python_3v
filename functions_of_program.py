
# def get_net_prices(price,discount):
#     return  price * (1-discount)
#
# net_ptices=get_net_prices(100,0.1)
#
# print(net_ptices)

# def Total_discount_prices(prices,discount):
#     return  prices * discount/100
# net_dicount=Total_discount_prices(200,10)
# print(net_dicount)
#
# def get_net_prices(prices,txt,discount):
#
#     return  prices * (1+txt-discount)
#
# net_prices=get_net_prices(400,0.01,0.2)
# print("net prices of :",net_prices)
#
# def  math_law(a,b):
#     return  a * a + 2*a*b + b*b
# res=math_law(2,3)
# print(res)

# # using lambda function
#
# x=(lambda a,b:a*b+2*a*b+b*b)(2,3)
# print(x)

# import  functools
# #
# # lis =[1, 3, 5, 6, 2]
# #
# # display_result=functools.reduce(lambda a,b:a+b,lis)
# # print("display result :",display_result)
#
# # lis=[12,67,80,70,34,50,60]
# #
# # display_result=functools.reduce(lambda a,b:a+b,lis)
# # print("display result :",display_result)
#
# # lis =[1, 3, 5, 6, 2]
# # display_res=functools.reduce(lambda a,b: a if a>b else b,lis )
# # print(display_res)

# from  functools import reduce
#
# # lis=[23,21,45,98]
#
# display_res=reduce(lambda a,b:a+b,[23,21,45,98] )
# print(display_res)
# from  itertools import accumulate
#
# # lis=[23,21,45,98]
# #
# # a=list(accumulate(lis,lambda x,y: x+y ))
# # print("result is :",a)
#
# res_finally=list(accumulate([23,45,58,90,45,66],lambda x ,y : x+y))
# print("result is ",res_finally)

# ZIP function

# name=["sumilon","Rakib","hassan","ovi"]
# roll=[101,102,103,104]
# age=[21,26,30,45]
#
# info_list=list(zip(name,roll,age))
# print(info_list)

# std_name=["sumilon","tanbir islam","joya bain","sagor sikdar","montu"]
# std_department=["CSE","CSE","CSE","RAC","EEE"]
# std_Roll=[101,102,103,104,105]
# srd_BLOod_gp=['A+',"B+","B+",'A+',"A-"]
#
# list_of_result=list(zip(std_name,std_department,std_Roll,srd_BLOod_gp))
# print("list of result :",list_of_result)

# std_name=["sumilon","anik","jovhan","nishe","pori","likhon"]
# strd_Gpa=[3.50,5.80,3.30,3.99,3.76,4.50]
#
# student_info=list(zip(std_name,strd_Gpa))
# print(student_info)

# std_name=["manjeet","Nikile","shambavie","Astha"]
# std_roll=[4,3,2,1]
#
# display_std=list(zip(std_name,std_roll))
# # print("full information student :",display_std)
# print(set(display_std))


# names = ['Mukesh', 'Roni', 'Chari']
# ages = [24, 50, 18]
#
# for i ,(name,age) in enumerate(zip(names,ages)):
#     print(i,name,age)

# student information
#
# std_name=["sumilon  biswas","joya bain","setu bain","lipe bain","monie bain","Rinku bain"]
# std_roll=[102,103,104,109,1001,106]
# std_GPA=[3.50,3.44,3.70,3.80,3.65,3.90]
#
# for i ,(name,roll,GPA) in enumerate(zip(std_name,std_roll,std_GPA)):
#     print(i,name,roll,GPA)
#

# std_name=["manjeet",'Robie',"shopono","tupon","Rekhion"]
# std_Roll=[9,3,2,5,8]
# std_marks=[60,70,40,80,90]
#
# for i ,(std_nam,std_Roll,std_mark) in enumerate(zip(std_name,std_Roll,std_marks)):
#     print(i,std_nam,std_Roll,std_mark)

#practrial application example

# players_name=["sachin","shewag","Gambir","Dravide","Raina"]
#
# secore=[100,70,60,65,85]
#
# Rankng=[1,18,12,7,20]
#
# for i ,(players_name,secore,Rankng) in enumerate(zip(players_name,secore,Rankng)):
#     print(f"players name : {players_name}, secore  :{secore},  Ranking  :{Rankng}")

languages=["java","python","javascript"]
version=[18,3,6]

res=list(zip(languages,version))
print(res)