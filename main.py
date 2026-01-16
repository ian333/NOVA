from machine import Pin
import time

# Para LED interno usa 25, para externo usa 15
led = Pin(25, Pin.OUT)  # cambia a Pin(15, Pin.OUT) si usas un LED externo

while True:
	led.value(1)
	time.sleep(0.5)
	led.value(0)
	time.sleep(0.5)