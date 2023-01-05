class Seamstress:
    #class atributes:
    hand = 'hand'
    sewing_machine = 'singer' #every seamstress in Israel has a singer sewing machine
    
    def __init__(self, experience, talent, specialty):
        self.experience = experience
        self.talent = talent
        self.specialty = specialty
    def cut_material(self, cutting_tool, fabric):
        print("I'm cutting the fabric called", fabric, 'with my', cutting_tool, 'in my', self.hand)
    
    def take_measurements(self, measuring_tool):
        print("Now I'm taking measurements with a", measuring_tool)
    
    def sew_garment(self, garment_type):
        print("I'm sewing a", garment_type, "with my", self.sewing_machine)

def main():
    rivky_berlin = Seamstress('6 years', True, 'Gowns')
    rivky_berlin.take_measurements('measuring_stick')
    rivky_berlin.cut_material('scissors', 'crushed_velvet')
    rivky_berlin.sew_garment('Gown')
    print("This is my experience", rivky_berlin.experience)
    chava_kurman = Seamstress('10 years', True, 'Baby things - From the Eibishter')
#if __name__ == "__main__":
main()