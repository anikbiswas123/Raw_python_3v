
#create outer class

class merchant:
    def __init__(self,today_Status):
        self.today_status=today_Status

    def status(self):
        print("today our office statices ",self.today_status)

    class order:
        def __init__(self,item1,item2,item3,item4,price):
            self.item1=item1
            self.item2=item2
            self.item3=item3
            self.item4=item4
            self.price=price
        def products(self):
            print("{} ".format(self.item1))
            print("{}".format(self.item2))
            print("{}".format(self.item3))
            print("{}".format(self.item4))

        def case(self):
            print("Our case officer is ",self.price)
    class owner:
        def __init__(self,ownerName,owner_age):
            self.ownerName=ownerName
            self.owner_age=owner_age

        def owner_info(self):
            print("{} ".format(self.ownerName))
            print("{} ".format(self.owner_age))

class customer(merchant):
    def __init__(self,c_name,c_address,c_phone,item1,item2,item3,item4,today_Status):
        super().__init__(today_Status)
        self.c_name=c_name
        self.c_address=c_address
        self.c_phone=c_phone
        self.item1=item1
        self.item2=item2
        self.item3=item3
        self.item4=item4
    def customer_info(self):
        print("customer Name {}\n customer address {} customer phone number {}".format(self.c_name,self.c_address,self.c_phone))
    def place_order(self):
        print("place order :{}{}{}".format(self.item1,self.item2,self.item3))

class Delivery_boy(merchant):
    def __init__(self,today_statuse,delivery_statause):
        super().__init__(today_statuse)
        self.dlivery_status=delivery_statause

    def delivery_status(self):
          if self.dlivery_status =="Dlivered":
              print("All product have been delivered")
          else:
              print("products delivery soon...")

# merchant=merchant("open")
# print(merchant.today_status)
# merchant.status()
#
# merchant=merchant.order("apple","Banana","orange","lemon",450)
# merchant.products()
# merchant.case()
#
# merchant1=merchant.owner("Dulal chandra biswas",45)
# merchant1.owner_info()
# print("\n \n")
customer=customer("Rakib","Dhanmondie","9485753","apple","Banana","orange","lemon","open")
customer.customer_info()
customer.place_order()
customer.status()
print("\n \n")