import speech_recognition as sr
import gtts
from playsound import playsound


r = sr.Recognizer()

def get_audio():
    with sr.Microphone() as source:
        print("Say something :)")
        audio = r.listen(source)
    return audio
   
def audio_to_text(audio):
    pass