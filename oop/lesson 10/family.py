class Family:
    
    def __init__(self, last_name, home_address ,famous_for,members):
        self.lname=last_name
        self.address=home_address
        self.famous=famous_for
        self.members=members

    def __str__(self):
        s='/n'
        for member in self.members:
            s+= '\n name: '+ member.f_name +'\n age: '+ str(member.age)+ '\n is_parent: '+str(member.is_parent) 
        return s

