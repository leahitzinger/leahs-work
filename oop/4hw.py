class Monkey:
    species='Gorilla'
    def __init__(self,country,food,how_much_can_eat=25):
        self.country=country
        self.food=food
        self.how_much_ate=0
        self.how_much_can_eat=how_much_can_eat
        

    def show_if_to_feed(self):
        if self.food=='bamboo' or self.food=='fruit' or self.food== 'leafy plants':
            print('Perfect I love that food')
        else:
            print('please give me something else to eat')
    
    
    def feed_me_and_show_message(self,amount):
        if self.how_much_ate+amount <= self.how_much_can_eat:
            self.how_much_ate+=amount
            print( self.how_much_ate)
        else:
            print('I dont want so much food, try less')    
        


    def __str__ (self):
        welcome='This food checkup is for {}  species only'.format(self.species)
        return welcome

def main():
    
    mymonkey = Monkey("Israel",'fruit')
    print(mymonkey)
    mymonkey.show_if_to_feed()
    mymonkey.feed_me_and_show_message(15)
    
    
main()

   