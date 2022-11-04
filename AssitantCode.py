import os
import pywhatkit
import pyttsx3
import pyjokes
import time
import webbrowser
import speech_recognition as sr
import wikipedia
import datetime

Bossname = 'Satya Narayana'

def speak(audio):
    engine = pyttsx3.init()
    #To know the current system voice model
    '''
    voices = engine.getProperty('voices')
    for voice in voices:
        print(voice.name)
        print(voice.id)
    '''
    femalevoice = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    engine.setProperty('voice',femalevoice)
    engine.say(audio)
    engine.runAndWait()

def takeCommand():

    mic = sr.Recognizer()
    with sr.Microphone() as source:

        print("Listening...")
        mic.pause_threshold = 1
        audio = mic.listen(source)

    try:
        print("Recognizing...")
        command = mic.recognize_google(audio,language='en-in')
        print(f"Boss Said : {command}\n")

    except Exception as e:
        print(e)
        print("Sorry Boss I doesn't understand")
        print("Plz Repeat it again \n")
        return "Empty"
    
    return command


def wishBoss():

    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Boss !")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon Boss !")  
  
    else:
        speak("Good Evening Boss !") 
  
    assistant = "Friday"
    speak("This is Friday")
    speak("Your Virtual Assistant")

def getBossDetails():
    speak("Tell me your name")
    global Bossname
    try:
        Bossname = takeCommand()
        print("Boss Changed Succesfully")
    except Exception as e:
        print("Boss unchanged")


def whoami():
    speak(Bossname)
    speak("You are my Boss")


def tellDay():
    day = datetime.datetime.today().weekday() + 1
      
    Day_dict = {1: 'Monday', 2: 'Tuesday', 
                3: 'Wednesday', 4: 'Thursday', 
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
      
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("Today is " + day_of_the_week + "Boss")

def tellTime():
      
    time = str(datetime.datetime.now())
      
    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak("The time is sir" + hour + "Hours and" + min + "Minutes")

def NumDetails():
    import phonenumbers
    from phonenumbers import geocoder
    number = "+9182593312"
    chnum = phonenumbers.parse(number,"CH")
    print("COUNTRY : " + geocoder.description_for_number(chnum,"en"))

    from phonenumbers import carrier
    service_number = phonenumbers.parse(number,"RO")
    print("CARRIER : " + carrier.name_for_number(service_number,"en"))  

def runFriday():

    wishBoss()

    i = 0
    while (i < 3):
        command = takeCommand().lower()

        if 'who am i' in command:
            whoami()
            continue
        elif 'bye' in command or 'exit' in command:
            speak("Good bye Boss")
            exit()
        elif 'friday' in command:
            speak("Yes Boss")
            speak("What I have to do")
            continue
        elif 'what is your full name' in command:
            speak("My name is")
            speak("Female Replacement Intelligent Digital Assistant Youth")
            continue
        elif 'joke' in command:
            speak(pyjokes.get_joke())
            continue
        elif 'tell me the time' in command:
            tellTime()
            continue
        elif 'which day it is' in command:
            tellDay()
            continue
        elif "open google" in command:
            speak("Opening Google ")
            webbrowser.open("www.google.com")
            continue
        elif "open youtube" in command:
            speak("Opening youtube")
            webbrowser.open("https://www.youtube.com/")
            continue
        elif "open vs" in command:
            speak("opening visual studio")
            vscode = r"Microsoft VS Code\Code.exe"
            os.startfile(vscode)
        elif "tell me your name" in command:
            speak("I am Friday  Your deskstop Assistant")
            continue
        elif "change boss" in command:
            getBossDetails()
            continue
        elif "who made you" in command or "who created you" in command:
            speak("I have been created by Satya Narayana")
            continue
        elif 'what is love' in command :
            speak("It is 7th sense that destroy all other senses")
            continue
        elif "i love you" in command:
            speak("There is nothing better than hearing you say that   Boss ")
            continue
        elif "get number details" in command or "trace number" in command:
            speak("tracing number")
            NumDetails()

        i = i+1

    
