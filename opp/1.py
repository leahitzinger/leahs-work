def set_settings(temp,spinspeed,cycle):
    print('my temperture is' , temp)
    print('my spinspeed is' , spinspeed )
    print('my cycle type is ' + cycle)
def soak(door_is_loocked):
    if door_is_loocked==True:
        print("i'am soaking!" )
    else:
        print('close door')

def agitate(detergent):
    print('scrubbing with' ,detergent)

def rinse():
    print('rinsing')   

def wash_laundry(temp,speed,cycle,door_is_loocked,detergent):
    set_settings(temp,speed,cycle)
    soak(door_is_loocked)
    agitate(detergent)
    rinse()

wash_laundry(30,700,'cottons',True,'persil')


        

