import machine
import utime
import _thread

green = machine.Pin(13, machine.Pin.OUT)
yellow = machine.Pin(14, machine.Pin.OUT)
red = machine.Pin(15, machine.Pin.OUT)

buzzer = machine.Pin(12, machine.Pin.OUT)
button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)

global button_pressed
button_pressed = False

def button_reader_thread():
    global button_pressed
    while True:
        if button.value() == 1:
            button_pressed = True

sequence = [
    (1,0,0),
    (1,1,0),
    (0,0,1),
    (0,1,0)
]

def setState(state):
    red.value(state[0])
    yellow.value(state[1])
    green.value(state[2])
    
utime.sleep(1)
_thread.start_new_thread(button_reader_thread, ())

delay = 0.5

while True:
    if button_pressed == True:
        buzzer.value(1)
        utime.sleep(2)
        buzzer.value(0)
        button_pressed = False
        
    for state in sequence:
        setState(state)
        utime.sleep(delay)