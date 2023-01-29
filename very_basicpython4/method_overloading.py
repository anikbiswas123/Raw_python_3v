
# method overlodaing

# class parents:
#     def __init__(self,name):
#         self.name=name
#         self.value="parent  value"
#     def show(self):
#         print(self.value)
#         print("person name ",self.name)
#
# class child(parents):
#     def __init__(self, name):
#          self.name = name
#          self.value="inside clas"
#
#
#
#     def show(self):
#         print(self.value)
#         print("child name ".format(self.name))
#
# obj1=parents("Md shajhan mia")
# obj2=child("Rakib hossain")
#
# obj1.show()
# print("\n\n")
# obj2.show()


class person:
    def __init__(self,p_name,p_address,p_phone):
        self.p_name=p_name
        self.p_address=p_address
        self.p_phone=p_phone
        self.value= 'parent class'

    def display(self):
        print(self.value)
        print("person name {}".format(self.p_name))
        print("person address {}".format(self.p_address))
        print("person phone number {}".format(self.p_phone))

class employee(person):
    def __init__(self,p_name,p_address,p_phone,post_title,worker_time):
        self.p_name=p_name
        self.p_address=p_address
        self.p_phone=p_phone
        self.post_title=post_title
        self.worker_time=worker_time
    def display(self):
        print(self.value)
        print("employee name {}".format(self.p_name))
        print("Employee address {}".format(self.p_address))
        print("Employee phone {}".format(self.p_phone))
        print("emloyee post_title ".format(self.post_title))
        print("working time ".format(self.worker_time))

pb=person("sumilon biswas","patukhali","47873")
print("person name :",pb.p_name)
print("person address :",pb.p_address)
print("person phone :",pb.p_phone)
print("===================")
pb.display()




