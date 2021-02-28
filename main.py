import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from time import sleep

listener = sr.Recognizer()
program = pyttsx3.init()
voices = program.getProperty('voices')
program.setProperty('voice', voices[1].id)


def speak(text):
    program.say(text)
    program.runAndWait()


def user_input():
    try:
        with sr.Microphone() as source:
                speak('how may I help you today, Hiba?')
                print('listening...')
                voice = listener.listen(source)
                sleep(1)
                command = listener.recognize_google(voice)
                command = command.lower()
                if 'alexa' in command:
                    command = command.replace('alexa', '')
                return command
    except:
        pass

words_for_wiki = ['who is', 'what is', 'what does', 'why', 'wiki', 'wikipedia', 'define']

def run_alexa():
    global input_command
    input_command = user_input()
    print(input_command)
    understand = False

    if 'play' in input_command:
        song = input_command.replace('play', '')
        speak('playing' + song)
        pywhatkit.playonyt(song)
        understand = True
        sleep(4)
    elif 'time' in input_command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak(time)
        understand = True
    elif 'joke' in input_command:
        speak(pyjokes.get_joke())
        understand = True
    elif 'bye' in input_command:
        speak('See you later!')
        understand = True

    for term in words_for_wiki:
        if term in input_command and understand == False:
            search_term = input_command.replace(term, ' ')
            info = wikipedia.summary(search_term, 1)
            speak(info)
            understand = True

    if understand == False:
        speak('I could not understand what you said.')
        run_alexa()
    elif 'goodbye' not in input_command:
        run_alexa()

run_alexa()


