import serial
import time
# port = serial.Serial("/dev/ttyACM0", baudrate=11520, timeout=3.0)
# to utf8 or ascii

import speech_recognition as sr
r = sr.Recognizer()

with serial.Serial("COM3", baudrate=115200, timeout=1) as arduino:
    # with serial.Serial("/dev/ttyACM0", baudrate=115200, timeout=1) as arduino:
    with sr.Microphone() as source:
        try:
            print("Silence please, calibrating...")
            r.adjust_for_ambient_noise(source, duration=2)
            print("calibrated, speak now...")
            audio = r.listen(source)
            text = r.recognize_google(audio)
            text = text.lower()
            print("You said "+text+"\n")
            arduino.write(str.encode(text))
            
            
        except sr.UnknownValueError:
            print("Could not understand audio")
            
        except sr.RequestError as e:
            print("Request error; {0}".format(e))