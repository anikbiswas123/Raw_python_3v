# example :-01
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
#
# rows=int(input("Input rows values :"))
#
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(i , end=" ")
#     print(" ")

# partten :-02
"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

# rows=int(input("Inputs rows values :"))
#
#
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(j ,end=" ")
#
#     print(" ")

# patten:-03

"""
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5
# """
# rows=int(input("Input rows values :"))
# b=0
# for i in range(rows,0,-1):
#     b +=1
#     for j in range(i,0,-1):
#         print(b,end=" ")
#     print(" ")
#
# rows=int(input("Input rows values :"))
# b=0
# for i in range(rows,0,-1):
#     b +=1
#     for j in range(i,0,-1):
#         print(b,end=" ")
#     print(" ")

#pattren:-05
"""
5 5 5 5 5 
5 5 5 5 
5 5 5 
5 5 
5
"""
# rows=int(input("Input rows values :"))
# r=rows
#
# for i in range(rows,0,-1):
#     for j in range(i,0,-1):
#         print(r,end=" ")
#     print(" ")

#pattren :- 07
""""
0 1 2 3 4 5 
0 1 2 3 4 
0 1 2 3 
0 1 2 
0 1
# """
# rows=int(input("Input rows values :"))
#
# for i in range(rows,0,-1):
#     for j in range(i+1):
#         print(j,end=" ")
#     print(" ")
#
# rows=int(input("Inputs rows values :"))
# for i in range(rows,0,-1):
#     for j in range(i+1):
#         print(j,end=" ")
#     print(" ")

# rows=int(input("Input rows valus :"))
# for i in range(1,rows+1):
#     for j in  range(i+1):
#         print((i*2-1),end=" ")
#     print("\r")

# rows=int(input("Inputes rows values :"))
# i=1
# while i <=5:
#     j =1
#     while j  <=i:
#         print((i*2-1),end=" ")
#         j +=1
#     print(" ")
#     i +=1

#pattren :-07
"""
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1
"""
# rows=int(input("Input rows values :"))
#
# for i in range(rows,0,-1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print(" ")

#pattren:07
"""
1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1

"""

# rows=int(input("Inputs rows values :"))
#
# for i in range(1,rows+1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print(" ")
# rows=int(input("Input rows values :"))
# for i in range(1,rows+1):
#     for j in range(i,0,-1):
#         print(j ,end=" ")
#     print(" ")
#

#pattren program :-
"""
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
"""
# rows=int(input("Input rows:"))
# for i in range(0,rows+1):
#     for j in range(rows-i,0,-1):
#         print(j,end=" ")
#     print(" ")
#
# rows=int(input("Input rows values :"))
# for i in range(0,rows+1):
#     for j in range(rows-i,0,-1):
#         print(j,end=" ")
#     print(" ")

#pattren:-
"""
          1 
        1 2 
      1 2 3 
    1 2 3 4 
  1 2 3 4 5 
"""
# rows=int(input("Input rows values :"))
#
# for i in range(1,rows+1):
#     num=1
#     for j in range(rows,0,-1):
#
#         if j > i:
#             print(" ",end=" ")
#         else:
#             print(num,end=" ")
#             num +=1
#
#     print(" ")

# rows=int(input("Inputes rows values :"))
#
# for i in range(1,rows+1):
#     num=1
#     for j in range(rows,0,-1):
#
#         if j > i :
#             print(" ",end=" ")
#         else:
#             print(num,end=" ")
#             num+=1
#     print(" ")

#pattren:-08
""""
1 2 3 4 5 
2 2 3 4 5 
3 3 3 4 5 
4 4 4 4 5 
5 5 5 5 5
"""
# rows=int(input("Inpute rows :"))
#
# for i in range(1,rows+1):
#     for j in range(1,rows+1):
#         print(j,end=" ")
#     print(" ")

# rows=int(input("Inpute rows :"))
# for i in range(1,rows+1):
#     for j in range(1,rows+1):
#         if j <=i:
#             print(i,end=" ")
#         else:
#             print(j,end=" ")
#     print(" ")

#pattren :-
"""
1  
2  4  
3  6  9  
4  8  12  16  
5  10  15  20  25  
6  12  18  24  30  36  
7  14  21  28  35  42  49  
8  16  24  32  40  48  56  64  
"""

rows=int(input("Input rows values :"))

for i in range(1,rows+1):
    for j in range(1,i+1):
        print(i * j ,end=" ")

    print(" ")