from tools import connect, reconnect
from machine import ADC,Pin,Timer
import time
#https://hook.us1.make.com/1khpve1tymy2jk7aw47o7a1v14beob99?data=2024-01-15-14:25:00&temperature=25.456&from=學院養雞場

adc = ADC(4)     # create ADC object on ADC pin,最後一個,溫度
conversion_factor = 3.3/65535

start_time = time.ticks_ms() # get millisecond counter 用來抓到開始時間點
duration = 10 #用來設定多久發送一次訊息

def alert():
    global start_time # 每一次循環需要建立全新變數，需要 global 進行定義>> 需要進一步查詢用途及功能
    if time.ticks_diff(time.ticks_ms(),start_time) >= duration * 1000: # 1000ms = 1s
        print("要爆炸了")
        print("將傳送信息") # 預計每個60秒進行傳送
        start_time = time.ticks_ms()

def second1(t):
    reading_v = adc.read_u16() * conversion_factor
    # The temperature sensor measures the Vbe voltage of a biased bipolar diode, connected to the fifth ADC channel
    # Typically, Vbe = 0.706V at 27 degrees C, with a slope of -1.721mV (0.001721) per degree. 
    celsius = 27 - (reading_v-0.706) / 0.001721
    print(round(celsius,3))
    if celsius >= 25:
        alert()
        
    
tim1 = Timer()
tim1.init(period=1000, callback=second1)
