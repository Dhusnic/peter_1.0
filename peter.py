#imports
import speech_recognition as sr
import pyttsx3
import os
from datetime import datetime
import wikipedia
import webbrowser
from colorama import Fore
import time
import wikipedia.exceptions
import pywhatkit
import wolframalpha
r=sr.Recognizer()
def ear():
    r=sr.Recognizer()
    with sr.Microphone() as source2:
                            r.adjust_for_ambient_noise(source2,duration=0.2)
                            r.pause_threshold=1
                            audio2=r.listen(source2)
                            try:
                                mytext=r.recognize_google(audio2)
                                (mytext)=mytext.lower()
                                print(Fore.LIGHTBLUE_EX+mytext)
                            except  sr.RequestError as e :
                                print("could not request results;{0}".format(e))
                            except sr.UnknownValueError:
                                print(Fore.BLUE+"cant understand please tell again ")
                                tell("cant understand please tell again")

#function to pause a program     
def pause():
    print(Fore.LIGHTRED_EX+"alright,wake me up when you want my help,by pressing enter")
    tell("alright,wake me up when you want my help , by pressinng enter")
    os.system('pause')

#function to make program speak
def tell(text):
    engine=pyttsx3.init('sapi5')
    engine.say(text)
    engine.runAndWait()
    engine.setProperty('rate',100)
    engine.setProperty('volume',1.0)
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
#function make a wish
def wishme():
    hr=datetime.now().hour
    if hr>=0 and hr<12:
        tell("Hello Dhusnic,i am peter,Good Morning,what can i do for you ")
        print("Hello Dhusnic,i am peter,Good Morning,what can i do for you ")
    if hr>=12 and hr<18:
        tell("Hello Dhusnic,i am peter,Good Afternoon,what can i do for you  ")
        print("Hello Dhusnic,i am peter,Good Afternoon,what can i do for you")
    if hr>18:
        tell("Hello Dhusnic,i am peter,Good evening,what can i do for you  ")
        print("Hello Dhusnic,i am peter,Good evening,what can i do for you ")
