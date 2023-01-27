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
gamepad = InputDevice('/dev/input/event1')
#   Recongizer object
r = sr.Recognizer()
#   translator object
translator = Translator()
#   Serial port to arduino
serialPort = serial.Serial("/dev/ttyACM0", baudrate=9600, timeout=1) 

# ------ VARIABLE DECLERATIONS ------ #
# Language Target 
targetLanguage = "nl"
#   LED
LED = 11
#   Button
BUTTON = 7

#   Motors
#   A motor -> Left
dcMotor_A1A = 35
dcMotor_A1B = 37
#   B Motor -> Right
dcMotor_B1B = 29
dcMotor_B1A = 31

#   Button code variables (switch pro controller)
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

# Language dict
LANGUAGES = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'am': 'amharic',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'eu': 'basque',
    'be': 'belarusian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh-cn': 'chinese (simplified)',
    'zh-tw': 'chinese (traditional)',
    'co': 'corsican',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'fy': 'frisian',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'hebrew',
    'he': 'hebrew',
    'hi': 'hindi',
    'hmn': 'hmong',
    'hu': 'hungarian',
    'is': 'icelandic',
    'ig': 'igbo',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'korean',
    'ku': 'kurdish (kurmanji)',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'lb': 'luxembourgish',
    'mk': 'macedonian',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar (burmese)',
    'ne': 'nepali',
    'no': 'norwegian',
    'or': 'odia',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sm': 'samoan',
    'gd': 'scots gaelic',
    'sr': 'serbian',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'so': 'somali',
    'es': 'spanish',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'swedish',
    'tg': 'tajik',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'ug': 'uyghur',
    'uz': 'uzbek',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu'
}

#   base messages to display to user on lcd
startMessage = "Press the button to start your translation\n\r"
lightMessage = "Say something when the light is on\n\r"


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
    
    gpio.output(dcMotor_A1A, gpio.LOW)
    gpio.output(dcMotor_A1B, gpio.LOW)
    gpio.output(dcMotor_B1B, gpio.LOW)
    gpio.output(dcMotor_B1A, gpio.LOW)

# ------ MOTOR DIRECTIONS ------ #
#   Motor Left
def motorLeft(sec):
    print("Left")
#   Motor Right
    gpio.output(dcMotor_A1A, True)
    gpio.output(dcMotor_A1B, False)
#   Motor Left
    gpio.output(dcMotor_B1A, True)
    gpio.output(dcMotor_B1B, False)
    time.sleep(sec)
    
#   Motor Right
def motorRight(sec):
    print("Right")
#   Motor Right
    gpio.output(dcMotor_A1A, False)
    gpio.output(dcMotor_A1B, True)
#   Motor Left
    gpio.output(dcMotor_B1A, False)
    gpio.output(dcMotor_B1B, True)
    time.sleep(sec)

#   Motor Reverse
def motorReverse(sec):
    print("Reverse")
#   Motor Right
    gpio.output(dcMotor_A1A, True)
    gpio.output(dcMotor_A1B, False)
#   Motor Left
    gpio.output(dcMotor_B1A, False)
    gpio.output(dcMotor_B1B, True)
    time.sleep(sec)

#   Motor Forward
def motorForward(sec):
    print("Forward")
#   Motor Right
    gpio.output(dcMotor_A1A, False)
    gpio.output(dcMotor_A1B, True)
#   Motor Left
    gpio.output(dcMotor_B1A, True)
    gpio.output(dcMotor_B1B, False)
    time.sleep(sec)

# ------ Arduino ------ #
def toArduino(message):
    if serialPort.isOpen():
        print("{} connected".format(serialPort.port))
        serialPort.write(str.encode(message))
        time.sleep(1.5)
        received = serialPort.readline().decode()
        print(received)
        serialPort.flushInput()
        return True
    else:
        print("serial Unavailable")

# ------ Translation ------ #
#   Get audio from microphone
def listenToAudio(source):
    received = toArduino(lightMessage)
    if received == True:
        print("Silence please, calibrating...")
        r.adjust_for_ambient_noise(source, duration=2)
        print("Say something when the light is on")
        gpio.output(LED, gpio.HIGH)
        audio = r.listen(source, timeout=5, phrase_time_limit=20)
        gpio.output(LED, gpio.LOW)
        print("LED OFF")
        return audio
  
#   Translate text to target language and detect origin langauge
def translateText(speech):    
    translationText = translator.translate(speech, targetLanguage)
    translationText_String = translationText.new_text + "\n\r"
    print("Translation text: " + str(translationText.new_text))
    detectedLang = detect(speech)
    print("Detected language: " + str(detectedLang))
    return translationText_String, detectedLang


#   Translate target language to origin language
def translateOriginLang(speech, detectedLang):
    originLangText = translator.translate(speech, LANGUAGES[detectedLang])
    print(LANGUAGES[detectedLang])
    translationText_String = originLangText.new_text + "\n\r"
    return translationText_String

# Listen for hardware button
def listenForButton(listening):
    received = toArduino(startMessage)
    if received == True:
        while listening:
            if gpio.input(BUTTON) == True:
                listening = False
                print("Button to start pressed")
                # Set up serial port to arduino and microphone source object
                # with serialPort  as arduino:
                with sr.Microphone() as source:
                    try:
                        #   Listen to audio and display what user said on terminal
                        audio = listenToAudio(source)
                        speech = r.recognize_google(audio)
                        print("You said "+speech+"\n")

                        #  Translate text to target language and send to arduino for display
                        translationText, detectedLang = translateText(speech)
                        # arduino.write(str.encode(translationText))  
                        received = toArduino(translationText)

                        #   Listen to audio and display what user said on terminal
                        audio = listenToAudio(source)
                        speech = r.recognize_google(audio, language=targetLanguage)
                        print("You said "+speech+"\n")

                        #   Translate text to detected language and send to arduino for display
                        originLangText = translateOriginLang(speech, detectedLang)
                        # arduino.write(str.encode(originLangText))  
                        received = toArduino(originLangText)
                    #   Error handling            
                    except sr.UnknownValueError:
                        print("Could not understand audio")
                        
                    except sr.RequestError as e:
                        print("Request error; {0}".format(e))

# ------ MAIN ------ #
def main():
    try:
        while True:
            #   Set up board, pins and in/outputs
            gpioInnit()
            print("Try a controller button")
            #   Listen for controller button input
            for event in gamepad.read_loop():
                if event.type == ecodes.EV_KEY:
                    if event.value == 1:
                        print("button pressed")
                        if event.code == plsBtn:
                            #   + button pressed -> listen for button input
                            print("Plus")
                            listenForButton(True)
                        if event.code == aBtn:
                            #   A button pressed -> move right
                            print("A")
                            motorRight(1)
                        elif event.code == bBtn:
                            #   B button pressed -> move backwards
                            print("B")
                            motorReverse(1)
                        elif event.code == yBtn:
                            #   Y button pressed -> move left
                            print("Y")
                            motorLeft(1)
                        elif event.code == xBtn:
                            #   X button pressed -> move forward
                            print("X")
                            motorForward(1)
                        elif event.code == hmBtn:
                            #   Home button pressed -> stop motors
                            # Stop motors
                            print("Stop")
                            gpio.cleanup()
                            gpioInnit()

            # cleanup pins
            gpio.cleanup()
    #   Error handling
    except KeyboardInterrupt:
        gpio.cleanup()
        print("KeyboardInterrupt")
    except Exception as e:
        gpio.cleanup()
        print(e)

if __name__ == "__main__":
    main()  