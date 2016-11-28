from tkinter import *
from tkinter import ttk
import time

class TimeApp(object):
    def __init__(self, master):
        #Tab Construction
        self.master = master
        
class Stopwatch(object):
    def __init__(self, master):
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
        Label(tab1, textvariable=self.count).pack()
        Button(tab1, textvariable=self.startStop, command=self.startStopButton).pack(side=LEFT)
        Button(tab1, text="Reset", command=self.resetButton).pack(side=LEFT)

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

class Timer(object):
    def __init__(self, master):
        #Tab Construction
        tab2 = ttk.Frame(master)
        self.parent = tab2
        master.add(self.parent, text="Timer")

        #Control Variables
        hours = StringVar()
        hours.set("00")
        mins = StringVar()
        mins.set("00")
        secs = StringVar()
        secs.set("00.0")
        startStop = StringVar()
        startStop.set("Start")
        self.timeRunning = "False"
        self.resetPressed = "False"

        #Interface Construction
        hoursEntry = Entry(tab2, textvariable=hours, width=3)
        hoursEntry.grid(row=0, column=0)
        Label(tab2, text=":").grid(row=0, column=1)
        minsEntry = Entry(tab2, textvariable=mins, width=3)
        minsEntry.grid(row=0, column=2)
        Label(tab2, text=":").grid(row=0, column=3)
        secsEntry = Entry(tab2, textvariable=secs, width=4)
        secsEntry.grid(row=0, column=4)
        Button(tab2, textvariable=startStop, command=self.startStopButton).grid()
        Button(tab2, text="Reset", command=self.resetButton).grid()

    def startStopButton(self):
        if self.timeRunning=="False":
            self.countTime()
            self.startStop.set("Stop")
        else:
            self.parent.after_cancel(self.iteration)
            self.timeRunning = "False"
            self.startStop.set("Start")

    def countTime(self):
        #start button pressed
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

    def resetButton(self):
        #stop button pressed
        self.parent.after_cancel(self.iteration)
        self.startTime = 0
        self.count.set("00:00:00.0")
        self.timeRunning = "False"
        self.startStop.set("Start")

class Alarm(object):
    def __init__(self, master):
        tab3 = ttk.Frame(master)
        self.parent = tab3
        master.add(self.parent, text="Alarm Clock")
        count = StringVar()
        count.set(0)
        startStop = StringVar()
        startStop.set("Start")
        Label(tab3, textvariable=count).pack()
        Button(tab3, textvariable=startStop, command=self.startStopButton).pack(side=LEFT)
        self.timeRunning = "False"
        self.resetPressed = "False"

    def startStopButton(self):
        #start button pressed
        print("A")

def main():
    root = Tk()
    tabs = ttk.Notebook(root)
    stopWatchTab = Stopwatch(tabs)
    timerTab = Timer(tabs)
    alarmTab = Alarm(tabs)
    tabs.pack()
    root.mainloop()
    

if __name__ == "__main__":
    main()
