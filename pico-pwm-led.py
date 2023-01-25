from machine import Pin, PWM
from time import sleep

pwm_pin = PWM( Pin(15) )
pwm_pin.freq(1000) # PWM Signal의 주파수는 1kHz, 따라서 주기 T = 1ms

while True:
    for duty in range(65025):       # 2^16 - 1 즉, 65535까지 아닐까?
        pwm_pin.duty_u16(duty)
        sleep(0.0001)
    for duty in range(65025, 0, -1):
        pwm_pin.duty_u16(duty)
        sleep(0.0001)
