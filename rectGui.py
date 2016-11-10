from tkinter import *

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

class guiClass(object):
    def __init__(self, parent, shape):
        self.parent = parent
        self.shape = shape
        self.varArea = StringVar()
        self.varPerimeter = StringVar()

        inputs = Frame(parent)
        inputs.pack(side=LEFT, padx=5, pady=5)
        Label(inputs, text="Width:").grid(column=0, row=0)
        Label(inputs, text="Height:").grid(column=0, row=1)
        self.widthEntry = Entry(inputs)
        self.widthEntry.grid(column=1, row=0)
        self.heightEntry = Entry(inputs)
        self.heightEntry.grid(column=1, row=1)
        calc = Button(inputs, text="Calculate", command=self.submit)
        calc.grid(column=0, row=2, columnspan=2, sticky="W N E S")

        outputs = Frame(parent)
        outputs.pack(side=LEFT, padx=5, pady=5)
        Label(outputs, text="Area:").grid(column=0, row=0)
        Label(outputs, text="Perimeter:").grid(column=0, row=1)
        Label(outputs, textvariable=self.varArea).grid(column=1, row=0)
        Label(outputs, textvariable=self.varPerimeter).grid(column=1, row=1)

        for child in inputs.winfo_children(): child.grid_configure(padx=1, pady=1)
        for child in outputs.winfo_children(): child.grid_configure(padx=1, pady=1)
      
    def submit(self, *args):
        self.shape.width = int(self.widthEntry.get())
        self.shape.height = int(self.heightEntry.get())
        self.varArea.set(self.shape.area)
        self.varPerimeter.set(self.shape.perimeter)
    
def main():
    root = Tk()
    a = Rectangle()
    rectGui = guiClass(root, a)
    rectGui.widthEntry.focus()
    root.bind('<Return>', rectGui.submit)
    

if __name__ == "__main__":
    main()
