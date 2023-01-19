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
import serial

#DECLERATIONS
BUTTON1 = 7
LED = 11


def main():
    #SETUPS
    r = sr.Recognizer()
    GPIO.setup(BUTTON1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(LED, GPIO.OUT)
    GPIO.output(LED, GPIO.LOW)

    while True:
        if GPIO.input(BUTTON1) == True:
            with serial.Serial("/dev/ttyACM0", baudrate=115200, timeout=1) as arduino:
                with sr.Microphone() as source:
                    try:
                        print("Silence please, calibrating...")
                        r.adjust_for_ambient_noise(source, duration=2)
                        print("Say something when the light is on")
                        # arduino.write(str.encode("Say something when the light is on"))
                        GPIO.output(LED, GPIO.HIGH)
                        audio = r.listen(source, timeout=5, phrase_time_limit=20)
                        GPIO.output(LED, GPIO.LOW)
                        speech = r.recognize_google(audio)
                        print("You said "+speech+"\n")

                        translationText, detectedLang = translateText(speech)
                        arduino.write(str.encode(translationText))      #DUTCH TO ARDUINO

                        r.adjust_for_ambient_noise(source, duration=2)
                        print("Say something back when the light is on")
                        # arduino.write(str.encode("Say something back when the light is on"))
                        GPIO.output(LED, GPIO.HIGH)
                        audio = r.listen(source, timeout=5, phrase_time_limit=20)
                        GPIO.output(LED, GPIO.LOW)
                        speech = r.recognize_google(audio, language="nl")
                        print("You said "+speech+"\n")

                        originLangText = translateOriginLang(speech, detectedLang)
                        arduino.write(str.encode(originLangText))      #ORIGIN LANGUAGE TO ARDUINO

                                  
                    except sr.UnknownValueError:
                        print("Could not understand audio")
                        
                    except sr.RequestError as e:
                        print("Request error; {0}".format(e))


#TRANSLATE TEXT TO DUTCH
def translateText(speech):    
    translator = Translator()
    translationText = translator.translate(speech, "dutch")
    translationText2 = translationText.new_text
    print(translationText.new_text)
    detectedLang = detect(speech)
    print(detectedLang)
    return translationText2, detectedLang


#TRANSLATE DUTCH BACK TO ORIGINAL LANGUAGE
def translateOriginLang(speech, detectedLang):
    translator = Translator()
    originLangText = translator.translate(speech, detectedLang)
    originLangText2 = originLangText.new_text
    return originLangText2


#MAIN
if __name__ == "__main__":
    main()            