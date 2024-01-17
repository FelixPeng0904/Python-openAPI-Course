<<<<<<< HEAD
import machine
import time
from machine import Pin

led25 = Pin("LED", Pin.OUT) #25是一個引數值
while True:
    led25.value(1) 
    time.sleep(1)
    led25.value(0)
    time.sleep(5)
    
    start = time.ticks()
    delta = time.ticks_diff(time.ticks(),start)
    
    
=======
name = input("please input your name:")
print(name)
>>>>>>> ab32329f91aed19a41dda2ec2076e96ad7dee5d6
