from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self,first_name,last_name):
        self.l_name=last_name
        self.f_name=first_name


    @property
    def full_name(self):
        return self.f_name +' '+ self.l_name
    
    @abstractmethod
    def get_salary(self):
        pass















