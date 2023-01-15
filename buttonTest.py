import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
from time import sleep
from translate import Translator
import speech_recognition as sr

def main():
    #DECLERATIONS
    # LED = 16
    BUTTON = 7


    #SETUPS
    # GPIO.setup(LED, GPIO.OUTPUT)
    # GPIO.output(LED, GPIO.LOW)
    GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    while True:
        if GPIO.input(BUTTON) == False:
            print("button pressed")        
            speechToText()
            sleep(0.15)
                
                
            
def speechToText():
    print("speechToText")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        # audio = r.listen(source, timeout=5, phrase_time_limit=5)

    speech = r.recognize_google(audio)
    print(speech)
    
    translator = Translator(to_lang="nl")
    translationText = translator.translate(speech)
    print(translationText)
    
    
    
if __name__ == "__main__":
    main()
    

#LED ON 
    # GPIO.output(LED, GPIO.HIGH)
    
    #USER TALKS IN MIC
    # r = sr.Recognizer()
    # mic = sr.Microphone(device_index=1)

    # RPIOutputs = sr.Microphone.list_microphone_names()
    # print(RPIOutputs)


    # with mic as source:
    #     print("You can speak now")
    #     audio = r.listen(source, timeout=5, phrase_time_limit=5)
    #     print("Time Over")
        
    
    # try:
    #     print("voice text")
    #     print("TEXT: "+r.recognize_google(audio))
        
    # except:
    #     pass