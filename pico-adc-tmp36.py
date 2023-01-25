from machine import ADC, Pin
import time

adc = ADC( Pin(26) )
while True:
    adcValue = adc.read_u16() 		# 0~ 65025? 65535(2^16-1)?
    V = adcValue * 3.3/65536.0
    t = 100 * V - 50
    print(V, end='\t')
    print(t)
    time.sleep(1)
