#langdetect --> pip install langdetect
#python_translator --> pip install python-translator
#speech_recognition --> pip install SpeechRecognition

#ADD BUTTON AND LED
#MIC INPUT
#TRANSLATE INPUT
#(MAKE CONNECTION WITH ARDUINO) /dev/ttyACM0
#ADD MOTORS
#TEXT OUTPUT ON LCD SCREEN

# from translate import Translator
from python_translator import Translator
from langdetect import detect
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
        if GPIO.input(BUTTON) == True:
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
        # audio = r.listen(source)
        audio = r.listen(source, timeout=5, phrase_time_limit=20)

    GPIO.output(LED, GPIO.LOW)
    speech = r.recognize_google(audio)
    print(speech)
    translateText(speech)


#TRANSLATE TEXT TO DUTCH
def translateText(speech):    
    translator = Translator()
    translationText = translator.translate(speech, "dutch")
    print(translationText)
    detectedSpeech = detect(speech)
    print(detectedSpeech)

if __name__ == "__main__":
    main()