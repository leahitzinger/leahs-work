from employee import Employee
from hourly_employee import HourlyEmployee
from salariedemployee import Salariedemployee
def main():
    employee1=HourlyEmployee('Leah','Itzinger',20,30)
    employee2=HourlyEmployee('Faigy','Winkler',500,20)
    employee3=HourlyEmployee('Ruchami','Bamberger',3000,10)
    employee4=Salariedemployee('malky','Choen',2000)
    employee5=Salariedemployee('Shoshi','Finkel',1000)
    Employees=[employee1,employee2,employee3,employee4,employee5]
    for e in Employees:
        print(e.full_name)
        print(e.get_salary())
main()
