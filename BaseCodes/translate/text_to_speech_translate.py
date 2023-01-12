import speech_recognition as sr

from googletrans import Translator
translator = Translator()

r = sr.Recognizer()

# micIndex = sr.Microphone.list_microphone_names()
# print(micIndex)

#with sr.Microphone(device_index=  2 ) as source:
audiofile =  sr.AudioFile('/home/pi/projects/IROB_project/BaseCodes/translate/pick-up-the-phone-1.wav')
with audiofile as source:
    print("You can speak now")
    # audio = r.listen(source, timeout=5, phrase_time_limit=5)
    # r.adjust_for_ambient_noise(source)
    audio = r.record(source)
    print("Time Over")

#Default Mic as source, it listens

try:
    print("TEXT: "+r.recognize_google(audio))
    text_record = r.recognize_google(audio)
    #Prints the Output

    translatedText = translator.translate(text_record, dest='nl')
    print(translatedText.text)

except:
    print("Didnt recognize anything")
    pass
    #Does nothing, if error occurred(No error is showed on-screen)