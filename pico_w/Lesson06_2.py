import machine
import time
from machine import Pin

start_ticks1 = time.ticks_ms()
start_ticks2 = time.ticks_ms()
start_ticks3 = time.ticks_ms()
led25 = Pin("LED",Pin.OUT)
ledStatus = False

while True:
    if time.ticks_diff(time.ticks_ms(),start_ticks1) >= 1000 #var_ticks - start_ticks >= 333:
        start_ticks1 = time.ticks_ms()
        ledStatus = not ledStatus
        led25.value(ledStatus)
    if time.ticks_diff(time.ticks_ms(),start_ticks1) >= 5000 #var_ticks - start_ticks >= 333:
        start_ticks2 = time.ticks_ms()
        ledStatus = not ledStatus
        led25.value(ledStatus)
    if time.ticks_diff(time.ticks_ms(),start_ticks1) >= 10000 #var_ticks - start_ticks >= 333:
        start_ticks3 = time.ticks_ms()
        ledStatus = not ledStatus
        led25.value(ledStatus)
