import machine
import time
from machine import Pin

start_ticks = time.ticks_ms()
led25 = Pin("LED",Pin.OUT)
ledStatus = False

while True:
    var_ticks = time.ticks_ms()
    if var_ticks - start_ticks >= 333:
        start_ticks = time.ticks_ms()
        ledStatus = not ledStatus
        led25.value(ledStatus)
