import tm1637
from machine import Pin
import utime

four  = tm1637.TM1637(clk=Pin(15), dio=Pin(14))
three = tm1637.TM1637(clk=Pin(16), dio=Pin(17))
two   = tm1637.TM1637(clk=Pin(13), dio=Pin(12))
one   = tm1637.TM1637(clk=Pin(11), dio=Pin(10))

def clear(screen):
    screen.show('    ')

def test_device(device):
    print("Testing device", device)
    device.show("JOHN")
    utime.sleep(1)

clear(four)
clear(three)
clear(two)

one.numbers(21, 45, True)
two.show("8")
three.show("FEB")
four.number(2020)

