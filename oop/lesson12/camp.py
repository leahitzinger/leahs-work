from person import Person
from counselor import Counselor
from camper import Camper
from bunk import Bunk
class Camp:
    def __init__(self,camp_name,max_bunk):
        self.num_bunks=0
        self.camp_name=camp_name
        self.max_bunk=max_bunk
        self.bunks=[]
        self.persons=[]

    def find_counselor(self, fname, lname ):
        for person in self.persons:
            if isinstance(person, Counselor):
                 if person.fname == fname and person.lname == lname:
                    print('Counselor: ' + person)

    def find_camper(self, fname, lname):
        for person in self.persons:
            if isinstance(person, Camper):
                 if person.fname == fname and person.lname == lname:
                    return person
            return None
    
    
    def add_counselor(self, fname, lname ,hire_date,salary):
        new_counselor=Counselor(fname,lname,hire_date,salary)
        self.persons.append(new_counselor)

    def add_camper(self, fname, lname ,dob):
        new_camper=Camper(fname,lname,dob)
        self.persons.append(new_camper)

    def add_bunk(self,bunk_name, counselor_fname,counselor_lname):
        if self.num_bunks< self.max_bunk:
            new_bunk=Bunk(bunk_name, counselor_fname + counselor_lname)
            self.bunks.append(new_bunk)
            self.num_bunks += 1
        else:
            raise Exception ('You have reached the maximum number of bunks.')

    def find_bunk(self,bunk_name):
        for bunk1 in self.bunks:
            if bunk_name  == Bunk.bunk:
                return bunk1

    def place_camper(self,fname,lname,bunk_name):
        Camper_bunk=self.find_bunk(bunk_name) 
        camper=self.find_camper(fname,lname)
        Camper_bunk.add_camper(camper)

    def add_allergy(self,fname,lname, allergy):
        my_camper=self.find_camper(fname,lname)
        my_camper.add_allergy(allergy) 

    def __str__(self):
        welcome='Welcome to {} !\n Bunks:'.format(self.camp_name)
        for bunk in self.bunks:
            welcome+= str(bunk) +' ,'
        return welcome




