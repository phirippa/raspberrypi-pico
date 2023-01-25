from machine import Pin
import time

# GPIO 25번 핀에 BUILTIN LED가 연결되어 있음.
led = Pin(25, Pin.OUT)

# GPIO 14번 핀에 버튼(스위치)를 pull down 형태로 연결.
button = Pin(14, Pin.IN)

while True:
    if button.value():
        led.value(1)
    else:
        led.value(0)
    
    #time.sleep(0.1)
    
    
# 스위치를 누르면 LED On, 스위치를 누르지 않으면 LED Off
