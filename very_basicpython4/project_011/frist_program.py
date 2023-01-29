#
# vowals=['a','e','i','o']
# letters=vowals
# letters.append('u')
# print(letters)

# palidrom string

# s=input("input plaidrome input :")
#
# def palidromStrint(string):
#     x=""
#     for i in string:
#         x = i+x
#     return x
#
# ans=palidromStrint(s)
#
# if s == ans:
#     print("yes!")
# else:
#     print("No!")

# def palidromStrigCheck(s):
#     return  s == s[::-1]
#
# s=input("choose you string ")
#
# ans=palidromStrigCheck(s)
#
# if ans:
#    print("yes")
# else:
#     print("No")

# def palidromstringCheck(string):
#     return  string == string[::-1]
# str=input("Input string values :")
#
# ans=palidromstringCheck(str)
#
# if ans:
#     print("yes!")
# else:
#     print("No!")

# def palidromcheck(s):
#
#     rev=''.join(reversed(s))
#
#     if s == rev:
#         return  True
#     return  False
#
#
#
# str=input("Input str values :")
#
# ans=palidromcheck(str)
#
#
#
# if ans:
#     print("Yes!")
# else:
#     print("No!")
#
# num=int(input("Enter you a number :"))
#
# if num < 1 :
#     print(" num not a prime number")
# else:
#     for i in range(2,num):
#         if num % 2 == 0:
#             print(f"{num} not a prime")
#             break
#     else:
#       print(f"{num} it is prime number")

# arr=[7,6,4,4,6,19,45,3,50,89]

# n=len(arr)
#
# for i in range(n-1):
#     for j in range(n-1-i):
#         if arr[j] > arr[j+1]:
#             temp=arr[j]
#             arr[j]=arr[j+1]
#             arr[j+1]=temp
#
# for i in arr:
#     print(arr[i])

# arr=[7,3,9,2 ,0 ,4,8,1,6,5]
#
# def bubblesort(seqlist):
#     n=len(seqlist)
#     for i in range(n-1):
#         for j in range(n-1-i):
#             if seqlist[j] > seqlist[j+1]:
#                 temp=seqlist[j]
#                 seqlist[j]=seqlist[j+1]
#                 seqlist[j+1] = temp
#     return seqlist
#
#
# print(bubblesort(arr)
#
# def search(arr,index):
#     for i in range(len(arr)):
#         if arr[i] == index:
#              return i
#
#     return  -1
#
# search_v=[14,20,24,56,12,56,70,34]
#
# print(search(search_v,12))



# def search(arr,index):
#     for i in range(len(arr)):
#         if arr[i] == index:
#              return i
#
#     return  -1
#
# # search_v=[14,20,24,56,12,56,70,34]
# search_val=["sumilon","anik","Keya","sumiya","nora","Suma"]
# print(search(search_val,"Keya"))

# def  str_search(arr,search):
#     for i in range(len(arr)):
#         if arr[i] == search:
#             return i
#     return  -1
#
#
# name_list=["sumilion","mona","Ripa","Nurpor","sampa","Likhon"]
# match_val='Ripa'
#
# print(str_search(name_list,match_val))

# def str_linear_search(arr_list,index):
#     for i in range(len(arr_list)):
#         if arr_list[i] == index:
#             return  i
#     return 0
#
# std_list=['Rakib',"sumilon","efa","safin","Nupor"]
# match="Nupor"
# print(str_linear_search(std_list,match))

# Linear Search on Lists

# def search(list,n):
#     for i in range(len(List)):
#         if List[i] == n:
#             return True
#     return False
#
# List = [1, 2, 'sachin', 4, 'Geeks', 6]
#
# n="sumilon"
#
# if search(list,n):
#     print("Data found!")
# else:
#     print("data is not found!")

#
# def search(Tuple,search):
#     for i in  range(len(Tuple)):
#         if Tuple[i] == search:
#             return  i
#     return  0
#
# Tuple = (1, 2, 'sachin', 4, 'Geeks', 6)
#
# n='Geeks'
#
# if search(Tuple,n):
#     print("data is found !")
# else:
#     print("Data is not found!")

#Bireary search program with pytho
#
# def Bineary_search(arr,low,heigh,x):
#     if heigh >= low:
#         mid=(heigh+low)//2
#         if arr[mid] == x:
#             return  mid
#         elif arr[mid] > x:
#             print(arr,low,heigh-1,x)
#         else:
#             print(arr,low,heigh+1,x)
#     else:
#         return 0
#
#
# # Test array
# arr = [ 2, 3, 4, 10, 40 ]
# x = 10
#
# result=Bineary_search(arr,0,len(arr)-1,x)
#
# if result !=-1:
#     print("Elments present in index ",)
# else:
#     print("Elments not prestent in index")


