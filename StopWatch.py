from tkinter import *
from tkinter import ttk
import time

#Container class for the object that is passed through the program
class container(object):
    def __init__(self):
        self.start_time = 0
        self.task = ""
        self.current_time = ""
        self.second_count = ""
        #These are the states of the program.
        self.clockRunning = False
        self.clockStopped = False

#Function that runs when start button is pressed.
#Checks if clock is already running.
def start_pressed(var):
    if var.clockRunning == False:
        start_count(var)

#Function that is called by Start Pressed.
#This is a recursive function that actually
#increments and updates the time.
def start_count(var):
    
    #Checks to see if a start time has been created
    if var.start_time == 0:
        var.start_time = time.time()

    #Checks to see if the stop button has been hit.
    #If it has, it refreshes stop time to continue count.
    elif var.clockStopped == True:
        var.start_time = time.time() - var.second_count
        var.clockStopped = False
    var.current_time = time.time()
    var.second_count = var.current_time - var.start_time
    var.second_count = round(var.second_count, 1)
    seconds.set(var.second_count)
    var.task = root.after(100, lambda: start_count(var))
    var.clockRunning = True

#Function that runs when the stop button is pressed.
#Stops the recursive function and sets the states of the program.
def stop_count(var):
    root.after_cancel(var.task)
    var.clockRunning = False
    var.clockStopped = True

#Resets the count of the timer and clears the states of the program.
def reset_count(var):
    root.after_cancel(var.task)
    var.clockRunning = False
    var.clockStopped = False
    var.start_time = 0
    seconds.set(0)

#Initializes the variable object.
var = container()
root = Tk()
seconds = StringVar()
seconds.set(0)

start = ttk.Button(text="Start", command=lambda: start_pressed(var))
start.grid(column=0, row=1)
start = ttk.Button(text="Stop", command=lambda: stop_count(var))
start.grid(column=1, row=1)
start = ttk.Button(text="Reset", command=lambda: reset_count(var))
start.grid(column=2, row=1)

count = ttk.Label(textvariable = seconds)
count.grid(column=1, row=0, columnspan=3)

#root.configure(bg="white")
#root.minsize(300, 300)
root.mainloop()

