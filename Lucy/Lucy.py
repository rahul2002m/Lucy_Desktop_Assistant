import musix
import speech_recognition as sr
import pyttsx3
import pyautogui
import screen_brightness_control as sb
import psutil
import cv2
import Face_recognition
import pywhatkit
import webbrowser as web
from pytube import *
from pyautogui import *
import pyperclip
import wolframalpha
from keyboard import press_and_release
import speedtest
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import geocoder
import requests
import pyjokes
import randfacts
from time import *
import winsound
from tkinter import *


engine = pyttsx3.init()
en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice', en_voice_id)
client = wolframalpha.Client(" ") #Enter your API key of wolframalpha


def speak(audio):
    print(f"{audio}")
    engine.say(audio)
    engine.runAndWait()


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language='en-in')
            print(f"Your command is {query} ")
        except:
            return ""

    return query.lower()


MASTER = "Rahul sir"


def wishme():
    press('esc')
    speak("User Authentication Successful")
    hr = int(datetime.datetime.now().hour)
    if 0 <= hr < 12:
        speak("Good Morning " + MASTER)
    elif 12 <= hr < 16:
        speak("Good Afternoon " + MASTER)
    elif hr >= 16:
        speak("Good Evening " + MASTER)
    speak("How May I Help You...")


def exe():
    while True:
        query = listen()
        if "hello" in query:
            speak("Hello sir")

        elif "how are you" in query:
            speak("I'm fine sir. What about you?")

        elif "fine" in query:
            speak("Good to hear that sir")

        elif "do you love me" in query:
            speak("Yes sir, Ofcourse. I Love you so much")

        elif "love you" in query:
            speak("I Love you too")

        elif "what are you doing" in query:
            speak("Nothing sir, Just setting up functions for you")

        elif "need a break" in query or "sleep" in query:
            speak("Ok sir, I'm going to sleep mode")
            speak("If you need any help, just say hey Lucy")
            exit()

        elif "volume" in query:
            vol(query)

        elif "brightness" in query:
            brightness(query)

        elif "battery" in query:
            battery()

        elif "current location" in query:
            cl()

        elif "photo" in query or "picture" in query:
            photo()

        elif "shutdown" in query:
            shut()

        elif "restart" in query:
            res()

        elif "capture video" in query:
            video()

        elif "search on youtube" in query:
            query = query.replace("search", "")
            query = query.replace("on youtube", "")
            speak(f"Searching {query} on youtube")
            youtube(query)

        elif "download this video" in query:
            speak("Your video is being downloaded sir...")
            ytd()

        elif "google search" in query:
            query = query.replace("google search", "")
            google(query)

        elif "music" in query or "song" in query:
            musix.music()

        elif "what time is it" in query or "what is the time" in query:
            p = strftime("%H")
            r = strftime("%M")
            speak("Current time is " + p + " hours " + r + " minutes")

        elif "day" in query:
            now = datetime.datetime.today().strftime("%A")
            speak("Today is " + now)

        elif "date" in query:
            g = datetime.datetime.today().strftime("%d")
            e = datetime.datetime.today().strftime("%m")
            t = datetime.datetime.today().strftime("%Y")
            speak("Today's date is " + g + " " + e + " " + t)

        elif "month" in query:
            e = datetime.datetime.today().strftime("%m")
            speak(f"{e}")

        elif "which year" in query:
            t = datetime.datetime.today().strftime("%Y")
            speak(f"{t}")

        elif "locate" in query or "navigate" in query:
            query = query.replace("locate ", "")
            query = query.replace("navigate ", "")
            speak(f"Locating {query} on maps")
            googlemaps(query)

        elif 'temperature' in query:
            term = str(query)
            term = term.replace("ok ", "")
            term = term.replace("lucy ", "")
            term = term.replace("in ", "")
            term = term.replace("what is the ", "")
            term = term.replace("temperature ", "")
            tempquery = str(term)
            if "outside" in tempquery:
                var = "Temperature in Delhi"
                a = wolfram(var)
                speak(f"{var} is {a} .")
            else:
                var1 = "Temperature in " + tempquery
                ans = wolfram(var1)
                speak(f"{var1} is {ans} .")


        elif "chrome mode" in query:
            chromemode()

        elif "speed" in query:
            speedTest(query)

        elif "remember this" or "note" in query:
            remember(query)

        elif "remind me" in query:
            rem()

        elif "education mode" in query:
            edu()

        elif "youtube mode" in query:
            yta()

        elif "whatsapp" in query:
            whatsapp()

        elif "instagram" in query:
            insta()

        elif "news" in query:
            news()

        elif 'joke' in query:
            jokes()

        elif 'fact' in query:
            facts()

        elif "d drive" in query:
            speak("Opening D drive")
            os.startfile("D:\\")

        elif "e drive" in query:
            speak("Opening e drive")
            os.startfile("E:\\")

        elif "c drive" in query:
            speak("Opening c drive")
            os.startfile("C:\\")

        elif "f drive" in query:
            speak("Opening f drive")
            os.startfile("F:\\")

        elif "alarm" in query:
            speak("please tell me the time to set alarm")
            tt = listen()
            tt = tt.replace("set alarm to", "")
            tt = tt.replace(".", "")
            tt = tt.upper()
            alarm(tt)

        elif "screenshot" in query:
            speak("Capturing ScreenShot")
            screenshot()

        else:
            speak("Unable to get it sir, please try with pre-defined commands")


