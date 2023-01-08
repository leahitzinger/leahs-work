class WashingMachine:
    def __init__ (self,temp,speed,cycle,door_is_loocked,detergent):
            self.temp=temp
            self.speed=speed
            self.cycle=cycle
            self.loocked=door_is_loocked
            self.detergent=detergent

    def set_settings(self):
        print('my temperture is' , self.temp)
        print('my spinspeed is' , self.speed )
        print('my cycle type is ' + self.cycle)

    def soak(self):
        if self.loocked==True:
            print("i'am soaking!")
        else:
            print('close door')

    def agitate(self):
        print('scrubbing with' ,self.detergent)

    def rinse(self):
        print('rinsing')   

    def wash_laundry(self):
        self.set_settings()
        self.soak()
        self.agitate()
        self.rinse()
my_washing_machine=WashingMachine(30,1200,'cottons',True,'ariel')
my_washing_machine.wash_laundry()
