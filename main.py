import RPi.GPIO as GPIO
from time import sleep

RELAY = 9 

GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY, GPIO.OUT, initial=GPIO.LOW)

try:
    while True:
        GPIO.output(RELAY, GPIO.HIGH)
        sleep(0.8)

        GPIO.output(RELAY, GPIO.LOW)
        sleep(3.0) 
finally:
    GPIO.cleanup()