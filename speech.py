import speech_recognition as sr
import pyttsx3
from windows_work import play_overwatch, shutdown_timed
import processing
# Google Speech Recognition #
r = sr.Recognizer()
with sr.Microphone() as source:
    print('>> ')
    audio = r.listen(source)
google_sr = r.recognize_google(audio)

print('Google Speech Recognition thinks you said ' + google_sr)

def say(text):
    engine.say(text)
    engine.runAndWait()
    with open('speechlogs.txt', 'a') as sl:
        sl.write(text + '\n')
        sl.close()

# Python TTS #
engine = pyttsx3.init()

try:
    if google_sr == 'play OverWatch':
        play_overwatch()
        say('I am starting Overwatch, sir.')

    if google_sr == 'shut down in 30 seconds':
        shutdown_timed('30')
        say('Shutting down in T Minus 30 seconds. Goodnight sir.')


except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

processing.process(google_sr)