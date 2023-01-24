class FamilyMembers:
    def __init__(self, f_name ,age ,is_parent):
        self.f_name=f_name
        self.age=age
        self.is_parent=is_parent

    @property
    def is_parent(self):
        return self._is_parent
    @is_parent.setter
    def is_parent(self,value):
        if self.age>20 and value==True: 
            self._is_parent=True
        else:
            self._is_parent=False