def vol(query):
    if "volume up" in query:
        pyautogui.press("volumeup")
        speak("Your volume is increased")

    elif "volume down" in query:
        pyautogui.press("volumedown")
        speak("Your volume is decreased")

    elif "mute volume" in query:
        pyautogui.press("volumemute")
        speak("Your volume is muted")


def brightness(query):
    if "brightness to hai" in query:
        sb.set_brightness(100)
        speak("Your brightness is set to high")

    elif "brightness to low" in query:
        sb.set_brightness('-100')
        speak("Your brightness is set to low")

    elif "brightness to medium" in query:
        sb.set_brightness(50)
        speak("Your brightness is set to medium")


def battery():
    battery = psutil.sensors_battery()
    speak(f"Your battery percent is {battery.percent}")

    if battery.power_plugged:
        speak("Your PC is plugged in")

    else:
        speak("Your PC is unplugged")

    convert(battery.secsleft)


def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    speak(f"Your pc will function upto {hour} hour {minutes} minutes")


def photo():
    speak("say cheese")
    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    for i in range(3):
        sleep(1)
        return_value, image = camera.read()
        cv2.imwrite('photos/opencv' + str(i) + '.png', image)
    del camera


def video():
    speak("Get ready , the video will start in a second")
    vid_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    vid_cod = cv2.VideoWriter_fourcc(*'XVID')
    output = cv2.VideoWriter("videos//cam_video.mp4", vid_cod, 20.0, (640, 480))
    speak("press, 'g', to stop your video")
    while True:
        ret, frame = vid_capture.read()
        cv2.imshow("My cam video", frame)
        output.write(frame)
        if cv2.waitKey(1) & 0XFF == ord('g'):
            break

    vid_capture.release()
    output.release()
    cv2.destroyAllWindows()


def shut():
    speak("Your System will shutdown in 5 seconds")
    os.system("shutdown /s /t 5")


def res():
    speak("Your System will restart in 5 seconds")
    os.system("shutdown /r /t 5")


def youtube(query):
    result = "https://www.youtube.com/results?search_query=" + query
    web.open(result)
    speak("This is what i found for your search .")
    pywhatkit.playonyt(query)
    speak("This may also help you.")


def ytd():
    sleep(5)
    try:
        click(x=942, y=59)
        # click(x=1250, y=75)
        hotkey('ctrl', 'a')
        hotkey('ctrl', 'c')
        link = pyperclip.paste()
        Link = str(link)
        YouTube(Link).streams.first().download('videos\\')
        speak("Your video has been downloaded and saved to videos folder")
    except:
        return ""


def google(query):
    speak(f"Searching {query} on google")
    pywhatkit.search(query)


def maps(query):
    location = query.replace("where is", "")
    speak("Hold on Sir, I will show you where " + location + " is.")
    web.open("https://www.google.nl/maps/place/" + location + "/&amp;")


def wolfram(query):
    api_key = "" #Enter your API key of wolframalpha
    requester = wolframalpha.Client(api_key)
    requested = requester.query(query)
    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("A string value is not answerable")


def chromemode():
    speak("Chrome mode activated")
    web.open(url='https://www.google.com')
    speak("Tell your command sir")
    while True:
        try:
            com = listen()
            print(com)
            com = com.lower()
            if "incognito tab" in com:
                press_and_release('ctrl + shift + n')
            elif "new tab" in com:
                press_and_release('ctrl + t')
            elif "new window" in com:
                press_and_release('ctrl + n')
            elif "switch tab" in com:
                press_and_release('ctrl + tab')
            elif "download" in com:
                press_and_release('ctrl + j')
            elif "history" in com:
                press_and_release('ctrl + h')
            elif "close tab" in com:
                press_and_release('ctrl + w')
            elif "reopen closed tab" in com:
                press_and_release('ctrl + shift + t')
            elif "reload" in com:
                press_and_release('ctrl + r')
            elif "back" in com:
                press_and_release('alt + left')
            elif "next" in com:
                press_and_release('alt + right')
            elif "close window" in com:
                press_and_release('alt + f4')
            elif "bookmark" in com:
                press_and_release('ctrl + shift + o')
            elif "clear browsing data" in com:
                press_and_release('ctrl + shift + delete')
            elif "search" in com:
                speak("what to search ?")
                com = listen()
                google(com)
            elif "source code" in com:
                press_and_release('ctrl + u')
            elif "add to bookmark" in com:
                press_and_release('ctrl + d')
            elif "scroll down" in com:
                press_and_release('space')
            elif "scroll up" in com:
                press_and_release('shift + space')
            elif "exit chrome mode" in com:
                press_and_release('alt + f4')
                speak("Chrome mode exited")
                break
        except:
            continue


