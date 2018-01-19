import speech_recognition as sr
import logging
logger = logging.getLogger(__name__)
r = sr.Recognizer()
with sr.Microphone() as source:

    while True:
        logger.debug('Awaiting User Input.')
        audio = r.listen(source)
        try:
            result = r.recognize_google(audio)
            print(result)
        except sr.UnknownValueError:
            logger.debug("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            logger.warn("Could not request results from Google Speech Recognition service: %s", e)
        except Exception as e:
            logger.error("Could not process text: %s", e)

