# Imorts
    # GPIO for pi pins control
import RPi.GPIO as gpio
    # Time for delays
import time
    # Controller readings
from evdev import InputDevice, categorize, ecodes
    # Translator
from python_translator import Translator
    # Language detector
from langdetect import detect
    # Speech recognition
import speech_recognition as sr


# Declerations
    #set board mode to GPIO.BOARD
gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
    #creates object 'gamepad' to store the data
gamepad = InputDevice('/dev/input/event1')
    # Button 
BUTTON1 = 7
    # LED
LED = 11

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
def gpioInnit():
    # Set board
    gpio.setmode(gpio.BOARD)
    # Set led
    gpio.setup(LED, gpio.OUT)
    gpio.output(LED, gpio.LOW)
    # Set button
    gpio.setup(BUTTON1, gpio.IN, pull_up_down=gpio.PUD_UP)
    # Set motor pins
    gpio.setup(dcMotor_A1A, gpio.OUT)
    gpio.setup(dcMotor_A1B, gpio.OUT)
    gpio.setup(dcMotor_B1B, gpio.OUT)
    gpio.setup(dcMotor_B1A, gpio.OUT)

# Motor Left
def motorLeft(sec):
    # motorInit()
    print("Left")
# Motor Right
    gpio.output(dcMotor_A1A, True)
    gpio.output(dcMotor_A1B, False)
# Motor Left
    gpio.output(dcMotor_B1A, True)
    gpio.output(dcMotor_B1B, False)
    time.sleep(sec)
    # gpio.cleanup()

# Motor Right
def motorRight(sec):
    # motorInit()
    print("Right")
# Motor Right
    gpio.output(dcMotor_A1A, False)
    gpio.output(dcMotor_A1B, True)
# Motor Left
    gpio.output(dcMotor_B1A, False)
    gpio.output(dcMotor_B1B, True)
    time.sleep(sec)
    # gpio.cleanup()

# Motor Reverse
def motorReverse(sec):
    # motorInit()
    print("Reverse")
# Motor Right
    gpio.output(dcMotor_A1A, True)
    gpio.output(dcMotor_A1B, False)
# Motor Left
    gpio.output(dcMotor_B1A, False)
    gpio.output(dcMotor_B1B, True)
    time.sleep(sec)
    # gpio.cleanup()

# Motor Forward
def motorForward(sec):
    # motorInit()
    print("Forward")
# Motor Right
    gpio.output(dcMotor_A1A, False)
    gpio.output(dcMotor_A1B, True)
# Motor Left
    gpio.output(dcMotor_B1A, True)
    gpio.output(dcMotor_B1B, False)
    time.sleep(sec)
    # gpio.cleanup()

#INPUT SPEECH VIA WEBCAM MIC 
def speechToText():
    print("speechToText")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something when the light is on")
        gpio.output(LED, gpio.HIGH)
        # audio = r.listen(source)
        audio = r.listen(source, timeout=5, phrase_time_limit=20)
    gpio.output(LED, gpio.LOW)
    return audio

#RECOGNIZE SPEECH CONVERT TO TEXT
def recognizeSpeech(audio):
    r = sr.Recognizer()
    speech = r.recognize_google(audio)
    print(speech)
    return speech

#TRANSLATE TEXT TO DUTCH
def translateText(speech):    
    translator = Translator()
    translationText = translator.translate(speech, "dutch")
    print(translationText) # -> to display for dutch
    detectedLang = detect(speech)
    print(detectedLang)
    return detectedLang

#TRANSLATE DUTCH BACK TO ORIGINAL LANGUAGE
def translateOriginLang(detectedLang):
    print("translateOriginLang")
    print(detectedLang)
    audio = speechToText()

    r = sr.Recognizer()
    speech = r.recognize_google(audio, language="nl")
    print(speech)

    translator = Translator()
    originLangText = translator.translate(speech, detectedLang)
    print(originLangText) #-> to display for foreign language

def listenToButtonInput(listening):
    while listening:
        if gpio.input(BUTTON1) == True:
            print("button1 pressed")        
            audio = speechToText()
            speech = recognizeSpeech(audio)
            detectedLang = translateText(speech)
            translateOriginLang(detectedLang)
            time.sleep(0.3)
            listening = False   

def main():
    try:
        while True:  
            gpioInnit() 
            print("try a control button")
            for event in gamepad.read_loop():
                if event.type == ecodes.EV_KEY:
                    if event.value == 1:
                        print("button pressed")
                        if event.code == plsBtn:
                            print("Plus")
                            listenToButtonInput(True)
                        if event.code == aBtn:
                            print("A")
                            motorRight(1)
                        elif event.code == bBtn:
                            print("B")
                            motorReverse(1)
                        elif event.code == yBtn:
                            print("Y")
                            motorLeft(1)
                        elif event.code == xBtn:
                            print("X")
                            motorForward(1)
                        elif event.code == hmBtn:
                            # Stop motors
                            print("Stop")
                            gpio.cleanup()
            gpio.cleanup()
    except KeyboardInterrupt:
        gpio.cleanup()
        print("KeyboardInterrupt")
    except Exception as e:
        gpio.cleanup()
        print(e)
    
                        
                        

if __name__ == '__main__':
    main()