import RPi.GPIO as GPIO


def on(pin):
    GPIO.setwarnings(False)
    # Set the GPIO mode to BCM
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin,GPIO.LOW)


def off(pin):
    GPIO.setwarnings(False)
    # Set the GPIO mode to BCM
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin,GPIO.HIGH)
