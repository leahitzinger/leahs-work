
from datetime import datetime 
from person import Person
class Counselor(Person):
    def __init__(self, fname, lname, hire_date, salary) -> None:
        super().__init__(fname, lname)
        self.hire_date = datetime.strptime(hire_date, "%d/%m/%Y")
        self.salary = salary
    def __str__(self) -> str:
        return super().__str__() + 'We have been proud of you since {}'.format(self.hire_date)

