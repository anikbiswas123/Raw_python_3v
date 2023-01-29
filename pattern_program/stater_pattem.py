
# rows = int(input("Input a raws :"))
#
# for x in range(rows):
#     for j in range(x+1):
#         print("*",end= " ")
#
#     print("\r")

# r = int(input("Input rows value :"))
#
# for x in range(r):
#     for j in range(x+1):
#         print("*",end="")
#
#     print(" ")

# rows = int(input("Input rows value : "))
# for i in range(rows):
#     for j in range(i+1):
#         print(j+1,end=" ")
#
#     print("  ")

# rows = int(input("Inputs row values :"))
# for x in range(rows):
#     for j in range(x+1):
#         print(j+1,end=" ")
#     print(" ")

# rows = int(input("Enter number of rows: "))
# ascii_value = 65
# for i in range(rows):
#     for j in range(i+1):
#         Aplphabet = chr(ascii_value)
#         print(Aplphabet,end=" ")
#     ascii_value +=1
#     print(" ")


# rows = int(input("Input number of  rows :"))
# asccii_value =  65
# for i in range(rows):
#     for j in range(i+1):
#         Alphabet =chr(asccii_value)
#         print(Alphabet,end="")
#     asccii_value += 1
#     print("  ")

# def printAlphabet(n):
#     ascci_value = 67
#     for i in range(n):
#         for j in range(i+1):
#             Allphabet = chr(ascci_value)
#             print(Allphabet,end=" ")
#         ascci_value +=1
#         print(" ")
#
#
# printAlphabet(8)

# r = int(input("Input row value :"))
#
# for i in range(r,0,-1):
#     for j in range(0,i):
#         print(" * ",end=" ")
#     print(" ")

rows = int(input("Input row value  :"))

for i in range(rows,0,-1):
    for j in range(0, i):
        print("s",end=" ")
    print(" ")