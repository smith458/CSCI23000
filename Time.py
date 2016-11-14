from tkinter import *
from tkinter import ttk
import time

class Stopwatch(object):
    def __init__(self, master):
    	tab1 = ttk.Frame(master)
        self.parent = tab1
        master.add(self.parent, text="Stop Watch")
        self.timeRunning = "False"
        self.resetPressed = "False"

    def startStopButton(self):
        #start button pressed

    def resetButton(self):
        #stop button pressed

class Timer(object):
    def __init__(self, parent):
        #init

    def startStopButton(self):
        #start button pressed

    def resetButton(self):
        #stop button pressed

class Alarm(object):
    def __init__(self):
        #init

    def startStopButton(self):
        #start button pressed

def main():
    root = Tk()
    tabs = ttk.Notebook(root)
    stopWatch = Stopwatch(tabs)
    

if __name__ == "__main__":
    main()