def speedTest(query):
    speak("Checking Your internet speed....")
    speed = speedtest.Speedtest()
    downloading = speed.download()
    cd = int(downloading / 800000)
    uploading = speed.upload()
    cu = int(uploading / 800000)
    if 'uploading' in query:
        speak(f"Uploading speed is {cu} mbps")
    elif 'downloading' in query:
        speak(f"Downloading speed is {cd} mbps")
    else:
        speak(f"Uploading speed is {cu} mbps and Downloading speed is {cd} mbps")


def remember(rmsg):
    rmsg = rmsg.replace("remember this", "")
    rmsg = rmsg.replace("lucy ", "")
    remember = open('notes/remember.txt', 'w+')
    remember.write(rmsg)
    remember.close()
    speak("ok, i remember this. ask me to remind you whenever you want .")


def rem():
    reme = open("data.txt", "r")
    speak("You told me to remind you this message" + reme.read())


def edu():
    speak("Education mode activated!!")
    while True:
        sleep(2)
        speak("ask your question sir..")
        abc = listen()

        if "exit education mode" in abc:
            speak("Education mode exited")
            break

        abc = abc.replace("plus", "+")
        abc = abc.replace("minus", "-")
        abc = abc.replace("power", "^")
        abc = abc.replace("by", "/")
        abc = abc.replace("into", "*")

        try:
            wolfram_res = next(client.query(abc).results).text
            speak(wolfram_res)

        except:
            speak("No data available")

        engine.runAndWait()


def googlemaps(place):
    url_place = "https://www.google.com/maps/place/" + str(place)
    geolocator = Nominatim(user_agent="myGeocoder")
    location = geolocator.geocode(place, addressdetails=True)
    target_loc = location.latitude, location.longitude
    location = location.raw['address']
    target = {'city': location.get('city', ''), 'state': location.get('state', ''),
              'country': location.get('country', '')}
    current_loc = geocoder.ip('me')
    current_latlon = current_loc.latlng
    distance = str(great_circle(current_latlon, target_loc))
    distance = str(distance.split(' ', 1)[0])
    distance = round(float(distance), 2)
    web.open(url=url_place)
    speak(target)
    speak(f"{place} is {distance} kilometer away from your location .")


def whatsapp():
    os.startfile("") #enter your whatsapp location and make sure that you scan qrcode befor running the script
    sleep(10)
    speak("Tell the contact name")
    name = listen()
    pyautogui.click(x=124, y=166)
    pyautogui.doubleClick()
    press('delete')
    pyautogui.typewrite(name)
    sleep(1)
    pyautogui.click(x=345, y=391)
    speak("What do you want to do sir")
    speak("Do you want me to send message, or call, or video call")
    task = listen()
    try:
        if "message" in task:
            pos = pyautogui.locateOnScreen("src/emojiB.png", confidence=.6)
            x = pos[0]
            y = pos[1]
            pyautogui.moveTo(x + 200, y + 20, duration=.5)
            pyautogui.click()
            speak("Tell your message sir")
            message = listen()
            pyautogui.typewrite(message, interval=.01)
            pyautogui.typewrite("\n", interval=.01)

        elif "video" in task:
            pos = pyautogui.locateOnScreen("src/video.png", confidence=.6)
            x = pos[0]
            y = pos[1]
            pyautogui.moveTo(x, y, duration=.5)
            pyautogui.click()

        elif "call" in task:
            pos = pyautogui.locateOnScreen("src/call.png", confidence=.9)
            x = pos[0]
            y = pos[1]
            pyautogui.moveTo(x, y, duration=.5)
            pyautogui.click()

    except:
        pass


