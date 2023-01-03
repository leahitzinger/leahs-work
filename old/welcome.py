import sys
import datetime
name1=sys.argv[1]
teacher1=sys.argv[2]
def welcome_to_class(name,teacher):
    print('Welcome ', name ,' to class')
    d=datetime.datetime.now()
    print(d)
    a=d.strftime("%H:%M")
    while True:   
        if a<('09:00'):
            print('before class')
        elif a>('09:00') and a<('10:50') : 
            print('class time')
        elif a>('10:50') and a<('11:10'):
            print('break time')
        if a>('11:10') and a<('13:00'):
            print('class time')
        else:
            print('you finished class for today')
        if teacher=='yocheved':
            print('Yocheved will teach functions') 
        elif teacher=='ellie':
            print('Ellie will teach command line')
        else:
            ('not teaching today')
        break
welcome_to_class(name1,teacher1)
    
