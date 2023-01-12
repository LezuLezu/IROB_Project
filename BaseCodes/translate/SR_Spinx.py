import speech_recognition as sr

from googletrans import Translator
translator = Translator()

r = sr.Recognizer()

pickUp = sr.AudioFile("D:/IROB_Coding/Project/BaseCodes/translate/pick-up-the-phone-1.wav")
with pickUp as source:
    audio = r.record(source)


try:
    text_record = r.recognize_sphinx(audio)

    translatedText = translator.translate(text_record, dest='nl')

    text_record2 = r.recognize_google(audio)
    translatedText2 = translator.translate(text_record2, dest='nl')
    print(translatedText.text)

except:
    print("Dindt recognize")
    pass
