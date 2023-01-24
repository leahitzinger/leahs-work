class Teacher:
    def __init__(self, name,subject):
        self.name=name
        self.subject=subject

    def __str__(self):
        return 'Name: '+ self.name + '\n Subject: '+self.subject