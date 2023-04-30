# Project -  News reader
from win32com.client import Dispatch
import json
import requests

def speak(str):
    speaker = Dispatch("Sapi.SpVoice")
    print(str)
    speaker.Speak(str)

news_url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=5137df215b844aeea48dd824beed6847"
news_request = requests.get(news_url).text
news_dict_converter = json.loads(news_request)
article = news_dict_converter["articles"]

starting = speak("Welcome to News reader... Top headlines from Techcrunch :")
for reader in article:
    speak(reader["title"])

greetings = speak("Thanks for using News reader...")