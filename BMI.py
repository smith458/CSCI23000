from tkinter import *
from tkinter import ttk

class entryVar(object):
    def __init__(self, default="", entryName="none", limit="1000"):
        self.entryName = entryName
        self.default = default
        self.value = StringVar()
        self.value.set(default)
        self.limit = limit

class Gui(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.mainframe = Frame(self, padx=10, pady=10)
        self.mainframe.pack()

        #Setting Variables
        self.feet = entryVar("ft")
        self.inches = entryVar("in", limit=11)
        self.weight = entryVar("pounds")
        self.BMI = entryVar()
        self.status = entryVar()
        
        self.inputs = Frame(self.mainframe, padx=10, pady=10)
        self.inputs.grid(column=0, row=0)
        
        self.sep = ttk.Separator(self.mainframe, orient=VERTICAL)
        self.sep.grid(column=1, row=0, sticky="ewns")
        
        self.outputs = Frame(self.mainframe, padx=10, pady=10)
        self.outputs.grid(column=2, row=0)
        
        #Input GUI Construction
        Label(self.inputs, text="Height:").grid(row=0, column=0)
        
        self.feet.entryName = Entry(self.inputs, width=5)
        self.feet.entryName.config(textvariable=self.feet.value, foreground="#888")
        self.feet.entryName.grid(row=0, column=1)
        
        self.inches.entryName = Entry(self.inputs, width=5)
        self.inches.entryName.config(textvariable=self.inches.value, foreground="#888")
        self.inches.entryName.grid(row=0, column=2)

        Label(self.inputs, text="Weight:").grid(row=1, column=0)

        self.weight.entryName = Entry(self.inputs, width=11)
        self.weight.entryName.configure(textvariable=self.weight.value, foreground="#888")
        self.weight.entryName.grid(row=1, column=1, columnspan=2)
        
        #Output GUI Construction
        Label(self.outputs, text="BMI:").grid(column=0, row=0)
        Label(self.outputs, textvariable=self.BMI.value).grid(column=1, row=0)
        Label(self.outputs, text="Status:").grid(column=0, row=1)
        Label(self.outputs, textvariable=self.status.value).grid(column=1, row=1)

        #Calculate
        calcButton = Button(self.mainframe, text="Calculate", command=self.calculate)
        calcButton.grid(row=1, column=0, columnspan=3, sticky="enws")

        #Events
        self.bind_class("Entry", sequence="<FocusIn>", func=self.entryMod)
        self.bind_class("Entry", sequence="<FocusOut>", func=self.entryMod)
        self.bind_class("Entry", sequence="<Key>", func=self.entryEval)
        self.bind("<Return>", self.calculate)
        self.outputs.columnconfigure(1, minsize=60)
        
        self.mainloop()

    def calculate(self, event="None"):
        weight = int(self.weight.value.get())
        feet = int(self.feet.value.get())
        inches = int(self.inches.value.get())          

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
        
        self.BMI.value.set(str(BMI))
        self.status.value.set(status)

    def entryMod(self, event):
        widgetName = {self.feet.entryName: self.feet,
                      self.inches.entryName: self.inches,
                      self.weight.entryName: self.weight}
        widget = widgetName[event.widget]
        current = widget.value.get()
        if current == widget.default:
            widget.value.set("")
            widget.entryName.config(foreground="#000")
        elif current == "":
            widget.value.set(widget.default)
            widget.entryName.config(foreground="#888")
        else:
            widget.entryName.select_range(0, END)

    def entryEval(self, event):
        widgetName = {self.feet.entryName: self.feet,
                      self.inches.entryName: self.inches,
                      self.weight.entryName: self.weight}
        widget = widgetName[event.widget]
        current = widget.value.get()
        if (event.char.isdigit()):
            current += event.char
            if(int(current) <= int(widget.limit)):
                widget.value.set(current)
                widget.entryName.icursor(END)

def main():
    myGui = Gui()

if __name__ == "__main__":
    main()
