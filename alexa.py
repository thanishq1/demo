import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys

listener = sr.Recognizer()
engine = pyttsx3.int()

voices = engine.getProperty('voices')

if len(voices) > 1:
    engine.setProperty()('voice', voice[1].id)
else:
    engine.setProperty()('voice', voice[0].id)

def engine_talk(text):
    print(f"Alexa is saying: {text}")
    engine.say(text)
    enging.runAndWait()

def user_commands():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noice(source)
            print("Start Speaking!!")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(f"User Said: {command}")
                return command
    except Exception as e:
        print(f"Error: {e}")
    return ""

def run_alexa():
    command = user_commands()
    if commands:
        if 'play' in command:
            song = command.replace('play','')
            engine_talk('playing' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().srtftime('%I:%M:%p')
            enging_talk('The current time is' + time)
        elif 'who is' in command:
            name = command.replace('who is', '')
            info = wikipedia.summary(name, 1)
            print(info)
            engine_talk(info)
        elif 'joke' in command:
            engine_talk(pyjokes.get_joke())
        elif 'stop' in command:
            sys.exit()
        else:
            engine_talk(' I could not hear you properly')
    else:
        engine_talk('I did not catch that. Please speak again')

while True:
    run_alexa()
        































    
    
