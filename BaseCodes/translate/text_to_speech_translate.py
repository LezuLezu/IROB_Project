import speech_recognition as sr

from googletrans import Translator
translator = Translator()

r = sr.Recognizer()

with sr.Microphone() as source:
    print("You can speak now")
    audio = r.listen(source, timeout=5, phrase_time_limit=5)
    print("Time Over")

#Default Mic as source, it listens

try:
    # print("TEXT: "+r.recognize_google(audio))
    text_record = r.recognize_google(audio)
    #Prints the Output

    translatedText = translator.translate(text_record, dest='nl')
    print(translatedText.text)

except:
    pass
    #Does nothing, if error occurred(No error is showed on-scree)