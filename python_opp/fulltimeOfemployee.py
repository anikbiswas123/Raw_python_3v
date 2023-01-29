from abc import  ABC,abstractmethod

class Employee:
    def __init__(self,frist_name,Last_name):
        self.frist_name=frist_name
        self.Last_name=Last_name
    @property
    def full_name(self):
        return  f"{self.frist_name} {self.Last_name}"
    @abstractmethod
    def get_salary(self):
        pass
class fulltimeOfemployee(Employee):
    def __int__(self,frist_name,Last_name,salary):
        super.__init__(frist_name,Last_name)
        self.salary=salary

    def get_salary(self):
        return  self.salary

class HourlyOfemployee(Employee):
    def __init__(self,frist_name,Last_name,working_hour,Rate):
        super().__init__(frist_name,Last_name)
        self.working_hour=working_hour
        self.Rate=Rate
    def get_salary(self):
        return self.working_hour * self.Rate