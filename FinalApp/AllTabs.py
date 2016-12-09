from tkinter import *
from tkinter import ttk
import time

class TimeTab(object):
    def __init__(self):
        self.master = ""

    def pad(self):
        for child in self.parent.winfo_children(): child.grid_configure(padx=5, pady=5)

    def disableFields(self, onOff):
        for child in self.mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

    def toggleEntry(self, onOff):
        for id in self.entries:
            id.config(state=onOff)

class entryVar(StringVar):
    def __init__(self, default="", entry="", limit="60"):
        StringVar.__init__(self)
        self.default = default
        self.set(self.default)
        self.entry = entry
        self.limit = limit

class Stopwatch(TimeTab):
    def __init__(self, master):
        TimeTab.__init__(self)
        #Tab Construction
        tab1 = ttk.Frame(master)
        self.parent = tab1
        master.add(self.parent, text="Stop Watch")

        #Control Variables
        self.count = StringVar()
        self.count.set("00:00:00.0")
        self.startStop = StringVar()
        self.startStop.set("Start")
        self.delay = 100
        self.timeRunning = "False"
        self.startTime = 0
        self.iteration = ""

        #Interface Construction
        Label(tab1, textvariable=self.count).grid(row=0, column=0)
        Button(tab1, textvariable=self.startStop, command=self.startStopButton).grid(row=1, column=0)
        Button(tab1, text="Reset", command=self.resetButton).grid(row=1, column=1)

    #Method that runs when the Start/Stop Button is pressed
    def startStopButton(self):
        if self.timeRunning=="False":
            self.countTime()
            self.startStop.set("Stop")
        else:
            self.parent.after_cancel(self.iteration)
            self.timeRunning = "False"
            self.startStop.set("Start")
            
    #Recursive method that updates the Stopwatch values 
    def countTime(self):
        if self.startTime == 0:
            self.startTime = time.time()
        elif self.timeRunning == "False":
            self.startTime += time.time() - self.currentTime
        self.timeRunning = "True"
        self.currentTime = time.time()
        self.timeElapsed = self.currentTime - self.startTime
        self.hoursElapsed = str(int(self.timeElapsed / 3600)).zfill(2)
        self.minutesElapsed = str(int(self.timeElapsed % 3600 / 60)).zfill(2)
        self.secondsElapsed = str(round(self.timeElapsed % 60, 1)).zfill(4)
        self.concatElapsed = self.hoursElapsed+":"+self.minutesElapsed+":"+self.secondsElapsed
        self.count.set(self.concatElapsed)
        self.iteration = self.parent.after(self.delay, self.countTime)

    #Method that runs when the Reset Button is pressed
    def resetButton(self):
        self.parent.after_cancel(self.iteration)
        self.startTime = 0
        self.count.set("00:00:00.0")
        self.timeRunning = "False"
        self.startStop.set("Start")

class Timer(TimeTab):
    def __init__(self, master):
        #Tab Construction
        tab2 = ttk.Frame(master)
        self.parent = tab2
        master.add(self.parent, text="Timer")

        #Control Variables
        self.hours = entryVar(default="00")
        self.mins = entryVar(default="05")
        self.secs = entryVar(default="00.0")
        self.startStop = StringVar()
        self.startStop.set("Start")
        self.delay = 100
        self.startTime = 0
        self.iteration = ""
        self.timeSet = 0
        self.timeRunning = "False"

        #Interface Construction
        self.hours.entry = Entry(tab2, textvariable=self.hours, width=3)
        self.hours.entry.grid(row=0, column=0)
        Label(tab2, text=":").grid(row=0, column=1)
        self.mins.entry = Entry(tab2, textvariable=self.mins, width=3)
        self.mins.entry.grid(row=0, column=2)
        Label(tab2, text=":").grid(row=0, column=3)
        self.secs.entry = Entry(tab2, textvariable=self.secs, width=4)
        self.secs.entry.grid(row=0, column=4)
        Button(tab2, textvariable=self.startStop, command=self.startStopButton).grid()
        Button(tab2, text="Reset", command=self.resetButton).grid()

        self.entries = [self.hours.entry, self.mins.entry, self.secs.entry]
        for id in self.entries:
            id.config(disabledforeground="#444444")
            id.config(disabledbackground="#CCCCCC")

    def startStopButton(self):
        #start button pressed
        if self.timeRunning=="False":
            if self.timeSet == 0:
                self.hoursSet = int(self.hours.get())
                self.minsSet = int(self.mins.get())
                self.secsSet = float(self.secs.get())
                self.timeSet = self.hoursSet * 3600 + self.minsSet * 60 + self.secsSet
            self.toggleEntry("disabled")
            self.countTime()
            self.startStop.set("Stop")
        else:
            self.parent.after_cancel(self.iteration)
            self.timeRunning = "False"
            self.toggleEntry("normal")
            self.startStop.set("Start")

    def countTime(self):
        #Counts down the timer
        if self.startTime == 0:
            self.startTime = time.time()
        elif self.timeRunning == "False":
            self.startTime = time.time() - self.elapsedTime
        self.timeRunning = "True"
        self.currentTime = time.time()
        self.elapsedTime = self.currentTime - self.startTime
        self.timeLeft = self.timeSet - self.elapsedTime
        self.hoursLeft = str(int(self.timeLeft / 3600)).zfill(2)
        self.minsLeft = str(int(self.timeLeft % 3600 / 60)).zfill(2)
        self.secsLeft = str(round(self.timeLeft % 60, 1)).zfill(4)
        self.hours.set(self.hoursLeft)
        self.mins.set(self.minsLeft)
        self.secs.set(self.secsLeft)
        if self.timeLeft > 0:
            self.iteration = self.parent.after(self.delay, self.countTime)
        else:
            self.alert("Time is up!")

    def alert(self, message):
        messagebox.showwarning(message, message)
        self.resetButton()

    def resetButton(self):
        #stop button pressed
        self.parent.after_cancel(self.iteration)
        self.startTime = 0
        self.hours.set(str(self.hoursSet).zfill(2))
        self.mins.set(str(self.minsSet).zfill(2))
        self.secs.set(str(self.secsSet).zfill(4))
        self.timeSet = 0
        self.timeRunning = "False"
        self.startStop.set("Start")
        self.toggleEntry("normal")

class Alarm(TimeTab):
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
        self.hours.entry = OptionMenu(tab3, self.hours, *self.hoursOpt)
        self.hours.entry.grid(row=0, column=0)
        Label(tab3, text=":").grid(row=0, column=1)
        
        self.mins.entry = OptionMenu(tab3, self.mins, *self.minsOpt)
        self.mins.entry.grid(row=0, column=2)
        Label(tab3, text=":").grid(row=0, column=3)
        
        self.amPm.entry = OptionMenu(tab3, self.amPm, *self.amPmOpt)
        self.amPm.entry.grid(row=0, column=4)
        
        Button(tab3, textvariable=self.startStop, command=self.startStopButton).grid()

        self.entries = [self.hours.entry, self.mins.entry, self.amPm.entry]
        
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
            self.toggleEntry("disabled")
            self.checkTime()
        else:
            self.parent.after_cancel(self.iteration)
            self.toggleEntry("normal")
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
    stopwatchTab = Stopwatch(tabs)
    timerTab = Timer(tabs)
    alarmTab = Alarm(tabs)
    tabs.pack()
    root.resizable(width=False, height=False)
    root.minsize(width=200, height=200)
    root.mainloop()
    

if __name__ == "__main__":
    main()
