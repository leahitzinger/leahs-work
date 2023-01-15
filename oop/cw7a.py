class Store:
    def __init__(self):
        self.__address=None
        self.__name=None
        self.__well_stocked=None
    
    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name = name
    
    def get_address(self):
        return self.__address

    def set_address(self,address):
        self.__address = address 

    def get_well_stocked(self):
        return self.__well_stocked

    def set_well_stocked(self,well_stocked):
        self.__well_stocked= well_stocked   