
# using the program while loop
#
# i = 1
# j = 1
# while i <= 4:
#     while j<=3:
#         print("i ",i,"j ",j,sep=" ")
#         j +=1
#     else:
#         print("j is end")
#     i+=1
#     j=1

# a = 1
# b = 1
# while a < 5:
#     while b <= 4:
#         print("a ",a," b",b,sep=" ")
#         b+=1
#     else:
#         print(" b is end")
#     a +=1
#     b=1

#Using the for in pythons

# a="Bangladesh"
# for i in a:
#     print(i)
# print("program end")

# myname='sumilon biswas anik'
# for item in myname:
#     print(item)
#
# print("wellcome program ====")

# jodie ami akta name 10 bar print korta  chai thaila amer loop use korbo
#example

# for item in range(11):
#     print("Bangladesh cricket team...")

#nother example

# for i in  range(1,11,3):
#     print(i)
# for i in range(5):
#     # print(i,end=" ")
#     print(i)
# for i in range(2,5):
#     print(i)
# print("=======================")
# for i in range(2,10,1) :
#     print(i)

#nested loop

# for i in range(1,4):
#     for j in range(1,4):
#         print("i ",i,"j ",j,sep=" ")

# for i in range(1,7):
#     for j in range(1,4):
#         print("i=",i,j,':'"python programing")

# for i in range(0,2):
#     for j in range(5):
#         print("i-",i,"j-",j,end=" ")
#
# #Example :
#
# # for i in range(5):
# #     for j in range(4):
# #         print("i =",i,"j=",j, end=" ")
# #     print(" ")
#
# for i in range(5):
#     for j in range(5):
#         print("i=",i,"j=",j,end=" ")
#     print(" ")

#squared pattren  program

# for i in range(5):
#     for j in range(4):
#         print(" +",end=" ")
#     print(" ")

#using foor loop solve pattren problem
#
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# rows=int(input("Input rows values :"))
#
# for i in range(1,rows+1,1):
#     for j in range(1, i+1,1):
#         print(i,end=" ")
#     print("\r")
#

#another pattern program solve

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# rows=int(input("Input a number rows :"))
#
# for i in range(1,rows,1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print("\r")

# another pattren problem selve
# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5

# rows=int(input("input number of pattern :"))
# b=0
# for i in range(1,rows+1,1):
#     b+=1
#     for j in range(1,i+1,1):
#         print(b,end=" ")
#     print("\r")

# another pattern program
# 5
# 5 5
# 5 5 5
# 5 5 5 5
# 5 5 5 5 5


# rows=int(input("Input number of rows :"))
#
# num=rows
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(num,end=" ")
#     print("\r")
#another problem solve pattern
# 5 5 5 5 5
# 5 5 5 5
# 5 5 5
# 5 5
# 5
#
# rows=int(input("Input number of rows :"))
#
# num=rows
#
# for i in range(rows,0,-1):
#     for j in range(i+1,0,-1):
#         print(num,end=" ")
#     print("\r")

# rows=int(input("Input number of rows :"))
# num=rows
# for i in  range(1,rows+1,1):
#     for j in range(1,i+1,1):
#         print("*",end=" ")
#     print("\r")
# for i in range(rows,0,-1):
#     for j in range(i+1,0,-1):
#         print("*",end=" ")
#     print("\r")

#Another inverted half pyramid pattern with number
# output show

# 0 1 2 3 4 5
# 0 1 2 3 4
# 0 1 2 3
# 0 1 2
# 0 1

# rows=int(input("Input a number of rows :"))
# for i in range(rows,0,-1):
#     for j in range(0,i+1):
#         print(j,end=" ")
#     print("\r")


# rows=int(input("Input a number of rows :"))
# for i in range(rows,0,-1):
#       for j in range(0,i+1):
#          print(j,end=" ")
#       print("\r")

# 1
# 3 3
# 5 5 5
# 7 7 7 7
# 9 9 9 9 9

# rows=int(input("INput a number of value rows :"))
# i=1
# while i <= rows:
#     j=1
#     while j <= i:
#         print((i*2-1),end=" ")
#         j +=1
#     i +=1
#     print("\r")

# 1
# 3 3
# 5 5 5
# 7 7 7 7
# 9 9 9 9 9

# rows=int(input("Input a number of rows :"))
# i=1
# while i <= rows:
#     j=1
#     while j<=i:
#         print((i*2-1),end=" ")
#         j +=1
#     i +=1
#     print("\r")

#Reverse number pattern
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1

# rows=int(input("Input number of rows :"))
#
# for i in range(rows,0,-1):
#     num=i
#     for j in range(1,i+1):
#         print(num,end=" ")
#     print(" \r")

# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1
# rows=int(input("Input number of rows :"))
#
# for i in range(rows,0,-1):
#     num=i
#     for j in range(1,i+1):
#         print(num,end=" ")
#     print(" \r")

#Reverse Pyramid of Numbers
#
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1
# rows=int(input("Input number of rows :"))
# for i in range(1,rows+1):
#     for j in range(i,0,-1):
#         print(j ,end=" ")
#     print("\r")

# rows=int(input("Input number of rows :"))
#
# for i in  range(1,rows+1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print("\r")

#Another reverse number pattern

#output display show

# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

rows=int(input("Input number of rows :"))
