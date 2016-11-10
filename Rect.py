class Shape(object):
    def __init__(self, width=0, height=0):
        object.__init__(self)
        self.__width = width
        self.__height = height

    def setWidth(self, width):
        self.__width = width
        
    def getWidth(self):
        return self.__width

    def setHeight(self, height):
        self.__height = height

    def getHeight(self):
        return self.__height

    width = property(fget = getWidth, fset = setWidth)
    height = property(fget = getHeight, fset = setHeight)

class Rectangle(Shape):
    def __init__(self, width=0, height=0):
        Shape.__init__(self, width, height)

    def getArea(self):
        return self.width * self.height

    def setArea(self, area):
        print("You can't set the Area! It's a derived value!")

    def getPerimeter(self):
        return 2 * (self.width + self.height)

    def setPerimeter(self, area):
        print("You can't set the Perimeter! It's a derived value!")

    area = property(fget = getArea, fset = setArea)
    perimeter = property(fget = getPerimeter, fset = setPerimeter)

    def getStats(self):
        print("width:       %d" % self.width)
        print("height       %d" % self.height)
        print("perimeter:   %d" % self.perimeter)
        print("area:        %d" % self.area)
        
    
def main():
    print("Rectangle a:")
    a = Rectangle(5, 7)
    print("area:        %d" % a.area)
    print("perimeter:   %d" % a.perimeter)
    print("\nRectangle b:")
    b = Rectangle()
    b.width = 10
    b.height = 20
    b.getStats()

if __name__ == "__main__":
    main()
