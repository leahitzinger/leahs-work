class Employee:
    def __init__(self,emp_name,dept):
        self.__name = emp_name
        self.__department = dept
    @property
    def name(self):
        return self.__name.upper()
    @name.setter
    def name(self,value):
        if value.isdigit():
            self.__name = ''
        else:
            self.__name = value
    @property
    def department(self):
        return self.__department.upper()
    @department.setter
    def department(self,value):
        if value.isdigit():
            self.__department = ''
        else:
            self.__department = value