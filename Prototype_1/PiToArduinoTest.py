import serial
import time
# port = serial.Serial("/dev/ttyACM0", baudrate=11520, timeout=3.0)

import speech_recognition as sr

# def main():
        
#     print("Enter input to send to Arduino:")
#     inputToSend = input()

#     newText = inputToSend + "\n\r"
#     while True:
#         port.write(newText.encode("utf-8"))
#     # print("message send")

# main()

r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source, timeout=5, phrase_time_limit=20)
    
speech = r.recognize_google(audio)
print("DIR of speech: ")
print(dir(speech))
print("Type of speech: ")
print(type(speech))
print(speech)

with serial.Serial("/dev/ttyACM0", baudrate=115200, timeout=1) as arduino:
    time.sleep(0.1)
    if arduino.isOpen():
        print("{} connected".format(arduino.port))
        try:
            while True:
                # cmd = input("Enter input to send to Arduino: ")
                cmd = speech + "\n\r"
                print(cmd)
                arduino.write(cmd.encode("utf-16"))

                while arduino.inWaiting() == 0: pass
                if arduino.inWaiting() > 0:
                    received = arduino.readline()
                    print(received.decode())
                    arduino.flushInput()
        except KeyboardInterrupt:
            print("KeyboardInterrupt")
            arduino.close()