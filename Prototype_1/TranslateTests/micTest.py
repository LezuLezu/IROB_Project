import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone(device_index=1)

RPIOutputs = sr.Microphone.list_microphone_names()
print(RPIOutputs)


with mic as source:
    print("You can speak now")
    audio = r.listen(source, timeout=5, phrase_time_limit=5)
    print("Time Over")
    
 
try:
    print("voice text")
    print("TEXT: "+r.recognize_google(audio))
    
except:
    pass