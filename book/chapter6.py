import machine
import utime
import urandom

led = machine.Pin(15, machine.Pin.OUT)
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

def button_handler(pin):
    button.irq(handler=None)
    print(pin)

button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler)

while True:
    led.value(1)
    utime.sleep(urandom.uniform(5,10))
    led.value(0)
