class Rectangle:
    def __init__(self,width,length):
        self.width=width
        self.length=length

    @property
    def width(self):
        return self._width

    @property
    def length(self):
        return self._length

    @width.setter
    def width(self,value):
        self._width=value

    @length.setter
    def length(self,value):
        self._length=value

def main():
    my=Rectangle(5,10)
    my.length=5
    my.width=3
    print(my.length,my.width)

main()