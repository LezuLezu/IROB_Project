#ADD BUTTON AND LED
#MIC INPUT
#TRANSLATE INPUT
#TEXT OUTPUT ON LCD SCREEN

from translate import Translator
import speech_recognition as sr
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
from time import sleep

def main():
    #DECLERATIONS
    BUTTON = 7

    #SETUPS
    GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    #BUTTON PRESSED
    while True:
        if GPIO.input(BUTTON) == False:
            print("button pressed")        
            speechToText()
            sleep(0.15)


#SPEECH TO TEXT WEBCAM MIC 
def speechToText():
    print("speechToText")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        # audio = r.listen(source, timeout=5, phrase_time_limit=5)

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