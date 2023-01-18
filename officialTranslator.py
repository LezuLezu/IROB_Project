#ADD BUTTON AND LED
#MIC INPUT
#TRANSLATE INPUT
#(MAKE CONNECTION WITH ARDUINO) /dev/ttyACM0
#ADD MOTORS
#TEXT OUTPUT ON LCD SCREEN


#IMPORTS
from python_translator import Translator
from langdetect import detect
import speech_recognition as sr
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
from time import sleep

#DECLERATIONS
BUTTON1 = 7
LED = 11

def main():
    #SETUPS
    GPIO.setup(BUTTON1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(LED, GPIO.OUT)
    GPIO.output(LED, GPIO.LOW)
    

    #BUTTON PRESSED
    while True:
        if GPIO.input(BUTTON1) == False:
            print("button1 pressed")        
            audio = speechToText()
            speech = recognizeSpeech(audio)
            detectedLang = translateText(speech)
            translateOriginLang(detectedLang)
            sleep(0.3)


#INPUT SPEECH VIA WEBCAM MIC 
def speechToText():
    print("speechToText")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something when the light is on")
        GPIO.output(LED, GPIO.HIGH)
        # audio = r.listen(source)
        audio = r.listen(source, timeout=5, phrase_time_limit=20)
    GPIO.output(LED, GPIO.LOW)
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
    print(translationText)
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
    print(originLangText)


#MAIN
if __name__ == "__main__":
    main()