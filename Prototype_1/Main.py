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
# A motor -> Left
dcMotor_A1A = 35
dcMotor_A1B = 37
# B Motor -> Right
dcMotor_B1B = 29
dcMotor_B1A = 31

# Button code variables (switch pro controller)
aBtn = 305
bBtn = 304
yBtn = 306
xBtn = 307

plsBtn = 313        # plus button
mnBtn = 312         # minus button
scnBtn = 317        # screenshot button
hmBtn = 316         # home button

zlBtn = 310
lBtn = 308
zrBtn = 311
rBtn = 309

# motor init
def motorInit():
    gpio.setmode(gpio.BOARD)
    gpio.setup(dcMotor_A1A, gpio.OUT)
    gpio.setup(dcMotor_A1B, gpio.OUT)
    gpio.setup(dcMotor_B1B, gpio.OUT)
    gpio.setup(dcMotor_B1A, gpio.OUT)

# Motor forward
def motorForward(sec):
    motorInit()
    print("forward")
# Motor Right
    gpio.output(dcMotor_A1A, True)
    gpio.output(dcMotor_A1B, False)
# Motor Left
    gpio.output(dcMotor_B1A, True)
    gpio.output(dcMotor_B1B, False)
    time.sleep(sec)
    gpio.cleanup()

# Motor reverse
def MotorReverse(sec):
    motorInit()
    print("reverse")
# Motor Right
    gpio.output(dcMotor_A1A, False)
    gpio.output(dcMotor_A1B, True)
# Motor Left
    gpio.output(dcMotor_B1A, False)
    gpio.output(dcMotor_B1B, True)
    time.sleep(sec)
    gpio.cleanup()

# Motor right
def motorRight(sec):
    motorInit()
    print("right")
# Motor Right
    gpio.output(dcMotor_A1A, True)
    gpio.output(dcMotor_A1B, False)
# Motor Left
    gpio.output(dcMotor_B1A, False)
    gpio.output(dcMotor_B1B, True)
    time.sleep(sec)
    gpio.cleanup()

# Motor left
def motorLeft(sec):
    motorInit()
    print("left")
# Motor Right
    gpio.output(dcMotor_A1A, False)
    gpio.output(dcMotor_A1B, True)
# Motor Left
    gpio.output(dcMotor_B1A, True)
    gpio.output(dcMotor_B1B, False)
    time.sleep(sec)
    gpio.cleanup()

if __name__ == '__main__':
    try:
        while True:
            print("try a control button")
            for event in gamepad.read_loop():
                if event.type == ecodes.EV_KEY:
                    if event.value == 1:
                        print("button pressed")
                        if event.code == aBtn:
                            print("A")
                            motorRight(1)
                        elif event.code == bBtn:
                            print("B")
                            MotorReverse(1)
                        elif event.code == yBtn:
                            print("Y")
                            motorLeft(1)
                        elif event.code == xBtn:
                            print("X")
                            motorForward(1)
                        elif event.code == hmBtn:
                            # Stop motors
                            print("home")
                            gpio.cleanup()
                            
    except KeyboardInterrupt:
        print("Keyboard interrupt")
        gpio.cleanup()
    except:
        print("Other error or exception occured!")
        gpio.cleanup()