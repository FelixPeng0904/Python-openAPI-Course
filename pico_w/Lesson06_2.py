import machine
import time
from machine import Pin

start_ticks1 = time.ticks_ms()
start_ticks2 = time.ticks_ms()
start_ticks3 = time.ticks_ms()
led25 = Pin("LED",Pin.OUT)
ledStatus = False

while True:
    if time.ticks_diff(time.ticks_ms(),start_ticks1) >= 1000:
        print("pass 1 second")
        start_ticks1 = time.ticks_ms()
        ledStatus = not ledStatus
        led25.value(ledStatus)
    if time.ticks_diff(time.ticks_ms(),start_ticks2) >= 5000:
        print("pass 5 second")
        start_ticks2 = time.ticks_ms()
        ledStatus = not ledStatus
        led25.value(ledStatus)
    if time.ticks_diff(time.ticks_ms(),start_ticks3) >= 10000:
        print("pass 10 second")
        start_ticks3 = time.ticks_ms()
        ledStatus = not ledStatus
        led25.value(ledStatus)
