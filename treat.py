import RPi.GPIO as GPIO
import time

# GPIO parameters for stepper motor
GPIO.setmode(GPIO.BOARD)
#ControlPin = [7, 11, 13, 15]
ControlPin = [31, 33, 35, 37]
for pin in ControlPin:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

seq = [ [1,0,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,1,1,0],
        [0,0,1,0],
        [0,0,1,1],
        [0,0,0,1],
        [1,0,0,1] ]

# Rotate stepper motro 360 degrees
for i in range(512):
    for halfstep in range(8):
        for pin in range(4):
            GPIO.output(ControlPin[pin], seq[halfstep][pin])
        time.sleep(0.001)

# Clear GPIO memory
GPIO.cleanup()


