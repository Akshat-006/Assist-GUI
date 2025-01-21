import pyttsx3                                    # pip install pyttsx3
import requests
import speech_recognition as sr                   # pip install SpeechRecognition
import datetime
import time 
import os
import os.path
import sys
import cv2                                 # pip install opencv-python or pip3 install opencv-python==3.4.13.47
import random
from requests import get
import wikipedia                                  # pip install wikipedia
import webbrowser
import pyjokes                                    # pip install pyjokes
import pyautogui                                  # pip install pyautogui
import PyPDF2                                     # pip install PyPDF2
import operator
from bs4 import BeautifulSoup
from wikipedia.wikipedia import search
from pywikihow import search_wikihow              # pip install pywikihow


# GUI
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from GUI import Ui_JarvisGUI # change this line only

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Speak
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# Wish
def wishMe():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
    if hour>=0 and hour<12:
        speak(f"Good Morning Sir, its {tt}")

    elif hour>=12 and hour<18:
        speak(f"Good Afternoon Sir, its {tt}")

    else:
        speak(f"Good Evening Sir, its {tt}")
    
    speak("I am Friday Sir. tell me how may I help you")

# Process functions
def news():
    main_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=e44a5ef8ff6848158b21b486eb54f72f'

    mainpage = requests.get(main_url).json()
    articles = mainpage["articles"]
    head = []
    day=["first", "second", "third","fourth", "fifth", "sixth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")

