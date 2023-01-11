import RPi.GPIO as gpio
import time

# Motor vars
# A motor
dcMotor_A1A = 35
dcMotor_A1B = 37
# B Motor
dcMotor_B1B = 29
dcMotor_B1A = 31


def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(dcMotor_A1A, gpio.OUT)
    gpio.setup(dcMotor_A1B, gpio.OUT)
    gpio.setup(dcMotor_B1B, gpio.OUT)
    gpio.setup(dcMotor_B1A, gpio.OUT)

def forward(sec):
    init()
    print("forward")
    gpio.output(dcMotor_A1A, False)
    gpio.output(dcMotor_A1B, True)
    gpio.output(dcMotor_B1B, False)
    gpio.output(dcMotor_B1A, True)
    time.sleep(sec)
    gpio.cleanup()

def reverse(sec):
    init()
    print("reverse")
    gpio.output(dcMotor_A1A, True)
    gpio.output(dcMotor_A1B, False)
    gpio.output(dcMotor_B1B, True)
    gpio.output(dcMotor_B1A, False)
    time.sleep(sec)
    gpio.cleanup()

def right(sec):
    init()
    print("right")
    gpio.output(dcMotor_A1A, False)
    gpio.output(dcMotor_A1B, True)
    gpio.output(dcMotor_B1B, True)
    gpio.output(dcMotor_B1A, False)
    time.sleep(sec)
    gpio.cleanup()

def left(sec):
    init()
    print("left")
    gpio.output(dcMotor_A1A, True)
    gpio.output(dcMotor_A1B, False)
    gpio.output(dcMotor_B1B, False)
    gpio.output(dcMotor_B1A, True)
    time.sleep(sec)
    gpio.cleanup()

seconds = 3
forward(seconds)
time.sleep(seconds)
reverse(seconds)
time.sleep(seconds)
left(seconds)
time.sleep(seconds)
right(seconds)


