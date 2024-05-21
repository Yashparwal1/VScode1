# chatgpt api key: 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

import openai
import speech_recognition as sr #pip install speechRecognition
import pyttsx3 #pip install pyttsx3
import pyaudio, sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

global query

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def start():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in') # type: ignore
        return query
    except:
        return "None"

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') # type: ignore
        # print(f"User said: {query}\n")
        #speak(f": {query}\n")
        return query
    except:
        print("Say that again please...")  
        return "None"

def send_to_api(query):
    if query == "gpt stop":
        print("Ok, closing down..., BYE...")
        sys.exit(0)
    openai.api_key = "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"
    prompt = (f"User: {query}\n")
    response = openai.Completion.create(engine="text-davinci-002",prompt=prompt,max_tokens=1024)

    print(response.choices[0].text)
    speak(response.choices[0].text)
    
if __name__ == "__main__":
    print("Speak 'gpt' to start... ")
    for i in range(5):
        getname = start()
        if getname.lower() == "gpt":
            query = takeCommand()
            send_to_api(query)
            break
        else:
            print("Please Speak out 'gpt' to start")
while True:
    query = takeCommand().lower()
    send_to_api(query)