def yta():
    speak("Youtube mode activated")
    web.open(url='https://www.youtube.com/')
    speak("Tell your command sir")
    while True:
        try:
            com = listen()
            print(com)
            com = com.lower()
            if "pause" in com:
                press_and_release('space bar')
            elif "play" in com:
                press_and_release('space bar')
            elif "full screen" in com:
                press_and_release('f')
            elif "exit full screen" in com:
                press_and_release('esc')
            elif "theatre mode" in com:
                press_and_release('t')
            elif "fast forward" in com:
                press_and_release('l')
            elif "back forward" in com:
                press_and_release('j')
            elif "increase speed" in com:
                press('>')
            elif "decrease speed" in com:
                press('<')
            elif "reload" in com:
                press_and_release('ctrl + r')
            elif "previous" in com:
                press_and_release('shift + p')
            elif "next" in com:
                press_and_release('shift + n')
            elif "close youtube" in com:
                press_and_release('alt + f4')
            elif "download" in com:
                ytd()
            elif "history" in com:
                web.open("https://www.youtube.com/feed/history")
            elif "search" in com:
                speak("what do you want to search for ?")
                query = listen()
                result = "https://www.youtube.com/results?search_query=" + query
                web.open(result)
                speak("This is what i found for your search .")
                speak("This may help you.")
            elif "open youtube" in com:
                web.open(url='https://www.youtube.com/')
            elif "exit youtube mode" in com:
                press_and_release('alt + f4')
                break

        except:
            continue


def insta():
    web.open('https://www.instagram.com')


def news():
    apikey = "4ad432c899d345f6b946ed73db668cbd"
    mainurl = "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=4ad432c899d345f6b946ed73db668cbd"
    news = requests.get(mainurl).json()
    article = news['articles']
    newsarticle = []
    for arti in article:
        newsarticle.append(arti['title'])

    for i in range(10):
        speak(newsarticle[i])
        engine.runAndWait()


def jokes():
    speak(pyjokes.get_joke())


def facts():
    speak(randfacts.getFact())


def alarm(timing):
    altime = str(datetime.datetime.now().strptime(timing, "%I:%M %p"))
    altime = altime[11:-3]
    h = altime[:2]
    h = int(h)
    m = altime[3:5]
    m = int(m)
    speak(f"Done sir, alarm set at {timing}")
    while True:

        if h == datetime.datetime.now().hour:
            if m == datetime.datetime.now().minute:
                print("Alarm is running")
                winsound.PlaySound('abc', winsound.SND_LOOP)

            elif m < datetime.datetime.now().minute:
                break


def screenshot():
    try:
        myScreenshot = pyautogui.screenshot()
        x = str(datetime.datetime.now())
        myScreenshot.save('photos/ss_'+x+'.png')
        speak("screenshot is taken and saved to photos in Lucy folder .")
    except:
        pass


def wifi():
    os.system('cmd /c "netsh wlan show networks"')
    name_of_router = input('Enter Name/SSID of the Wifi Network you wish to connect to: ')
    os.system(f'''cmd /c "netsh wlan connect name={name_of_router}"''')
    speak("If you're not yet connected, try connecting to a previously connected SSID again!")


def cl():
    r=requests.get('https://get.geojs.io./')
    ipreq=requests.get('https://get.geojs.io/v1/ip.json')
    ipadd=ipreq.json()['ip']

    url='https://get.geojs.io/v1/ip/geo/'+ipadd+'.json'
    georeq=requests.get(url)
    geodata=georeq.json()

    speak(f"Latitude : {geodata['latitude']}")
    speak(f"Longitude : {geodata['longitude']}")
    speak(f"City : {geodata['city']}")
    speak(f"Region : {geodata['region']}")
    speak(f"Country : {geodata['country']}")
    speak(f"Timezone : {geodata['timezone']}")


def ert():
    r = requests.get('https://get.geojs.io./')
    ipreq = requests.get('https://get.geojs.io/v1/ip.json')
    ipadd = ipreq.json()['ip']

    url = 'https://get.geojs.io/v1/ip/geo/' + ipadd + '.json'
    georeq = requests.get(url)
    geodata = georeq.json()
    return geodata['country']


def security():
    speak("Recognizing and Verifying face...Please wait...")

    if Face_recognition.facerec():
        wishme()
        exe()

    else:
        speak("Face recognition failed")
        speak("Enter correct password to get access")
        try:
            def check():
                if pwd.get() == "rahul":
                    speak("Access granted!")
                    win.destroy()
                    wishme()
                    exe()
                else:
                    speak("Incorrect password... Terminating Program...")
                    win.destroy()
                    exit()

            win = Tk()
            win.title('Verification')
            win.geometry("800x400")
            win.config(background="black")
            pwd = StringVar()
            msg = Label(text="Enter Password :", font=('Comic Sans MS', 16, "bold"), background="black", fg='White')
            msg.place(x=100, y=100)
            entry = Entry(win, textvariable=pwd, font=15, bd='3')
            entry.place(x=400, y=110)
            set = Button(text="Submit", command=check, font=('Comic Sans MS', 13), bg='#567', fg='White')
            set.place(x=330, y=200)
            win.mainloop()

        except:
            print()


