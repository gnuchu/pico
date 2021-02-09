import tm1637
from machine import Pin
import time

timedisplay = tm1637.TM1637(clk=Pin(16), dio=Pin(17))
datedisplay = tm1637.TM1637(clk=Pin(15), dio=Pin(14))

timedisplay.numbers(21, 39, True)
datedisplay.numbers(8,2, False)
 

