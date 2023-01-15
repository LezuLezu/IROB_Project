from translate import Translator
import speech_recognition as sr

#BASIS TRANSLATE FROM TEXT
# text = "Hello"
# translator= Translator(to_lang="de")
# translation = translator.translate(text)
# print(translation)

#SPEECH TO TEXT FROM AUDIOFILE
# r = sr.Recognizer()
# audioTest = sr.AudioFile('audio.wav')
# with audioTest as source:
#     audio = r.record(source)
# try:
#     s = r.recognize_google(audio)
#     print("Text: " +s)
    
# except Exception as e:
#     print("Exception: " +str(e))
    
# translator = Translator(to_lang="nl")
# translation = translator.translate(s)
# print(translation)  

#SPEECH TO TEXT WEBCAM MIC
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
    # audio = r.listen(source, timeout=5, phrase_time_limit=5)

a = r.recognize_google(audio)
print(a)


#  audio = r.listen(source, timeout=5, phrase_time_limit=5)

    