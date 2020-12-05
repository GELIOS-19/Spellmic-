from gtts import gTTS
from playsound import  playsound
import time
import speech_recognition as sr
import os


def get_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('speak: ')
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
        except:
            print('not recognized')
            text = ''
        return text

def speech(text, lang, slow, file_name, repeat, sleep):
    text1=gTTS(text=text,lang=lang,slow=slow)
    text1.save(file_name)

    for _ in range(repeat):
        playsound(file_name)
        time.sleep(sleep)

    os.remove(file_name)



words = [('hello', 'en'), ('bonjour', 'fr'), ('ucuuba', 'pt')]

for word, lang in words:

    speech('Please spell ', 'en', False, 'general.mp3', 1, 0)
    speech(word, lang, False, 'word.mp3', 1, 1)

    ans = get_speech()
    print(ans)

    if ans == 'repeat':
        speech('Please spell ', 'en', False, 'general.mp3', 1, 0)
        speech(word, lang, False, 'word.mp3', 1, 1)

    elif ans == word:
        speech('Correct', 'en', False, 'correct.mp3', 1, 0)

    else:
        speech('Incorrect', 'en', False, 'correct.mp3', 1, 0)
