#ADD BUTTON AND LED
#MIC INPUT
#TRANSLATE INPUT
#TEXT OUTPUT ON LCD SCREEN

from translate import Translator
import speech_recognition as sr
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
from time import sleep

#DECLERATIONS
BUTTON = 7
LED = 11

def main():
    #SETUPS
    GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(LED, GPIO.OUT)
    GPIO.output(LED, GPIO.LOW)
    
    #BUTTON PRESSED
    while True:
        if GPIO.input(BUTTON) == False:
            print("button pressed")        
            speechToText()
            sleep(0.3)

#SPEECH TO TEXT WEBCAM MIC 
def speechToText():
    print("speechToText")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something when the light is on")
        GPIO.output(LED, GPIO.HIGH)
        audio = r.listen(source)
        # audio = r.listen(source, timeout=5, phrase_time_limit=5)

    GPIO.output(LED, GPIO.LOW)
    speech = r.recognize_google(audio)
    print(speech)
    translateText(speech)


#TRANSLATE TEXT TO DUTCH
def translateText(speech):    
    translator = Translator(to_lang="nl")
    translationText = translator.translate(speech)
    print(translationText)    

if __name__ == "__main__":
    main()