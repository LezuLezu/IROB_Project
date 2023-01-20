# ------ IMPORTS ------ #
    #   GPIO for pi pin controls for hardware
import RPi.GPIO as gpio
    #   Serial
import serial
    #   time for delays
import time
    #   controller event readings
from evdev import InputDevice, categorize, ecodes
    #   python translation
from python_translator import Translator
    #   Language detetcion
from langdetect import detect
    #   Speech recognitions
import speech_recognition as sr

# ------ OBJECT DECLERATIONS ------ #
    # Ignore GPIO warnings (board set in innit)
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)

#   Gamepad object
gamepad = InputDevice('/dev/input/event0')
#   Recongizer object
r = sr.Recognizer()
#   translator object
translator = Translator()


# ------ VARIABLE DECLERATIONS ------ #
# Language Target 
targetLanguage = "dutch"
#   LED
LED = 11
#   Button
BUTTON = 7

# Motors
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

# ------ GPIO INNIT ------ #
def gpioInnit():
    # Set board
    gpio.setmode(gpio.BOARD)
    # Set led
    gpio.setup(LED, gpio.OUT)
    gpio.output(LED, gpio.LOW)
    # Set button
    gpio.setup(BUTTON, gpio.IN, pull_up_down=gpio.PUD_UP)
    # Set motor pins
    gpio.setup(dcMotor_A1A, gpio.OUT)
    gpio.setup(dcMotor_A1B, gpio.OUT)
    gpio.setup(dcMotor_B1B, gpio.OUT)
    gpio.setup(dcMotor_B1A, gpio.OUT)
    
    gpio.setup(dcMotor_A1A, gpio.LOW)
    gpio.setup(dcMotor_A1B, gpio.LOW)
    gpio.setup(dcMotor_B1B, gpio.LOW)
    gpio.setup(dcMotor_B1A, gpio.LOW)

# ------ MOTOR DIRECTIONS ------ #
# Motor Left
def motorLeft(sec):
    print("Left")
# Motor Right
    gpio.output(dcMotor_A1A, True)
    gpio.output(dcMotor_A1B, False)
# Motor Left
    gpio.output(dcMotor_B1A, True)
    gpio.output(dcMotor_B1B, False)
    time.sleep(sec)
    
# Motor Right
def motorRight(sec):
    print("Right")
# Motor Right
    gpio.output(dcMotor_A1A, False)
    gpio.output(dcMotor_A1B, True)
# Motor Left
    gpio.output(dcMotor_B1A, False)
    gpio.output(dcMotor_B1B, True)
    time.sleep(sec)

# Motor Reverse
def motorReverse(sec):
    print("Reverse")
# Motor Right
    gpio.output(dcMotor_A1A, True)
    gpio.output(dcMotor_A1B, False)
# Motor Left
    gpio.output(dcMotor_B1A, False)
    gpio.output(dcMotor_B1B, True)
    time.sleep(sec)

# Motor Forward
def motorForward(sec):
    print("Forward")
# Motor Right
    gpio.output(dcMotor_A1A, False)
    gpio.output(dcMotor_A1B, True)
# Motor Left
    gpio.output(dcMotor_B1A, True)
    gpio.output(dcMotor_B1B, False)
    time.sleep(sec)


# ------ Translation ------ #
#   TRANSLATE TEXT TO Target Language
def translateText(speech):    
    #   Translate the text to target language 
    translatedText = translator.translate(speech, targetLanguage)
    #   Fetch string from translated text
    translatedText_String = translatedText.new_text
    print(translatedText_String)
    #   Detect origin langauge
    originLanguage = detect(speech)
    print("Detected language: " + originLanguage)
    #   Return string from text and origin language
    return translatedText_String, originLanguage

def translateOrigin(speech, originLanguage):
    #   Translate the text to origin language
    translatedText = translator.translate(speech, originLanguage)
    #   Fetch string from translated text
    translatedText_String = translatedText.new_text
    #   Return translated string
    return translatedText_String

# Listen for hardware button
def listenForButton(listening):
    while listening:
        if gpio.input(BUTTON) == False:
            print("Listen Button pressed")
            listening = False
            with serial.Serial("/dev/ttyACM0", baudrate=115200, timeout=1) as arduino:
                with sr.Microphone() as source:
                    try:
                        # Calibrate for background
                        print("Silence please... Calibrating....")
                        r.adjust_for_ambient_noise(source, duration=2)

                        #   Turn LED on and listen for input
                        print("Speak when the LED is turned on")
                        gpio.output(LED, gpio.HIGH)     # Turn LED on
                        audio = r.listen(source, timeout=5, phrase_time_limit= 20)
                                               
                        gpio.output(LED, gpio.LOW)  # Turn LED off

                        # Proces speech to text
                        speech = r.recognize_google(audio)
                        print("You said: " + speech + '\n')

                        #   Translate to target language, detect origin langauge and display on LCD 
                        translationText, originLanguage = translateText(speech)
                        arduino.write(str.encode(translationText))

                        # Calibrate for background
                        print("Silence please... Calibrating....")
                        r.adjust_for_ambient_noise(source, duration=2)
                        
                        #   Turn LED on and listen for input
                        print("Speak when the LED is turned on")
                        gpio.output(LED, gpio.HIGH)     # Turn LED on
                        audio = r.listen(source, timeout=5, phrase_time_limit= 20)
                        gpio.output(LED, gpio.LOW)  # Turn LED off

                        #   Proces speech to text
                        speech = r.recognize_google(audio)
                        print("You said: " + speech + '\n')

                        #   Translate text to origin language and display on LCD
                        originTranslationText = translateOrigin(speech, originLanguage)
                        arduino.write(str.encode(originTranslationText))
                    #   Catch some errors
                    except sr.UnknownValueError:
                        print("Could not understand audio")
                        
                    except sr.RequestError as e:
                        print("Request error; {0}".format(e))

    return


# ------ MAIN ------ #
def main():
    try:
        while True:
            gpioInnit()
            print("Try a controller button")
            for event in gamepad.read_loop():
                if event.type == ecodes.EV_KEY:
                    if event.value == 1:
                        print("button pressed")
                        if event.code == plsBtn:
                            print("Plus")
                            listenForButton(True)
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