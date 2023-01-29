from fulltimeemployee import FulltimeEmployee
from hourlyemployee import HourlyEmployee
from payroll import Payroll

payroll=Payroll()
payroll.add(FulltimeEmployee("john","Doe",6000))
payroll.add(FulltimeEmployee("jane","Doe",7000))
payroll.add(HourlyEmployee("janifer","smith",200,50))
payroll.add(HourlyEmployee("Devied","wilson",150,100))
payroll.add(HourlyEmployee("Kevin","miller",100,150))

payroll.print()
