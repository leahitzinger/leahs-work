from teacher import Teacher
from class_room import ClassRoom
from students import Students

def main():
    my_fave_teacher=Teacher('esti','support')
    student1=Students('elisheva','friedman','a')
    student2=Students('leah','itzinger','b')
    students=[student1,student2]
    my_classroom=ClassRoom(my_fave_teacher,students)
    print(my_classroom)

    teacher_say_hi(my_classroom)

def teacher_say_hi(classroom1):
    print('Hi from ' + classroom1.teacher.name)




main()

