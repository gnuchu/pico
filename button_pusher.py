import machine
import time

button = machine.Pin(14, machine.Pin.IN)

while True:
    print(time.localtime(), button.value())
    time.sleep(1)
    
    
    
    
    