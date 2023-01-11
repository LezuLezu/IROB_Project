import RPi.GPIO as GPIO
import time
    # PyAudio for audio input
import pyaudio
    #  speech recognition
import speech_recognition as sr
    # Google translate
from googletrans import Translator

translator = Translator()
r = sr.Recognizer()
GPIO.setmode(GPIO.BMC)

#DECLERATIONS
LED = 16
BUTTON = 18


#SETUPS
GPIO.setup(LED, GPIO.OUTPUT)
GPIO.output(LED, GPIO.LOW)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def speechToText():
    
    #USER TALKS IN MIC
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=1)

    RPIOutputs = sr.Microphone.list_microphone_names()
    print(RPIOutputs)


    with mic as source:
        print("You can speak now") 
        # LED ON    
        GPIO.output(LED, GPIO.HIGH)
        audio = r.listen(source, timeout=5, phrase_time_limit=5)
        print("Time Over")
        # LED OFF
        GPIO.output(LED, GPIO.LOW)
        
    
    try:
        print("voice text")
        print("TEXT: "+r.recognize_google(audio))
        
    except:
        pass

if __name__ == "__main__":
    
#BUTTON PRESSED (misschien dat die alleen werkt als je de knop ingedrukt houdt)
    if GPIO.input(BUTTON) == False:
        print("button pressed")
        speechToText()
        #talk in mic