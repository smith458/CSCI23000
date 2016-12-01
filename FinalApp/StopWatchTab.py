from tkinter import *
from tkinter import ttk
import time

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

def main():
    root = Tk()
    tabs = ttk.Notebook(root)
    stopWatchTab = Stopwatch(tabs)
    tabs.pack()
    root.mainloop()
    

if __name__ == "__main__":
    main()
