import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
pin = 0
nu = 0
GPIO.setup(pin, GPIO.OUT)

p = GPIO.PWM(pin, nu)
p.start(0)
try:
    while(1):
    p.start(int(input()))

finally:
    p.stop()
    GPIO.cleanup()