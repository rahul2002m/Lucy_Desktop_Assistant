import threading
import speech_recognition as sr
import pyttsx3
import selenium
from sys import exit
from time import sleep
from selenium import common
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

engine = pyttsx3.init()
en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice', en_voice_id)


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


class YoutubeMusic(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self);
        self.FirstTime = True;
        self.existingProj = False;
        self.IncreaseTime = 30;
        self.DecreaseTime = 30;
        self.user_agent = '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1'
        self.options = Options();
        self.CompletelyLoaded = True;
        self.options.add_argument(self.user_agent);
        self.options.add_argument('--headless');
        self.options.add_argument('--disable-extensions')
        self.options.add_argument('--log-level=3')
        self.chromedriverPath = r"chromedriver.exe";  # change this with your actual chromedriver path.
        self.Browser = Chrome(self.chromedriverPath, options=self.options)


    def NavigateYoutube(self, MusicName):
        # !t Will Navigate On Youtube Website.
        self.MusicName = MusicName;
        self.CompletelyLoaded = False
        speak(f"Searching {self.MusicName} On Lucy Server . . . " );
        self.Browser.get("https://m.youtube.com/results?search_query=%s" % self.MusicName);
        self.Browser.implicitly_wait(5);

    def ListVideos(self):
        self.existingProj = True;
        self.Counter = 1;
        self.Videos = [];
        for eachVid in range(1, 7):
            self.xpath = '//*[@id="app"]/div[1]/ytm-search/ytm-section-list-renderer/lazy-list/ytm-item-section-renderer/lazy-list/ytm-compact-video-renderer[%d]/div/div/a/h4' % eachVid;
            self.EachVideo = WebDriverWait(self.Browser, 5).until(
                EC.presence_of_element_located((By.XPATH, self.xpath)))
            self.EachVideo = self.EachVideo.text;
            # self.EachVideo = self.Browser.find_element_by_xpath('/html/body/ytm-app/div[3]/ytm-search/ytm-section-list-renderer/lazy-list/ytm-item-section-renderer/lazy-list/ytm-compact-video-renderer[%d]/div/div/a/h4/span'%eachVid).text;
            self.Videos.append(self.EachVideo);
        for eachVid in self.Videos:
            print("[%d]: %s" % (self.Counter, eachVid));
            self.Counter += 1;
        speak("Select song from the list")

    def RefreshPage(self):
        # !In Case Of Error Refresh Can Be Done.
        self.CurrentPage = self.Browser.current_url;
        self.Browser.get(self.CurrentPage);
        print("Page Refreshed.")

    def PlayVideo(self, VideoID):
        # Finally Plays Video.
        # !VIDEO PLAY CODE HERE
        self.VideoPlay = '//*[@id="app"]/div[1]/ytm-search/ytm-section-list-renderer/lazy-list/ytm-item-section-renderer/lazy-list/ytm-compact-video-renderer[%d]/div/div/a/h4' % VideoID;
        self.Video = WebDriverWait(self.Browser, 5).until(EC.presence_of_element_located((By.XPATH, self.VideoPlay)));
        sleep(2)
        self.Video.click()

        self.VideoTitle = WebDriverWait(self.Browser, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'slim-video-metadata-title')));
        # self.VideoTitle = self.Browser.find_element_by_class_name('slim-video-metadata-title'); #!To Fetch Video Title.
        self.VideoTitle = self.VideoTitle.text;
        speak('[Playing %s Now... ]' % self.VideoTitle);
        self.CompletelyLoaded = True;
        self.RefreshPage();
        self.GetUrl = self.Browser.find_element_by_css_selector('video.video-stream.html5-main-video');
        # self.GetUrl = WebDriverWait(self.Browser,30).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'video.video-stream.html5-main-video')));
        self.GetUrl = self.GetUrl.get_attribute("currentSrc");
        self.Browser.get(self.GetUrl)

    def MoveForward(self):
        
        self.Browser.execute_script("document.getElementsByTagName('video')[0].currentTime += %s" % self.IncreaseTime)

    def MoveBackwards(self):
        
        self.Browser.execute_script("document.getElementsByTagName('video')[0].currentTime += %s" % self.DecreaseTime)

    def RestartVideo(self):
        
        self.CurrentVideoUrl = self.GetUrl;
        self.Browser.get(self.CurrentVideoUrl);
        pass

    def Pause(self):
        self.Browser.execute_script("document.getElementsByTagName('video')[0].pause()");
        pass

    def Play(self):
        self.Browser.execute_script("document.getElementsByTagName('video')[0].play()");
        pass

    def Close(self):
        self.Browser.close()
        return ""

    def ThreadStatus(self):
        print(threading.enumerate())

def music():
    x = YoutubeMusic()
    while True:
        try:
            if x.existingProj:

                contentchoice = listen()

                if contentchoice == "exit" or contentchoice == "close":
                    x.Pause()
                    speak("Music exited")
                    return ""

                elif contentchoice == "refresh":
                    speak("Music replayed")
                    x.RestartVideo()

                elif contentchoice == "resume" or contentchoice == "play":
                    x.Play()

                elif contentchoice == "pause":
                    speak("Music paused")
                    x.Pause()

                elif contentchoice == "search":
                    x.Pause()
                    x.existingProj = False
                    continue

                elif contentchoice == 0:
                    x.PlayVideo(1)

                else:
                    if contentchoice == '1':
                        contentchoice = 1
                    elif contentchoice == 'tu' or contentchoice == 'Tu':
                        contentchoice = 2
                    elif contentchoice == 'three' or contentchoice == '3':
                        contentchoice = 3
                    elif contentchoice == 'four' or contentchoice == '4':
                        contentchoice = 4
                    elif contentchoice == 'five' or contentchoice == '5':
                        contentchoice = 5
                    elif contentchoice == 'six' or contentchoice == '6':
                        contentchoice = 6
                    contentchoice = int(contentchoice)
                    x.NavigateYoutube(contentName)
                    x.PlayVideo(contentchoice)
            else:
                
                speak("Which song do you want to play")
                contentName = listen()

                if contentName:
                    try:
                        x.NavigateYoutube(contentName)
                        x.ListVideos()
                    except:
                        pass

        except ValueError:
            pass


        except common.exceptions.ElementClickInterceptedException:
            print("Unknown Error - Please Try Again.")
            return ""

        except common.exceptions.WebDriverException:
            print("Error while using Chrome Driver (Possible Causes ) : ")
            print("1. Using Old Chrome Driver, Please Get Latest Version.")
            print("2. Incorrect Path of Chrome Driver Provided, Please Correct It.")
            return ""

