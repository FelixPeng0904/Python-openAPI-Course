import machine
import time
from machine import Pin

led25 = Pin("LED", Pin.OUT) #25是一個引數值
while True:
    print(machine.freq())
    led25.value(1) 
    time.sleep(1)
    led25.value(0)
    time.sleep(1)
    
    
    