# def Bineary_search(arr,low,high,x):
#     if high >= low:
#
#         mid = (high + low) // 2
#
#         # If element is present at the middle itself
#         if arr[mid] == x:
#             return mid
#
#         # If element is smaller than mid, then it can only
#         # be present in left subarray
#         elif arr[mid] > x:
#             return Bineary_search(arr, low, mid - 1, x)
#
#         # Else the element can only be present in right subarray
#         else:
#             return Bineary_search(arr, mid + 1, high, x)
#
#     else:
#         # Element is not present in the array
#         return -1


# arr=[12,34,45,60,60,70]
# n=77
# result=Bineary_search(arr,0,len(arr)-1,n)
# print(" ")
# if result != -1:
#     print("element of index  presents")
# else:
#     print("Element of index not present")



# # Python 3 program for recursive binary search.
# # Modifications needed for the older Python 2 are found in comments.
#
# # Returns index of x in arr if present, else -1
# def binary_search(arr, low, high, x):
#
# 	# Check base case
# 	if high >= low:
#
# 		mid = (high + low) // 2
#
# 		# If element is present at the middle itself
# 		if arr[mid] == x:
# 			return mid
#
# 		# If element is smaller than mid, then it can only
# 		# be present in left subarray
# 		elif arr[mid] > x:
# 			return binary_search(arr, low, mid - 1, x)
#
# 		# Else the element can only be present in right subarray
# 		else:
# 			return binary_search(arr, mid + 1, high, x)
#
# 	else:
# 		# Element is not present in the array
# 		return -1
#
# # Test array
# arr = [ 2, 3, 4, 10, 40 ]
# x = 20
#
# # Function call
# result = binary_search(arr, 0, len(arr)-1, x)
#
# if result != -1:
# 	print("Element is present at index", str(result))
# else:
# 	print("Element is not present in array")


# write a python programing  Bineary search program

#
# def Binear_search(arr,low,high,x):
#     if high >= low:
#         mid = (high + low) // 2
#
#        # If element is present at the middle itself
#         if arr[mid] == x:
#         	 return mid
#
#         # If element is smaller than mid, then it can only
#         # be present in left subarray
#         elif arr[mid] > x:
#         	return Binear_search(arr, low, mid - 1, x)
#
#         # Else the element can only be present in right subarray
#         else:
#            return Binear_search(arr, mid + 1, high, x)
#
#     else:
#      # Element is not present in the array
#        return -1
#
#
# arr=[23,15,30,36,40,45,50]
# n=60
#
# result=Binear_search(arr,0,len(arr),25)
#
# if result !=-1:
#     print("Elemets of array is presented..!")
# else:
#     print("element of array is not presented!")


# def Bineary_search(arr,low,high,x):
#     if high >= low:
#
#         mid=(low+high)//2
#
#         if arr[mid] == x:
#             return  mid
#         elif arr[mid] > x:
#             return  Bineary_search(arr,low,mid-1,x)
#         else:
#             return  Bineary_search(arr,mid+1,high,x)
#     else:
#         return -1
#
# a=[5,7,9,12,25,15,20,24,27,33,40,50,65,72]
# n=10
#
# result=Bineary_search(a,0,len(a),n)
# if result != -1:
#     print("Element preseted the array!")
# else:
#     print("Elemet not presented of array!")


# def linear_search(arr,x):
#     for i in range(len(arr)):
#         if arr[i]== x:
#             return  i
#     return 0
#
# arr=[12,34,67,80,90,67,45]
# x=81
#
# result=linear_search(arr,x)
#
# if result != 0:
#     print("Data is found",result)
# else:
#     print("Data is not found!",x)
#
# def linear_search(list,search):
#     for i in range(len(list)):
#         if list[i] == search:
#             return i
#     return 0
#
# arr=[12,23,21,34,45,67,89,90,10]
# x=10
#
# res=linear_search(arr,x)
#
# if res != 0:
#     print("data is found!",res)
# else:
#     print("Data is not found !",x)

# linear search name array

# def linear_name_name_list(arr,x):
#     for i in range(len(arr)):
#         if arr[i]== x:
#             return i
#     return 0
