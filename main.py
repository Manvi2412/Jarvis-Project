import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os


recognizer=sr.Recognizer()
engine=pyttsx3.init()
newsapi=""

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    pygame.mixer.init()

    pygame.mixer.music.load('temp.mp3')

    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 


def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def aiprocess(command):
    client = OpenAI(
  api_key="",
)

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": command}
  ]
)

    return completion.choices[0].message.content

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r=requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=.......")
        if r.status_code == 200:
            data = r.json()
            
            articles = data.get('articles', [])
            
            for article in articles:
                speak_old(article['title'])
    else:
        
        output = aiprocess(c)
        speak_old(output) 

if __name__=="__main__":
    speak_old("Initializing Jarvis......")
    while True:
        r=sr.Recognizer()
        
        print("recognizing.....")
        try:
            with sr.Microphone() as source:
                print("Listening!")
                audio=r.listen(source,timeout=2,phrase_time_limit=1)
            
            word=r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak_old("Yeah")
                with sr.Microphone() as source:
                    print("Jarvis Active!")
                    audio=r.listen(source,timeout=2,phrase_time_limit=1)
                    command=r.recognize_google(audio)
                    processCommand(command)

            
        except Exception as e:
            print("Error; {0}".format(e))


            