def pdf_reader():
    pdfname = ("")
    book = open(f"{pdfname}", 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"Total pages in this book are {pages} ")
    speak("Sir which page do you want me to read")
    pg = int(input("Enter the page number: "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)


class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.taskExecution()
        

    # Take command
    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening...')
            r.pause_threshold = 1
            audio = r.listen(source, timeout=3,phrase_time_limit=5)
        
        try:
            print('Recognizing...')
            query = r.recognize_google(audio, language='en-in') 
            print(f"User Said: {query}")

        except Exception as e :
            speak("Say that again please")
            return "none"
        return query

    # Main function
    def taskExecution(self):
        wishMe()
        while True:
            self.query = self.takecommand().lower()
        
        # general commands
            if 'hello' in self.query:
                speak("o, hello sir")
            elif 'how are you' in self.query:
                speak("i am fine sir and what about you")
            elif 'good' in self.query:
                speak("That's Great to hear from you")
            elif 'not' in self.query:
                speak("Well, there are some concequences")

            elif "sleep" in self.query:
                speak("ok sir, call me when you want")
                break

            elif "thanks" in self.query or "thank you" in self.query:
                speak("no problem sir")

        # system functions
            elif 'the time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is {strTime}")

            elif 'alarm' in self.query:
                speak("at what time. for example, set alarm to 5:30 a.m.")
                tt = self.takecommand().lower()
                tt = tt.replace("to", "")
                tt = tt.replace(".","")
                tt = tt.upper()
                import MyAlarm
                MyAlarm.alarm(tt)

            elif 'play music' in self.query:
                music_dir = 'H:\\Songs'
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                os.startfile(os.path.join(music_dir, rd))

            elif 'hide all files' in self.query or 'hide this folder' in self.query or 'visible for everyone' in self.query:
                speak("Sir, do you want to hide this folder or make it visible.")
                condition = self.takecommand().lower()
                if "hide" in condition:
                    os.system("attrib +h /s /d")
                    speak("Sir, all files in this folder are hidden. i am sure you know what you have done")
                    if "yes i" in condition:
                        speak("Ok sir, i wont suspect you")

                elif "visible" in condition:
                    os.system('attrib -h /s /d')
                    speak("Sir all the files in this folder are now visible, i hope you know what you are doing.")
                    if "I know" in condition:
                        speak("ok sir")

                elif "leave it" in condition or "leave for now" in condition:
                    speak("Ok sir")

            elif 'calculate' in self.query or 'calculations' in self.query:
                try:    
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                        speak ("what do you want to calculate sir")
                        print("listening...")
                        r.adjust_for_ambient_noise(source)
                        audio = r.listen(source)
                    my_string = r.recognize_google(audio)
                    print(my_string)
                    def get_operator_fn(op):  
                        return {
                        '+' : operator.add, #plus  
                        '-' : operator.sub, #sub
                        'x' : operator.mul, #mul
                        'divided' : operator.__truediv__, #div
                        }[op]
                    def eval_binary_expr(op1, oper, op2):
                        op1,op2 = int(op1), int(op2)
                        return get_operator_fn(oper)(op1, op2)
                    speak("your result is")
                    speak(eval_binary_expr(*(my_string.split())))
                except Exception as e :
                    speak("Say that again please")
                    return "none"
                return self.query

            elif 'screenshot' in self.query:
                speak("sir, please tell me name for this screenshot")
                name1 = self.takecommand().lower()
                speak("ok sir, taking screenshot")
                time.sleep(5)
                img = pyautogui.screenshot()
                img.save(f"{name1}.jpg")
                speak("Sir, screenshot has been taken")

            elif 'switch window' in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab") 
                time.sleep(2)
                pyautogui.keyUp("alt")

            elif 'volume up' in self.query or 'increse volume' in self.query:
                pyautogui.press("volumeup")
            
            elif 'volume down' in self.query or 'decrease volume' in self.query:
                pyautogui.press("volumedown")

            elif 'mute' in self.query or 'quiet' in self.query:
                pyautogui.press("volumemute")

            elif 'ip address' in self.query:
                ip = get('https://api.ipify.org').text
                speak(f"Your IP address is {ip}")

            elif 'restart system' in self.query:
                speak("restarting")
                os.system("shutdown /r /t s")

            elif 'shut down system' in self.query:
                speak("sir, Do you really want to shut down the system")
                if'yes' in self.query:
                    speak("shutting down")
                    os.system("shutdown /s /t s")
                else:
                    os.abort

        # application
            elif 'open notepad' in self.query:
                npath = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(npath)
                speak("opening notepad")
            
            elif 'close notepad' in self.query:
                speak("closing notepad")
                os.system('taskkill /f /im notepad.exe')

            elif 'open chrome' in self.query:
                chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(chromePath)
                speak("opening chrome")

            elif 'close chrome' in self.query:
                speak("closing chrome")
                os.system('taskkill /f /im chrome.exe')

            elif 'open zoom' in self.query:
                zoomPath = "C:\\Users\\user\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
                os.startfile(zoomPath)
                speak("opening zoom")
            
            elif 'close zoom' in self.query:
                speak("closing zoom")
                os.system('taskkill /f /im Zoom.exe')

            elif 'open code' in self.query:
                codePath = "D:\\Lucky Self\\Coding\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
                speak("opening code")

            elif 'close code' in self.query:
                speak("closing code")
                os.system('taskkill /f /im Code.exe')

            elif 'open telegram' in self.query:
                telePath = "D:\\Lucky Self\\Telegram Desktop\\Telegram.exe"
                os.startfile(telePath)
                speak("opening telegram")

            elif 'close telegram' in self.query:
                speak("closing telegram")
                os.system('taskkill /f /im Telegram.exe')

            elif 'open droidcam' in self.query:
                camPath = "D:\\Lucky Self\\Droidcam\\DroidCamApp.exe"
                os.startfile(camPath)
                speak("opening droidcam")

            elif 'close droidcam' in self.query:
                speak("closing droidcam")
                os.system('taskkill /f /im DroidCamApp.exe')

            elif 'open quick heal' in self.query:
                healPath = "C:\\Program Files\\Quick Heal\\Quick Heal Total Security\\SCANNER.EXE"
                os.startfile(healPath)
                speak("opening quick heal")

            elif 'open word' in self.query:
                wpath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
                os.startfile(wpath)
                speak("opening word")
            
            elif 'close word' in self.query:
                speak("closing word")
                os.system('taskkill /f /im WINWORD.EXE')

            elif 'open powerpoint' in self.query:
                ppath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
                os.startfile(ppath)
                speak("opening powerpoint")
            
            elif 'close powerpoint' in self.query:
                speak("closing powerpoint")
                os.system('taskkill /f /im POWERPNT.EXE')

            elif 'open excel' in self.query:
                epath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
                os.startfile(epath)
                speak("opening excel")
            
            elif 'close excel' in self.query:
                speak("closing excel")
                os.system('taskkill /f /im EXCEL.EXE')

            elif 'open access' in self.query:
                apath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\MSACCESS.EXE"
                os.startfile(apath)
                speak("opening access")
            
            elif 'close access' in self.query:
                speak("closing access")
                os.system('taskkill /f /im MSACCESS.EXE')

            elif 'open onenote' in self.query:
                opath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.EXE"
                os.startfile(opath)
                speak("opening onenote")
            
            elif 'close onenote' in self.query:
                speak("closing onenote")
                os.system('taskkill /f /im ONENOTE.EXE')

            elif 'open outlook' in self.query:
                lpath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE"
                os.startfile(lpath)
                speak("opening outlook")
            
            elif 'close outlook' in self.query:
                speak("closing outlook")
                os.system('taskkill /f /im OUTLOOK.EXE')

            elif 'open cmd' in self.query:
                os.system("start cmd")
                speak("starting command prompt") 

            elif 'close cmd' in self.query:
                speak("closing cmd")
                os.system('taskkill /f /im cmd.exe')

        # folders
            elif 'open lucky self' in self.query:
                luckyselfPath = "D:\\Lucky Self"
                os.startfile(luckyselfPath)

            elif 'open lucky' in self.query:
                luckyPath = "E:\\Lucky"
                os.startfile(luckyPath)

            elif 'open coding' in self.query:
                codingPath = "D:\\Lucky Self\\Coding"
                os.startfile(codingPath)

        # internet
            elif 'open google' in self.query:
                webbrowser.open("www.google.com")

            elif 'open youtube' in self.query:
                webbrowser.open("www.youtube.com")

            elif 'open facebook' in self.query:
                webbrowser.open("www.facebook.com")

            elif 'open instagram' in self.query:
                webbrowser.open("www.instagram.com")

            elif 'profile on instagram' in self.query:
                speak("Sir please enter the username.")
                name = input("Enter the username here: ")
                webbrowser.open(f"www.instagram.com/{name}")
                speak(f"Sir here is the profile of the user {name}")
                time.sleep(5)

            elif 'search on google' in self.query:
                speak("Sir, What should I search on google")
                cm = self.takecommand().lower()
                webbrowser.open(f"{cm}")

            elif "wikipedia" in self.query:
                speak("Searching wikipedia...")
                self.query = self.query.replace("wikipedia","")
                results = wikipedia.summary(self.query, sentences=2)
                speak("According to wikipedia")
                speak(results)

            elif 'enable how to mode' in self.query or 'how to mod' in self.query:
                speak("enabled")
                while True:
                    speak("what do you want to know")
                    how = self.takecommand()
                    try:
                        if 'exit' in how or 'close' in how:
                            speak("closing how to mode")
                            break
                        else:
                            max_results = 1
                            how_to = search_wikihow(how, max_results)
                            assert len(how_to) == 1
                            how_to[0].print()
                            speak(how_to[0].summary)
                    except Exception as e:
                        speak("sorry sir I am not able to find it")

            elif 'internet speed' in self.query:
                import speedtest
                st = speedtest.Speedtest()
                dl = st.download()
                up = st.upload()
                speak("wait")
                speak(f"sir, downloading speed is {dl} bit per second and uploding is {up} bit per second") 

            elif 'news' in self.query:
                speak("please wait sir, fetching the latest news")
                news()

            elif 'where am i' in self.query or 'where are we' in self.query:
                speak("wait sir, let me check")
                try:
                    ipAdd = requests.get('https://api.ipfy.org').text
                    print(ipAdd)
                    url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    city = geo_data['City']
                    country = geo_data['Country']
                    speak(f"sir I am not sure, but I think we are in {city} city in {country}")
                except Exception as e:
                    speak("Sorry sir, I am not able to access the location")
                    pass

            elif 'temperature' in self.query:
                search = "temperature in jaipur"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div",class_="BNeawe").text
                speak(f"current {search} is {temp}")

        # outer applications
            elif 'open camera' in self.query: # press ESC to exit
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k==27:
                        break;
                cap.release()
                cv2.destroyAllWindows()

            elif 'read pdf' in self.query:
                pdf_reader()

            elif 'joke' in self.query:
                joke = pyjokes.get_joke()
                speak(joke)

# GUI
startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_JarvisGUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("C:/Users/user/Downloads/armour.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()   # according to amount of gifs
        self.ui.movie = QtGui.QMovie("C:/Users/user/Downloads/Initialise.gif")
        self.ui.label_8.setMovie(self.ui.movie)  # check please label
        self.ui.movie.start()   # according to amount of gifs
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser_4.setText(label_date)
        self.ui.textBrowser_3.setText(label_time)


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())