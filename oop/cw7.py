class Shopper:
    def __init__(self):
        self.__address=None
        self.__lastname=None
        self.__pref_transport_method=None
    
    def get_name(self):
        return self.__lastname

    def set_name(self,last_name):
        self.__lastname = last_name
    
    def get_address(self):
        return self.__address

    def set_address(self,address):
        self.__address = address 

    def get_transport_method(self):
        return self.__pref_transport_method

    def set_transport_method(self,pref_transport_method):
        self.__pref_transport_method= pref_transport_method


          
        





