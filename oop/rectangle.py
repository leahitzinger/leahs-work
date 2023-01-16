class Rectangle:
    def __init__(self,width,length):
        self.__width=width
        self.__length=length

    @property
    def width(self):
        return self.__width

    @property
    def length(self):
        return self.__length

    @width.setter
    def width(self,value):
        self.__width=value

    @length.setter
    def length(self,value):
        self.__length=value

def main():
    my=Rectangle
    my.length=5
    my.width=3
    print(my.length,my.width)

main()