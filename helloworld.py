import machine
import time

led = machine.Pin(15, machine.Pin.OUT)

while True:
    led.toggle()
    time.sleep(5)