try:
    #loop of inactive a ai
    while True:
        try: 
            with sr.Microphone() as source2:
                r=sr.Recognizer()
                r.adjust_for_ambient_noise(source2,duration=0.3)
                r.pause_threshold=1
                audio2=r.listen(source2)
                mytext=r.recognize_google(audio2)
                mytext=mytext.lower()
                print(mytext)
                #loop of an active ai
                if "peter" in mytext or "listen" in mytext or "pete" in mytext:
                    os.system('cls')
                    print(Fore.LIGHTBLUE_EX + "listening.........")
                    wishme()
                    print(Fore.LIGHTGREEN_EX+"Hi dhusnic ," ,Fore.MAGENTA+" I am peter," ,Fore.YELLOW+ "What can i do for you")
                    #loop to have questions 
                    while True:
                        try:
                            with sr.Microphone() as source2:
                                r.adjust_for_ambient_noise(source2,duration=0.2)
                                r.pause_threshold=1
                                audio2=r.listen(source2)
                                mytext=r.recognize_google(audio2)
                                (mytext)=mytext.lower()
                                print(Fore.LIGHTBLUE_EX+mytext)
                                #call peter
                                if "peter" in mytext:
                                        wishme()


                                #tell date
                                if "date" in mytext:
                                        dt=datetime.today().strftime("%d-%b-%Y")
                                        print(Fore.YELLOW +"Todays Date is"+ dt)
                                        tell("Todays Date  is   "+dt)


                                #tell time
                                if "time" in mytext :
                                    ct=datetime.today().strftime("%I:%M %p")
                                    print(Fore.MAGENTA+"The time now is   "+ ct )
                                    tell("The time now is   "+ ct)


                                #make a program sleep
                                if "sleep" in mytext or "bye"in mytext or "leave" in mytext:
                                        print(Fore.LIGHTRED_EX+"ok bye ,see you later")
                                        tell("ok bye ,see you later")
                                        break


                                #clear the screen
                                if "clear" in mytext:
                                        os.system('cls')


                                #search in wikipedia
                                if "wikipedia" in mytext:
                                    try:
                                        tell("searching in wikipedia")
                                        mytext=mytext.replace("wikipedia search"or "wikipedia","")
                                        results=wikipedia.summary(mytext,sentences=3)
                                        print(Fore.LIGHTRED_EX+results)
                                        tell(results)
                                    except wikipedia.exceptions.PageError as e:
                                        print("try it in another way")
                                        tell("try it in another way")
                                    except wikipedia.exceptions.DisambiguationError as e:
                                        print("try it in another way")
                                        tell("try it in another way")



                                #open a youtube tab
                                if 'open youtube' in mytext:
                                    webbrowser.open_new_tab("https://www.youtube.com")
                                    tell("youtube is open now")
                                    print(Fore.RED+"youtube is open now")
                                    time.sleep(5)


                                #open a google tab
                                if 'open google' in mytext:
                                    webbrowser.open_new_tab("https://www.google.com")
                                    print(Fore.LIGHTGREEN_EX+"Google chrome is open now")
                                    tell("Google chrome is open now")
                                    time.sleep(5)


                                #open a gmail 
                                if 'open gmail' in mytext:
                                    webbrowser.open_new_tab("https://mail.google.com/mail/u/1/#inbox")
                                    tell("Google Mail open now")
                                    print(Fore.MAGENTA+"Google Mail open now")
                                    time.sleep(5)


                                #open my youtube channel
                                if ' my youtube channel' in mytext or "just belive"in mytext or "my yt channel"in mytext:
                                    webbrowser.open_new_tab("https://www.youtube.com/channel/UC2r-qtZPbbBJri1EXlQ2Q0g")
                                    tell("your youtube channel is  open now")
                                    print(Fore.BLUE+"your youtube channel is  open now")
                                    time.sleep(5)


                                #open my instagram
                                if ' instagram' in mytext  :
                                    webbrowser.open_new_tab("https://www.instagram.com/")
                                    tell("your Instagram is  open now")
                                    print(Fore.BLUE+"your Instagram is  open now")
                                    time.sleep(5)
                                    
                                    
                                #open my online class    
                                if ' online class'  in mytext or 'class'in mytext  :
                                    webbrowser.open_new_tab(" https://meet.google.com/exv-cmyj-oiv")
                                    tell("your google class is  open now")
                                    print(Fore.BLUE+"your google class is  open now")
                                    time.sleep(5)
                                    
                                    
                                #open my personal drive    
                                if ' personal drive' in mytext or 'my drive' in mytext  :
                                    webbrowser.open_new_tab("https://drive.google.com/drive/u/1/quota ")
                                    tell("your personal drive is  open now")
                                    print(Fore.BLUE+"your personal drive is  open now")
                                    time.sleep(5)
                                    
                                    
                                #open my study drive    
                                if ' study drive' in mytext or 'projects' in mytext  :
                                    webbrowser.open_new_tab("https://drive.google.com/drive/my-drive ")
                                    tell("your study drive is  open now")
                                    print(Fore.BLUE+"your study drive is  open now")
                                    time.sleep(5)

                                
                                #open my github
                                if ' github' in mytext or 'my github' in mytext  :
                                    webbrowser.open_new_tab("https://github.com/SpectralOps/keyscope?utm_term=github&utm_campaign=GitHub_Keyscope&utm_source=google&utm_medium=ppc&hsa_acc=1287660619&hsa_cam=14863556156&hsa_grp=127226304639&hsa_ad=550063928531&hsa_src=g&hsa_tgt=kwd-11648088761&hsa_kw=github&hsa_mt=e&hsa_net=adwords&hsa_ver=3&gclid=Cj0KCQjww4OMBhCUARIsAILndv4xt9yMfZKGWtoBLHWZODV-KMVNi_te9f3_CnArEY_ZTCYddCGhhIsaAgyREALw_wcB")
                                    tell("your study drive is  open now")
                                    print(Fore.BLUE+"your study drive is  open now")
                                    time.sleep(5)
                                
                                    
                                    
                                #open  study gmail      
                                if 'study gmail' in mytext or 'collage' and 'mail' in mytext:
                                    webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#inbox")
                                    tell("Google Mail of studies open now")
                                    print(Fore.MAGENTA+"Google Mail  of studies open now")
                                    time.sleep(5)
                                    
                                    
                                #open whatsapp    
                                if 'open whatsapp' in mytext:
                                    webbrowser.open_new_tab("https://web.whatsapp.com/")
                                    tell("whatsapp is open now")
                                    print(Fore.RED+"whatsapp is open now")
                                    time.sleep(5)
                                    
                                    
                                    
                                #pause a program
                                if "pause" in mytext or "wait" in mytext or "sleep"in mytext:
                                    
                                    
                                    pause()
                                
                                
                                #open  a browser
                                if "open browser" in mytext or "web browser" in mytext or "fire fox " in mytext:
                                    os.chdir('C:\Program Files (x86)\Mozilla Firefox ')
                                    os.system('firefox.exe')
                                    tell("your fire fox browser is opening")
                                    print(Fore.LIGHTRED_EX+"your fire fox browser is opening")
                                
                                
                                #paly videos in youtube  
                                if "play"in mytext and "youtube"in mytext:
                                    try:
                                        mytext=mytext.replace("play" and "youtube","")
                                        pywhatkit.playonyt(mytext)
                                        print(Fore.LIGHTRED_EX+" playing " ,mytext,"youtube")
                                        tell(" playing " + mytext + "youtube")
                                        pause()
                                    except:
                                        pass
                                
                                
                                #search and open tab in gooogle
                                if "search"in mytext and "google" in mytext and "show" in mytext:
                                    try:
                                        mytext=mytext.replace("google" ,"")
                                        mytext=mytext.replace("search" ,"")
                                        mytext=mytext.replace("searching","")
                                        mytext=mytext.replace("show","")
                                        mytext=mytext.replace("and","")

                                        pywhatkit.search(mytext)
                                        print(Fore.LIGHTRED_EX+" searching " ,mytext,"google")
                                        tell(" searching " + mytext + "google")
                                    except:
                                        pass
                                
                                
                                #search and tell in google
                                if "search"in mytext and "google" in mytext and "tell" in mytext:
                                    try:
                                        mytext=mytext.replace("google","")
                                        mytext=mytext.replace("search","")
                                        mytext=mytext.replace("searching","")
                                        mytext=mytext.replace("show","")
                                        mytext=mytext.replace("tell","")
                                        gt=pywhatkit.info(mytext,lines=3)
                                        tell(" searching " + mytext + "google")
                                        tell(pywhatkit.info(mytext,lines=3))
                                    except:
                                        pass
                                
                                
                                #to close a program
                                if "log out" in mytext:
                                    tell('ok ,i am shutting down')
                                    print(Fore.LIGHTGREEN_EX+'ok ,i am shutting down')
                                    exit()
                                
                                
                                # ask answer in wolf
                                if 'ask to wolf' in mytext:
                                    try:
                                        print(Fore.LIGHTRED_EX+'I can answer to you,what is the question')
                                        tell('I can answer to you,what is the question')
                                        ear()
                                        mytext=mytext.replace("ask to wolf","")
                                        app_id="4G8HAV-P2A7KT99GE "
                                        client = wolframalpha.Client('R2K75H-7ELALHR35X')
                                        res = client.query(mytext)
                                        answer = next(res.results).text
                                        tell(answer)
                                        print(answer)
                                    except:
                                        tell("try it in another way")
                                        pass
                                #restart a machine
                                if "restart yourself" in mytext:
                                    os.system('& python c:/Users/admin/Desktop/peter.py')
                                    exit()
                                else:
                                    print(Fore.LIGHTGREEN_EX+"I cant understand , please tell again")


                                
                        except  sr.RequestError as e :
                            print("could not request results;{0}".format(e))
                        except sr.UnknownValueError:
                            print(Fore.BLUE+"cant understand please tell again ")
                            tell("cant understand please tell again")
                
        except sr.RequestError as e:
            pass
        except sr.UnknownValueError:
            pass
except:
    pass
        
