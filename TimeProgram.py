from gpiozero import Button #reads inputs from gpio; used to read when circuit is closed
from signal import pause
from time import time #gets current Unix time

time_start = time() #defines time_start and time_end as time functions
time_end = time()
button = Button(2) #sets which gpio input is read
def get_time_start(): #variable to print time off 
    global time_start #defined as global so that get_time_start and get_time_end refer to one another rather than above functions
    time_start = time()
    temp = time_start - time_end #allows for easier printing
    print("Time Off" , temp) #tells how long the circuit has been open
def get_time_end(): #variable to print time on
    global time_end #same as above
    time_end = time()
    temp = time_end - time_start #allows for easier printing
    print(" Time On" , temp) #tells how long the circuit has been closed

button.when_pressed = get_time_start #runs get_time_start when circuit is closed
button.when_released = get_time_end #runs get_time_end when circuit is open




