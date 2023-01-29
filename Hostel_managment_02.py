import random
import datetime

# Global List Declaration

name=[]
phno=[]
add=[]
checkIn=[]
checkout=[]
room=[]
prcice=[]
rc=[]
p=[]
roomno=[]
customer_ID=[]
day=[]

#GLobal variable Declaration

def Home():
    print("\t\t\t\t\t\t\t\t\t\t\t\t  WELCOME TO HOTEL ANCASA\n")
    print("\t\t\t\t\t\t\t\t\t\t\t\t 1 Booking \n")
    print("\t\t\t\t\t\t\t\t\t\t\t\t 2 Room information \n")
    print("\t\t\t\t\t\t\t\t\t\t\t\t 3 Room Service(Menu Card)\n")
    print("\t\t\t\t\t\t\t\t\t\t\t\t 4 payment \n")
    print("\t\t\t\t\t\t\t\t\t\t\t\t 5 Record info \n")
    print("\t\t\t\t\t\t\t\t\t\t\t\t 0 Exit \n")

    ch=int(input(" - > :"))

    if ch == 1:
        print(" ")
        Booking()
    elif ch == 2:
        print(" ")
        Room_info()
    elif ch == 3:
        print(" ")
        restaurant()

    elif ch == 4:
        print(" ")
        Payment()
    elif ch == 5:
        print(" ")
        Record()
    else:
        exit()




