import _thread
import time


myName = "John"


def printThread():
    global myName
    time.sleep(10)
    print(myName)


_thread.start_new_thread(printThread(), ())


myName = "gnuchu"
print(myName)