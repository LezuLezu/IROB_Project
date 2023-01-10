# https://pypi.org/project/googletrans/

from googletrans import Translator
translator = Translator()
# translator.translate(dest=nl text='this is a test')
translatedText = translator.translate('This is a pen.', dest='nl')
print(translatedText.text)