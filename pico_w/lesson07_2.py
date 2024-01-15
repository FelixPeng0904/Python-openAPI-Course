from machine import ADC, Pin, Timer
adc = ADC(4)     # create ADC object on ADC pin,最後一個,溫度
print(adc.read_u16())         # read value, 0-65535 across voltage range 0.0v - 3.3v

def second1(t):
    print(adc.read_u16())

    
tim1 = Timer()
tim1.init(period=1000, callback=second1)

