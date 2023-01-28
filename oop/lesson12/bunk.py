class Bunk():
    
    def __init__(self ,bunk_name, counselor):
        self.bunk=bunk_name
        self.counselor=counselor
        self.campers=[]
    def add_camper(self,camper):
        for campe in self.campers:
            self.campers.append(camper)
                    for person in self.persons:
            if isinstance(person, Counselor):
                 if person.fname == fname and person.lname == lname:
                    print('Counselor: ' + person)

    def __str__(self)-> str:
       return str(self.counselor) +'bunk : {},\n counselor : {} \n campers: {}'.format(self.bunk,self.counselor,self.campers) 