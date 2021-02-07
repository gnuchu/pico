import tm1637
from machine import Pin
from utime import sleep
mydisplay = tm1637.TM1637(clk=Pin(16), dio=Pin(17))
 
#show a time with colon
x = -999
while True:
    mydisplay.number(x)
    x += 1
    if x == 9999:
        x = -999
    sleep(0.01)
