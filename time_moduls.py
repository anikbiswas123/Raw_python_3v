
# import time
# second=time.time()
# print(second)
#
# print("This is printed immediately.")
# time.sleep(6)
# print("This is printed after 2.4 seconds.")

#Python create a digital clock
# while True :
#     localtime=time.localtime()
#     result=time.strftime("%I:%M:%S %p",localtime)
#     print(result)
#     time.sleep(3)

# while True:
#      localTime=time.localtime()
#      result=time.strftime("%I:%M:%S %p",localTime)
#      print(result)
#      time.sleep(1)

# while True:
#     localtime=time.localtime()
#     result=time.strftime("%I:%M:%S %p",localtime)
#     print(result)
#     time.sleep(3)


# import time
#
# while True:
#   localtime = time.localtime()
#   result = time.strftime("%I:%M:%S %p", localtime)
#   print(result)
#   time.sleep(2)

# import datetime
#
# datatime_object=datetime.datetime.now()
# print(datatime_object)

#get current date

# data_today=datetime.date.today()
# print(data_today)
# import datetime
# d=datetime.date(2020,8,20)
# print(d)

# from  datetime import  date
# d=date(2018,9,23)
# print(d)

# today display show
# from  datetime import date
# d=date.today()
# print("current date :",d)
#
# datatimestramp=date.fromtimestamp(1745646433)
# print("get data and time :",datatimestramp)


from datetime import  date
#
# date=date.today()
# # print(date)
# print("current year :",date.year)
# print("current moth :",date.month)
# print("current days :",date.day)

from  datetime import time

# #time(Hours=0,minites=0 and second=0)
# a=time()
# print(a)

# set time (hours,mintues and second)

# time=time(11,47,50)
# print("time show",time)
# #get time
# print("current hours :",time.hour)
# print("current mintues :",time.minute)
# print("current second :",time.second)
#
# a=time(12,37,48)
# print("get hours =",a.hour)
# print("get mintues =",a.minute)
# print("get second =",a.second)

from  datetime import datetime

#include date time modules datatime(year,month,day)
# datetime=datetime(2021,8,25)
# # print("date show :",datetime)
#
# # get datetime
# print("current year =",datetime.year)
# print("current month =",datetime.month)
# print("current day =",datetime.day)

#datetime(year,month,day,hours,mintues,second,microsecond)
# datetime=datetime(2021,8,23,19,56,48,76455)
# # print("total =",datetime)
# #get all about attributes
# print("get year =",datetime.year)
# print("get month =",datetime.month)
# print("get day =",datetime.day)
# print("get hours =",datetime.hour)
# print("get mintues =",datetime.minute)
# print("get second =",datetime.second)
# print("microsecond =",datetime.microsecond)

# a = datetime(2017, 11, 28, 23, 55, 59, 342380)
#
# print(a)
# print("get year :",a.year)
# print("get month :",a.month)
# print("get day :",a.day)
# print("get hour :",a.hour)
# print("get mintue :",a.minute)
# print("get second :",a.second)
# print("get microsecond :",a.microsecond)

# from datetime import  date
#
# d=date(year=2020,month=9,day=27)
# print("date show",d)
# print("gett date")
# print("get year =",d.year)
# print("get month =",d.month)
# print("get days =",d.day)
#
# print("\n")
# from  datetime import  time
#
# time=time(hour=20,minute=43,second=55,microsecond=746643)
# print("show time =",time)
# print("get time show ")
# print("get hours =",time.hour)
# print("get mintues =",time.minute)
# print("get second =",time.second)
# print("get microsecond =",time.microsecond)
#
# print("\n")
# from  datetime import datetime
#
# datetime=datetime(year=2021,month=11,day=24,hour=20,minute=40,second=45,microsecond=4365)
# print("data time show :",datetime)
# print("get all attributes ")
#
# print("get year =",datetime.year)
# print("get month =",datetime.month)
# print("get days=",datetime.day)
# # print("get hours =",datetime.hour)
# # print("get mintues =",datetime.minute)
# # print("get second =",datetime.second)
# # print("get microscound =",datetime.microsecond)
#
# from datetime import  datetime,date
# t1=date(year=2018,month=9,day=12)
# t2=date(year=2017,month=11,day=27)
# t3=t1-t2
# print("get year month day")
# print("get year :",t1.year)
# print("get month t1",t1.month)
# print("get day t1",t1.day)
# print("t3 =",t3)
# # from  datetime import  datetime
# dat1=datetime(year=2021,month=10,day=24,hour=18,minute=45,second=56)
# dat2=datetime(year=2019,month=9,day=27,hour=20,minute=50,second=59)
#
# result=dat1-dat2
# print("total differences =",result)
#
# from  datetime import  datetime

# datetime=datetime(year=2021,month=9,day=23,hour=20,minute=40,second=44,microsecond=676766)
# print(datetime)
# print("get datatime propertices ...")
# print("get year=",datetime.year)
# print('get month=',datetime.month)
# print("get day=",datetime.day)
# print("get second =",datetime.second)
# print("get hours=",datetime.hour)
# print("get month=",datetime.minute)
# print("get second =",datetime.second)

#Difference between two timedelta objects

from  datetime import  timedelta

# # date_1=timedelta(days=10,hours=10,minutes=55,seconds=34)
# # date_2=timedelta(days=7,hours=16,minutes=56,seconds=44)
# # differences=date_1 - date_2
# # print("differences =",differences)
#
# datetime_1=timedelta()

# timedelta_1=timedelta(weeks=4,days=5,hours=20,minutes=43,seconds=55)
# timedelta_2=timedelta(weeks=2,days=3,hours=20,minutes=43,seconds=45)
# differences=timedelta_1-timedelta_2
# print(differences)

# from  datetime import timedelta
#
# t2=timedelta(weeks=3,days=3,hours=20,minutes=25,seconds=55)
# print("total second =",t2.total_seconds())


# date time formating

# from datetime import  datetime
# datetime=datetime.now()
# t1=datetime.strftime("%m:%d:%y ,%H:%M:%S")
# print(t1)

# import time
# print("prnted before on datatime")
# time.sleep(2)
# print("printed after 2 second ")

from  datetime import  time,datetime


