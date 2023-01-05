class ShabbosMaker:
    tools=['mixer','oven','pot']
    storage=['fridge','freezer']
    
    def __init__(self,type_of_kugel,icecream):
        self.timer=timer
        self.type=type_of_kugel
        self.icecream=icecream

    def kugel(self):
        print('The kugel is in the', self.tools[1])
        print('The', self.type, 'kugel is ready, put it in the' , self.storage[0])

    def soup(self,veg):
        for each in veg:
            print('Iam peeling now the',each)
        print('the soup is ready, put the',self.tools[2],'in to the', self.storage[0])

    def dessert(self):
        print('Wipping up the whip in the', self.tools[0])
        print('Prepearing',self.icecream,'icecream')
        print('ready, please put the icecream in the',self.storage[1])
    
    def start_timer(self,veg,timer):
        if  timer=='on':
            print('starting to prepere timer is on')
            self.kugel()
            self.soup(veg)
            self.dessert()

def timer():
    my_shabbos_timer=ShabbosMaker('apple','strawberry')
    my_shabbos_timer.start_timer(['carrot','potato','squash'],'on')

def main():
    my_shabbos=ShabbosMaker('apple','strawberry')
    my_shabbos.kugel()
    my_shabbos.soup(['carrot','potato','squash'])
    my_shabbos.dessert()

# main()
timer()