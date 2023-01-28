
from person import Person
from allergy import Allergy
from datetime import datetime
class Camper(Person):
    def __init__(self, fname, lname, dbirth):
        super().__init__(fname, lname)
        self.date_of_birth= datetime.strptime(dbirth,"%d/%m/%Y")
        self.allergies = []
    def add_allergy(self, allergy) -> str:
        allergy_entered = Allergy[allergy.upper()]
        self.allergies.append(allergy_entered)
    def get_age(self):
        camper_age = int(datetime.now().year - self.date_of_birth.year)
        return camper_age
    def __str__(self) -> str:
        return super().__str__()

