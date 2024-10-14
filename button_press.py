from machine import Pin
import time

led = Pin(16, Pin.OUT)
button = Pin(15, Pin.IN, PULL_DOWN)

timer = 0

while True:
    time .sleep(1)
    
    if button.value() == 1:
        timer =timer+1
        
    print (timer)
