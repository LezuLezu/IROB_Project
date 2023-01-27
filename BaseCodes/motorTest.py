import RPi.GPIO as gpio
import time

dcMotorA1 = 35
dcMotorB1 = 37
dcMotorA2 = 29
dcMotorB2 = 31

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(dcMotorA1, gpio.OUT)
    gpio.setup(dcMotorB1, gpio.OUT)
    gpio.setup(dcMotorA2, gpio.OUT)
    gpio.setup(dcMotorB2, gpio.OUT)

def forward(sec):
    init()
    print("forward")
    gpio.output(dcMotorA1, False)
    gpio.output(dcMotorB1, True)
    gpio.output(dcMotorA2, False)
    gpio.output(dcMotorB2, True)
    time.sleep(sec)
    gpio.cleanup()

def reverse(sec):
    init()
    print("reverse")
    gpio.output(dcMotorA1, True)
    gpio.output(dcMotorB1, False)
    gpio.output(dcMotorA2, True)
    gpio.output(dcMotorB2, False)
    time.sleep(sec)
    gpio.cleanup()

def right(sec):
    init()
    print("right")
    gpio.output(dcMotorA1, False)
    gpio.output(dcMotorB1, True)
    gpio.output(dcMotorA2, True)
    gpio.output(dcMotorB2, False)
    time.sleep(sec)
    gpio.cleanup()

def left(sec):
    init()
    print("left")
    gpio.output(dcMotorA1, True)
    gpio.output(dcMotorB1, False)
    gpio.output(dcMotorA2, False)
    gpio.output(dcMotorB2, True)
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