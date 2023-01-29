"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""

# rows=int(input("Input rows values :"))
#
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(i, end=" ")
#     print("\r")
#
# """
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
#
# """
#
# rows=int(input("Input rows values :"))
#
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print("\r")

"""
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5
"""
# rows=int(input("Inputs values of rows :"))
# k=1
# for i in range(rows,0,-1):
#     for j in range(1,i+1):
#         print(k,end=" ")
#     k=k+1
#     print("\r")

"""
5 5 5 5 5 
5 5 5 5 
5 5 5 
5 5 
5
"""

# rows=int(input("Input rows values :"))
#
# k=rows
# for i in range(rows,0,-1):
#     for j in range(1,i+1):
#         print(k,end=" ")
#     print("\r")

"""
0 1 2 3 4 5 
0 1 2 3 4 
0 1 2 3 
0 1 2 
0 1
"""

# rows=int(input("Input a number of rows :"))
#
# for i in range(rows,0,-1):
#     for j in range(i+1):
#         print(j ,end=" ")
#     print("\r")

"""
1 
3 3 
5 5 5 
7 7 7 7 
9 9 9 9 9
"""

# rows=int(input("Input  rows values :"))
# i=1
# while i<= rows:
#     j = 1
#     while j <= i:
#         print(i*2-1,end=" ")
#         j =j+1
#     i=i+1
#     print("\r")


"""
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1
# """
# rows=int(input("Inputs rows values :"))
#
# for i in range(rows,0,-1):
#     for j in  range(i):
#         print(i,end=" ")
#     print("\r")
#

"""
1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1
"""
# rows=int(input("Input rows values :"))
#
# for i in range(rows+1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print("\r")

"""
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
"""
#
# rows=int(input("Input rows values :"))
#
# for i in range(0,rows+1):
#     for j in range(rows-i,0,-1):
#         print(j,end=" ")
#     print("\r")

"""

  
        5 
      4 5 
    3 4 5 
  2 3 4 5 
1 2 3 4 5 

"""

# rows=int(input("Inputs rows value:"))
#
# for i in range(rows+1):
#     num=1
#     for j  in range(rows,0,-1):
#         if j > i:
#             print(" ",end=" ")
#         else:
#             print(num,end=" ")
#         num+=1
#     print("\r")

"""
          1 
        1 2 
      1 2 3 
    1 2 3 4 
  1 2 3 4 5 
"""

# rows=int(input("Inputs values rows :"))
#
# for i in range(0,rows+1):
#     num=1
#     for j in range(rows,0,-1):
#        if j > i:
#            print(" ",end=" ")
#        else:
#            print(num,end=" ")
#            num +=1
#     print("\r")

"""
1 2 3 4 5 
2 2 3 4 5 
3 3 3 4 5 
4 4 4 4 5 
5 5 5 5 5
"""

# rows=int(input("Input rows values :"))
#
# for i in  range(1,rows+1):
#     for j in range(1,rows+1):
#         if j <= i:
#             print(i,end=" ")
#         else:
#             print(j,end=" ")
#     print("\r")


"""
1  
2  4  
3  6  9  
4  8  12  16  
5  10  15  20  25  
6  12  18  24  30  36  
7  14  21  28  35  42  49  
8  16  24  32  40  48  56  64  
# """
# rows=int(input("Inputs rows values :"))
#
# for i in  range(1,rows+1):
#     for j in range(1,i+1):
#         print(i*j,end=" ")
#     print("\r")

"""
    Simple half pyramid pattern: 
* 
* * 
* * * 
* * * * 
* * * * * 
"""

# rows=int(input("Inputs values rows :"))
#
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print("\r")
"""
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
"""

# rows =int(input("Inputs rows values:"))
# for i in range(1,rows+1):
#     for j in range(rows,0,-1):
#
#         if j > i:
#             print(" ",end=" ")
#         else:
#             print("*",end=" ")
#     print("\r")

"""
* * * * *  
* * * *  
* * *  
* *  
*
"""

# rows=int(input("Input rows values :"))
# for i in range(rows,0,-1):
#     for j in  range(1,i+1):
#         print("*", end=" ")
#     print("\r")

"""
        * * * * * * 
         * * * * * 
          * * * * 
           * * * 
            * * 
             * 
"""

# rows=int(input("Inputs rows values :"))
# k=2*rows-1
#
# for i in range(rows,-1,-1):
#     for  h in range(k,0,-1):
#         print(end=" ")
#     k +=1
#     for j in range(i+1):
#         print("*",end=" ")
#     print("\r")


rows=int(input("input rows valus:"))
k=2*rows -1
for  i in range(rows,-1,-1):
    for j in range(k,0,-1):
        print(end=" ")
    k=k+1
    for h in range(i+1):
        print("*",end=" ")
    print("\r")