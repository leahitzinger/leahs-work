class Person:
    def __init__(self, fname, lname) -> None:
        self.fname = fname
        self.lname = lname

    def get_full_name(self):
        full_name=self.fname+ ' '+ self.lname
        return full_name
    def __str__(self) -> str:
        return 'Hi {}'.format(self.get_full_name())