from tkinter import *
from tkinter import ttk

class entryVar(object):
    def __init__(self, name):
        self.name = name
    
    

class Gui(Tk):
    def __init__(self):
        #Setting Variables
        Tk.__init__(self)
        self.mainframe = Frame(self, padx=10, pady=10)
        self.mainframe.pack()
        self.feet = StringVar()
        self.feet.set("Feet")
        self.inches = StringVar()
        self.inches.set("Inches")
        self.weight = StringVar()
        self.weight.set("Weight")
        self.BMI = StringVar()
        self.BMI.set("")
        self.status = StringVar()
        self.status.set("")
        self.inputs = Frame(self.mainframe, padx=10, pady=10)
        self.inputs.grid(column=0, row=0)
        self.sep = ttk.Separator(self.mainframe, orient=VERTICAL)
        self.sep.grid(column=1, row=0, sticky="ewns")
        self.outputs = Frame(self.mainframe, padx=10, pady=10, width=100000)
        self.outputs.grid(column=2, row=0)
        
        #Input GUI Construction
        Label(self.inputs, text="Height:").grid(row=0, column=0)
        
        self.feetInput = Entry(self.inputs, width=5)
        self.feetInput.config(textvariable=self.feet, foreground="#888")
        self.feetInput.grid(row=0, column=1)
        
        self.inchesInput = Entry(self.inputs, width=5)
        self.inchesInput.config(textvariable=self.inches, foreground="#888")
        self.inchesInput.grid(row=0, column=2)

        Label(self.inputs, text="Weight:").grid(row=1, column=0)

        self.weightInput = Entry(self.inputs, width=11)
        self.weightInput.configure(textvariable=self.weight, foreground="#888")
        self.weightInput.grid(row=1, column=1, columnspan=2)
        
        #Output GUI Construction
        Label(self.outputs, text="BMI:").grid(column=0, row=0)
        Label(self.outputs, textvariable=self.BMI).grid(column=1, row=0)
        Label(self.outputs, text="Status:").grid(column=0, row=1)
        Label(self.outputs, textvariable=self.status).grid(column=1, row=1)

        #Calculate
        calcButton = Button(self.mainframe, text="Calculate", command=self.calculate)
        calcButton.grid(row=1, column=0, columnspan=3, sticky="enws")

        #Events        
        self.feetInput.bind("<FocusIn>", self.entryModFeet)
        self.feetInput.bind("<FocusOut>", self.entryModFeet)
        self.inchesInput.bind("<FocusIn>", self.entryModInches)
        self.inchesInput.bind("<FocusOut>", self.entryModInches)
        self.weightInput.bind("<FocusIn>", self.entryModWeight)
        self.weightInput.bind("<FocusOut>", self.entryModWeight)
        self.bind("<Return>", self.calculate)
        self.outputs.columnconfigure(1, minsize=60)
        
        self.mainloop()

    def calculate(self, event="None"):
        weight = int(self.weight.get())
        feet = int(self.feet.get())
        inches = int(self.inches.get())
        
        height = feet * 12 + inches
        BMI = round(weight * 703 / height**2, 1)

        if BMI <= 18.5:
            status = "Underweight"
        elif BMI < 25:
            status = "Normal"
        elif BMI < 30:
            status = "Overweight"
        else:
            status = "Obese"
        
        self.BMI.set(BMI)
        self.status.set(status)

    def entryModFeet(self, event):
        current = self.feetInput.get()
        if current == "Feet":
            self.feet.set("")
            self.feetInput.config(foreground="#000")
        elif current == "":
            self.feet.set("Feet")
            self.feetInput.config(foreground="#888")
            
    def entryModInches(self, event):
        current = self.inchesInput.get()
        if current == "Inches":
            self.inches.set("")
            self.inchesInput.config(foreground="#000")
        elif current == "":
            self.inches.set("Inches")
            self.inchesInput.config(foreground="#888")

    def entryModWeight(self, event):
        current = self.weightInput.get()
        if current == "Weight":
            self.weight.set("")
            self.weightInput.config(foreground="#000")
        elif current == "":
            self.weight.set("Weight")
            self.weightInput.config(foreground="#888")

def main():
    myGui = Gui()

if __name__ == "__main__":
    main()
