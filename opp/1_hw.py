class HomeOrganizer:
    def _init_ (self,amount_of_dishes,amount_of_rooms_to_clean,num_shirts_to_fold,wesh_the_floor):
            self.dishes1=amount_of_dishes
            self.rooms1=amount_of_rooms_to_clean
            self.shirts1=num_shirts_to_fold
            self.floor=wesh_the_floor

    def shirts(self):
        total1=self.shirts1 * 0.5
        print('it will take you around ' ,total1 ,' minutes to fold the shirts')
        return total1

    def dishes(self):
        if self.dishes1=='a little':
            total2=5
            print('It will take you around 5 min. to wash your dishea')
        elif self.dishes1=='a little':
            total2=10
            print('It will take you around 10 min. to wash your dishea')
        elif self.dishes1=='a lot':
            total2=15
            print('It will take you around 15 min. to wash your dishea')
            return total2 
    
    def rooms(self):
        total3=self.rooms1 * 15
        print('it will take you around ' ,total3 ,' minutes to clean the rooms')
        return total3
    
    def washing(self):
        while self==True:
            print('It takes around 20 min. to wash the floor')
            return 20
            break

    def calculate_time(self):
        a=self.shirts()
        b=self.dishes() 
        c=self.rooms()
        d=self.washing()
        total=a+b+c+d
        print('It will take you around ', total ,  ' min. to get the house cleaned' ) 

    def stages(self):     
        self.shirts()
        self.dishes() 
        self.rooms()
        self.washing()
        self.calculate_time()

