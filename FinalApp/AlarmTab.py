from tkinter import *
from tkinter import ttk
import time

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

        self.hours = StringVar()
        self.hours.set(self.hoursOpt[0])
        self.mins = StringVar()
        self.mins.set(self.minsOpt[0])
        self.amPm = StringVar()
        self.amPm.set(self.amPmOpt[0])
        self.startStop = StringVar()
        self.startStop.set("Set")
        self.delay = 100
        self.iteration = ""
        self.checkingAlarm = "False"

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

    def startStopButton(self):
        #Start button pressed
        if self.checkingAlarm == "False":
            self.hoursSet = int(self.hours.get())
            self.minsSet = int(self.mins.get())
            self.amPmSet = self.amPm.get()
            if self.amPmSet == "PM":
                self.hoursSet += 12
                if self.hoursSet == 24:
                    self.hoursSet == 0
            self.checkingAlarm = "True"
            self.startStop.set("Cancel")
            self.checkTime()
        else:
            self.parent.after_cancel(self.iteration)
            self.checkingAlarm = "False"
            self.startStop.set("Set")

    def checkTime(self):
        #Checks to see if alarm time has been reached
        now = time.localtime()
        if (self.hoursSet == now[3]) and (self.minsSet == now[4]):
            self.parent.after_cancel(self.iteration)
            self.Alarm("Alarm!")
        else:
            self.iteration = self.parent.after(1000, self.checkTime)

    def Alarm(self, message):
        messagebox.showwarning(message, message)
        self.startStopButton()

def main():
    root = Tk()
    tabs = ttk.Notebook(root)
    alarmTab = Alarm(tabs)
    tabs.pack()
    root.mainloop()
    

if __name__ == "__main__":
    main()
