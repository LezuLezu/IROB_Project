import RPi.GPIO as gpio
import time

#   LED
LED = 11
#   Button
BUTTON = 7

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)

gpio.setup(BUTTON, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(LED, gpio.OUT)
gpio.output(LED, gpio.LOW)



while True:
    if gpio.input(BUTTON) == False:
        print("Pressed")
        gpio.output(LED, gpio.HIGH)
        time.sleep(2)
        gpio.output(LED, gpio.LOW)