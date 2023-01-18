# Imorts
    # GPIO for pi pins control
import RPi.GPIO as gpio
    # Time for delays
import time
    # PyAudio for audio input
import pyaudio
    #  speech recognition
import speech_recognition as sr
    # Google translate
from googletrans import Translator

translator = Translator()
r = sr.Recognizer()


# Variables
    # Button
button = 36
    # LED
LED = 38
    # Mic

if __name__ == '__main__':
    try:
        with sr.Microphone() as source:
            print("You can speak now")
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            print("Time Over")        
        try:
            # print("TEXT: "+r.recognize_google(audio))
            text_record = r.recognize_google(audio)
            #Prints the Output
            translatedText = translator.translate(text_record, dest='nl')
            print(translatedText.text)
        except:
            pass
    except KeyboardInterrupt:
        print("Keyboard interrupt")
        gpio.cleanup()
    except:
        print("Other error or exception occured!")