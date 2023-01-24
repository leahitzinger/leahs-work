class ClassRoom:
    def __init__(self,teacher,students):
        self.teacher=teacher
        self.students=students

    def __str__(self):
        s='Welcome to our classroom.'
        s+='\nTeacher' +str(self.teacher)+'\n'
        for student in self.students:
            s+= ' ' + student.first_name+' ' + student.last_name+'\n'


        return s


