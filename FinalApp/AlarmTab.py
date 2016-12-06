from tkinter import *
from tkinter import ttk
import time

class entryVar(StringVar):
    def __init__(self, default="", name="", limit="60"):
        StringVar.__init__(self)
        self.default = default
        self.set(self.default)
        self.name = name
        self.limit = limit

class Alarm(object):
    def __init__(self, master):
        #Tab Construction
        tab3 = ttk.Frame(master)
        self.parent = tab3
        master.add(self.parent, text="Alarm")

        #Control Variables
        self.hoursOpt = ["01", "02", "03", "04", "05", "06",
                         "07", "08", "09", "10", "11", "12"]
        
        self.minsOpt = ["00", "05", "10", "15", "20", "25",
                        "30", "35", "40", "45", "50", "55"]
        
        self.amPmOpt = ["AM", "PM"]

        self.hours = entryVar(default=self.hoursOpt[0])
        self.mins = entryVar(default=self.minsOpt[0])
        self.amPm = entryVar(default=self.amPmOpt[0])
        self.startStop = StringVar()
        self.startStop.set("Start")
        self.delay = 100
        self.iteration = ""
        self.timeSet = 0

        #Interface Construction
        self.hoursEntry = OptionMenu(tab3, self.hours, *self.hoursOpt)
        self.hoursEntry.grid(row=0, column=0)
        Label(tab3, text=":").grid(row=0, column=1)
        self.minsEntry = OptionMenu(tab3, self.mins, *self.minsOpt)
        self.minsEntry.grid(row=0, column=2)
        Label(tab3, text=":").grid(row=0, column=3)
        self.secsEntry = OptionMenu(tab3, self.amPm, *self.amPmOpt)
        self.secsEntry.grid(row=0, column=4)
        Button(tab3, textvariable=self.startStop, command=self.startStopButton).grid()
        Button(tab3, text="Reset", command=self.resetButton).grid()

    def startStopButton(self):
        #start button pressed
        print("A")

    def resetButton(self):
        #start button pressed
        print("A")

def main():
    root = Tk()
    tabs = ttk.Notebook(root)
    alarmTab = Alarm(tabs)
    tabs.pack()
    root.mainloop()
    

if __name__ == "__main__":
    main()
