# from translate import Translator
import speech_recognition as sr
from python_translator import Translator
from langdetect import detect

#BASIS TRANSLATE FROM TEXT
# text = "Hello"
# translator= Translator(to_lang="de")
# translation = translator.translate(text)
# print(translation)


#SPEECH TO TEXT FROM AUDIOFILE WITH TRANSLATION AND LANGUAGE DETECTION
# r = sr.Recognizer()
# audioTest = sr.AudioFile('audio.wav')
# with audioTest as source:
#     audio = r.record(source)
# try:
#     s = r.recognize_google(audio)
#     print("Text: " +s)
    
# except Exception as e:
#     print("Exception: " +str(e))
    
# translator = Translator()
# translation = translator.translate(s, "dutch")
# print(translation)  
# print(detect(s))

#SPEECH TO TEXT WEBCAM MIC
# r = sr.Recognizer()
# with sr.Microphone() as source:
#     r.adjust_for_ambient_noise(source)
#     print("Say something!")
#     # audio = r.listen(source)
#     audio = r.listen(source, timeout=5, phrase_time_limit=20)

# a = r.recognize_google(audio)
# print(a)
# translator = Translator()
# translation = translator.translate(a, "dutch")
# print(translation)
# print(detect(a))



#DETECT TEXT LANGUAGE
text = "hello how are you"
translator = Translator()
result = translator.translate(text, "dutch")
print(result)

detectedLang = detect(text)
print(detectedLang)

resText = "goed en met jou"
resResult = translator.translate(resText, detectedLang)
print(resResult)

    