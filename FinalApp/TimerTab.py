from tkinter import *
from tkinter import ttk
import time

class Timer(object):
    def __init__(self, master):
        #Tab Construction
        tab2 = ttk.Frame(master)
        self.parent = tab2
        master.add(self.parent, text="Timer")

        #Control Variables
        self.hours = StringVar()
        self.hours.set("00")
        self.mins = StringVar()
        self.mins.set("00")
        self.secs = StringVar()
        self.secs.set("00.0")
        self.startStop = StringVar()
        self.startStop.set("Start")
        self.delay = 100
        self.startTime = 0
        self.iteration = ""
        self.timeRunning = "False"

        #Interface Construction
        self.hoursEntry = Entry(tab2, textvariable=self.hours, width=3)
        self.hoursEntry.grid(row=0, column=0)
        Label(tab2, text=":").grid(row=0, column=1)
        self.minsEntry = Entry(tab2, textvariable=self.mins, width=3)
        self.minsEntry.grid(row=0, column=2)
        Label(tab2, text=":").grid(row=0, column=3)
        self.secsEntry = Entry(tab2, textvariable=self.secs, width=4)
        self.secsEntry.grid(row=0, column=4)
        Button(tab2, textvariable=self.startStop, command=self.startStopButton).grid()
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

    def resetButton(self):
        #stop button pressed
        self.parent.after_cancel(self.iteration)
        self.startTime = 0
        self.count.set("00:00:00.0")
        self.timeRunning = "False"
        self.startStop.set("Start")

    def toggleEntry(self):
        self.secsEntry = 0
        self.secsEntry = 0
        self.secsEntry = 0

    def getTimes(self):
        self.seconds = self.secsEntry.get()
        self.minutes = self.minsEntry.get()
        self.hours = self.hoursEntry.get()

def main():
    root = Tk()
    tabs = ttk.Notebook(root)
    timerTab = Timer(tabs)
    tabs.pack()
    root.mainloop()
    

if __name__ == "__main__":
    main()
