import RPi.GPIO as GPIO
import time
    # PyAudio for audio input
import pyaudio
    #  speech recognition
import speech_recognition as sr
    # Google translate
from googletrans import Translator
    # OS
import os

translator = Translator()
r = sr.Recognizer()
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#DECLERATIONS
LED = 16
BUTTON = 18


#SETUPS
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def speechToText():
    print("In functie SpeechToText")
    # USER TALKS IN MIC
    r = sr.Recognizer()
    r.energy_threshold = 500
    mic = sr.Microphone()


    with mic as source:
        # LED ON    
        GPIO.output(LED, GPIO.HIGH)
        print("You can speak now")    
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=5, phrase_time_limit=5)
        print("Time Over")
        # LED OFF
        GPIO.output(LED, GPIO.LOW)
        
    
    try:
        print("voice text")
        print("TEXT: "+r.recognize_google(audio))
        
    except:
        print("sorry, could not recognise")

if __name__ == "__main__":
    running = True
    while running:   
        button_state = False     
    #BUTTON PRESSED (misschien dat die alleen werkt als je de knop ingedrukt houdt)
        if GPIO.input(BUTTON) == True:
            button_state = True
        else:
            button_state = False
        time.sleep(0.2)
        if button_state:
            print("button pressed")
            speechToText()
            #talk in mic