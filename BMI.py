from tkinter import *
from tkinter import ttk

class Gui(Tk):
    def __init__(self):
        #Setting Variables
        Tk.__init__(self)
        self.feet = StringVar()
        self.feet.set("Feet")
        self.inches = StringVar()
        self.inches.set("Inches")
        self.inputs = ttk.Frame()
        self.inputs.grid(column=0)
        self.sep = ttk.Separator(orient=VERTICAL)
        self.sep.grid(column=1, sticky="ewns")
        self.outputs = ttk.Frame()
        self.outputs.grid(column=2)

        #Build GUI Graphics
        Label(self.inputs, text="Height:").pack(side=LEFT)
        self.feetInput = Entry(self.inputs)
        self.feetInput.config(textvariable=self.feet, foreground="#888")
        self.feetInput.pack(side=LEFT)
        self.inchesInput = Entry(self.inputs)
        self.inchesInput.config(textvariable=self.inches, foreground="#888")
        self.inchesInput.pack(side=LEFT)
        Label(self.outputs, text="BMI").pack()

        self.feetInput.bind("<FocusIn>", self.entryModFeet)
        self.feetInput.bind("<FocusOut>", self.entryModFeet)
        self.inchesInput.bind("<FocusIn>", self.entryModInches)
        self.inchesInput.bind("<FocusOut>", self.entryModInches)

    def entryModFeet(self, event):
        current = self.feetInput.get()
        if current == "Feet":
            self.feet.set("")
        elif current == "":
            self.feet.set("Feet")
            
    def entryModInches(self, event):
        current = self.inchesInput.get()
        if current == "Inches":
            self.inches.set("")
        elif current == "":
            self.inches.set("Inches")

def main():
    myGui = Gui()
      
    

if __name__ == "__main__":
    main()
    
