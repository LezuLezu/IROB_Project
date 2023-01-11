# Imorts
    # GPIO for pi pins control
import RPi.GPIO as gpio
    # Time for delays
import time
    # Controller readings
from evdev import InputDevice, categorize, ecodes

#creates object 'gamepad' to store the data
gamepad = InputDevice('/dev/input/event0')

# Motor vars
dcMotorA1 = 35
dcMotorB1 = 37
dcMotorA2 = 29
dcMotorB2 = 31

# Button code variables (switch pro controller)
aBtn = 305
bBtn = 304
yBtn = 306
xBtn = 307

plsBtn = 313       # plus button
mnBtn = 312         # minus button
scnBtn = 317        # screenshot button
hmBtn = 316        # home button

zlBtn = 310
lBtn = 308
zrBtn = 311
rBtn = 309

# motor init
def motorInit():
    gpio.setmode(gpio.BOARD)
    gpio.setup(dcMotorA1, gpio.OUT)
    gpio.setup(dcMotorB1, gpio.OUT)
    gpio.setup(dcMotorA2, gpio.OUT)
    gpio.setup(dcMotorB2, gpio.OUT)

# Motor forward
def motorForward(sec):
    motorInit()
    print("forward")
    gpio.output(dcMotorA1, False)
    gpio.output(dcMotorB1, True)
    gpio.output(dcMotorA2, False)
    gpio.output(dcMotorB2, True)
    time.sleep(sec)
    gpio.cleanup()
# Motor reverse
def MotorReverse(sec):
    motorInit()
    print("reverse")
    gpio.output(dcMotorA1, True)
    gpio.output(dcMotorB1, False)
    gpio.output(dcMotorA2, True)
    gpio.output(dcMotorB2, False)
    time.sleep(sec)
    gpio.cleanup()
# Motor right
def motorRight(sec):
    motorInit()
    print("right")
    gpio.output(dcMotorA1, False)
    gpio.output(dcMotorB1, True)
    gpio.output(dcMotorA2, True)
    gpio.output(dcMotorB2, False)
    time.sleep(sec)
    gpio.cleanup()
# Motor left
def motorLeft(sec):
    motorInit()
    print("left")
    gpio.output(dcMotorA1, True)
    gpio.output(dcMotorB1, False)
    gpio.output(dcMotorA2, False)
    gpio.output(dcMotorB2, True)
    time.sleep(sec)
    gpio.cleanup()

if __name__ == '__main__':
    try:
        while True:
            for event in gamepad.read_loop():
                if event.type == ecodes.EV_KEY:
                    if event.value == 1:
                        if event.code == aBtn:
                            print("A")
                            motorForward(1)
                        elif event.code == bBtn:
                            print("B")
                            MotorReverse(1)
                        elif event.code == yBtn:
                            print("Y")
                            motorRight(1)
                        elif event.code == xBtn:
                            print("X")
                            motorLeft(1)
                        elif event.code == hmBtn:
                            # Stop motors
                            print("home")
                            raise KeyboardInterrupt            
                            
    except KeyboardInterrupt:
        print("Keyboard interrupt")
        gpio.cleanup()
    except:
        print("Other error or exception occured!")
        gpio.cleanup()