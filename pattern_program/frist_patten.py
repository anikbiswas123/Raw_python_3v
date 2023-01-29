# demonstrate star pattern

# def pyptta(n):
#     #outer loop can handle of rows
#     for i in range(0,n+1):
#         #value cjanaging outer loop
#         for j in range(0,i+1):
#             print(" * ",end=" ")
#             j +=1
#
#         print("\r")
# n =5
# pyptta(n)

# def patten_pro(n):
#      # outer loop starte can handle of rows defines
#      for i in  range(0,n+1):
#          for  j in range(0,i+1):
#              print(" * ",end=" ")
#              j += 1
#          print("\r")
#
# n = 5
# patten_pro(n)
#
# def mypart(n):
#     mylist = []
#     for i in range(1,n+1):
#         mylist.append("*"*i)
#     print("\n".join(mylist))
#
# n=4
# mypart(n)

# pattren program

#outer loop declare of rows
# for i in range(1,5+1):
#     for j in range(1,i+1):
#         print(" * ",end=" ")
#         j += 1
#     print("\r")

mylist =[]

# for i in range(1,5+1):
#     mylist.append(" *" * i)
# print("\n".join(mylist))

# def pytta(n):
#     if n == 0 :
#         return
#     else:
#         pytta(n-1)
#         print(" * " * n)
#
# pytta(5)

# n = 5
# i=1
# j=0
#
# while i<= n :
#      while j <= i-1:
#          print(" * ",end=" ")
#          j += 1
#      print("\r")
#      j= 0;i+=1
#
#
# n=5
# i=1
# j=0
# while i<=n:
#      while j <= i-1:
#          print(" * ",end=" ")
#          j += 1
#      print("\r")
#      j= 0;i+=1

# def pyttan(n):
#     k = 2* n- 2
#
#     for i in range(0,n):
#         for j in range(0,k):
#             print(end=" ")
#         k =k-2
#         for j in range(0, i+1):
#             print(" * ", end=" ")
#         print("\r")
# pyttan(5)

# def pypart2(n):
#     # number of spaces
#     k = 2 * n - 2
#
#     # outer loop to handle number of rows
#     for i in range(0, n):
#
#         # inner loop to handle number spaces
#         # values changing acc. to requirement
#         for j in range(0, k):
#             print(end=" ")
#
#         # decrementing k after each loop
#         k = k - 2
#
#         # inner loop to handle number of columns
#         # values changing acc. to outer loop
#         for j in range(0, i + 1):
#             # printing stars
#             print("* ",end="")
#
#         # ending line after each row
#         print("\r")
#
#
# # Driver Code
# n = 5
# pypart2(n)


# n= 5
# k = 2 * n-2
#
#
# #definess of spease values
#
# for i in range(0,n):
#     for j in range(0,k):
#         print(end=" ")
#     k = k - 2
#
#     for l in range(0,i+1):
#         print(" *",end=" ")
#     print("\r")


# height = 5
# for row in range(1, height+ 1):
#     print(" " * (height - row) +"*" * row)
n = 5
for i in range(0,n):
    for j in range(0, i+1):
        print("*", end =" ")
    print("\r")

    # Printing
    # Triangle
    # Solution:

    # for i in range(1, 20):
    #     for j in range(i, 20):
    #         print(" ", end=" ")
    #     print(' * ' * i)
    # print("\n")

# for i in range(1,20):
#     for j in range(i,20):
#         print(" ",end="")
#     print(" * " *  i)
# print("\n")



