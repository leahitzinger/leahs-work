from employee import Employee
class  HourlyEmployee(Employee):
    def __init__(self, first_name, last_name,hourly_rate , hours_worked_this_week):
        super().__init__(first_name, last_name)
        self.rate=hourly_rate
        self.hours=hours_worked_this_week

    def get_salary(self):
        salary=self.rate*self.hours
        return salary 