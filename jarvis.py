import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import os
import webbrowser
import smtplib
import pywhatkit


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning!')
    elif hour>=12 and hour<18:
        speak('Good Afternoon Aansh Bhai!')
    else:
        speak('Good evening')
    speak("I am Jarvis. Please tell me how may I help you")

def sendEmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sagaraansh@gmail.com', '1809aansh')
    server.sendmail('sagaraansh@gmail.com', to, content)
    server.close()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print('Recognizing....')
        query=r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query
    except Exception as e:
        print('Say that again please...')
        return "None"

if __name__=="__main__":
    wishme()
    
    while True:
        query=takeCommand()
        query=query.lower()
        print(query)
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query=query.replace("wikipedia", "")
            results=wikipedia.summary(query, sentences=2)
            speak("According to wikipedia..")
            speak(results)

        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strtime}")

        elif 'open code' in query:
            codePath="C:\\Users\\Aansh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open('https://www.google.com')
        
        elif 'email to ansh' in query:
            try:
                speak("what should I say")
                content=takeCommand()
                to='aansh.sagar18@siesgst.ac.in'
                sendEmail(to, content)
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("Sorry Aansh. I am not able to send this email")

        elif 'shefali' in query:
            speak('What should I say')
            content=takeCommand()
            pywhatkit.sendwhatmsg("+919619413489", content, datetime.datetime.now().hour, datetime.datetime.now().minute+2)
        