# Jarivs Assistant

# Modules
from win32com.client import Dispatch
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywhatkit

# Functions
def speak(text):
    '''This function is using to give voice output from the programme'''
    function_initializer = pyttsx3.init()
    function_initializer.say(text)
    function_initializer.runAndWait()

def greetings():
    '''This functions is using to welcome the user with voice'''
    current_time = datetime.datetime.now().hour
    print(current_time)
    if current_time > 0 and current_time < 12:
        speak("Good morning.")
    elif current_time >= 12 and current_time < 15:
        speak("Good noon.")
    elif current_time >= 15 and current_time < 17:
        speak("Good afternoon.")
    elif current_time >= 17 and current_time < 18:
        speak("Good evening.")
    else:
        speak("Good night.")

def voice_input():
    '''This function is using take voice input from the user'''
    function_initializer = sr.Recognizer()
    with sr.Microphone() as source:
        try :
            print("Listening...")
            audio = function_initializer.listen(source)
            text = function_initializer.recognize_google(audio, language = "en-US")
        except:
            print("Sorry. Say that again please.")
            speak("Sorry. Say that again please.")
            voice_input()
    return text


if __name__ == '__main__':
    greetings()

    while True:
        speak("How can I help you ?")
        user_query = voice_input().lower()

        if "wikipedia" in user_query:
            query = user_query.replace("wikipedia","")
            result = wikipedia.summary(query)
            print(result)
            speak(result)

        elif "open google" in user_query:
            webbrowser.open("google.com")

        elif "open youtube" in user_query:
            webbrowser.open("youtube.com")

        elif "open facebook" in user_query:
            webbrowser.open("facebook.com")

        elif "open chrome" in user_query:
            chrome_folder_path = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            speak("Opening chrome...")
            os.startfile(chrome_folder_path)

        elif "what's the time" in user_query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(current_time)
            print(current_time)

        elif "open music folder" in user_query:
            music_folder_path = "E:\My songs"
            os.startfile(music_folder_path)

        elif "play" in user_query:
            query = user_query.replace("play","")
            speak(f"Playing {query}")
            pywhatkit.playonyt(query)

        elif "quit" in user_query:
            speak("Thanks for using me. See you soon.")
            print("Thanks for using me. See you soon.")
            exit()

        else:
            speak("This option is not added yet.But I'm trying to search it on google")
            pywhatkit.search(user_query)