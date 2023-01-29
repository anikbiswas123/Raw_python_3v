
class payroll:
    def __init__(self):
        self.employe_list=[]
    def add(self,employee):
        self.employe_list.append(employee)
    def print(self):
        for x in self.employe_list:
            print("x.full_name} \t ${x.get_salary()" )