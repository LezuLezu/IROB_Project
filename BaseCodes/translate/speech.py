import speech_recognition as sr
#Needed Module

r = sr.Recognizer()
#Initializes r for Recognizer()

with sr.Microphone() as source:
    print("You can speak now")
    audio = r.listen(source, timeout=5, phrase_time_limit=5)
    print("Time Over")

#Default Mic as source, it listens

try:
    print("TEXT: "+r.recognize_google(audio));
    #Prints the Output

except:
    pass;
    #Does nothing, if error occurred(No error is showed on-scree)