import tkinter,time
from tkinter import Label ,Button

# -----------------------------------------------------------------------------------------------------------------------------------

def engine():

    import pyttsx3 , datetime 
    import speech_recognition as sr
    import wikipedia , webbrowser ,os
    import time
    import pyautogui

    def speak(var):
    
        tts = pyttsx3.init()
        tts.say(var)
        tts.runAndWait()
    
    def wish():
    
        time_ = datetime.datetime.now().hour
    
        if ( time_ >= 0 and time_ < 12 ):
            speak("Good Morning Rohith Vishnu")
        
        if( time_ >= 12 and time_ < 16 ):
            speak("Good Afternoon Rohith Vishnu")
        
        if( time_ >= 16 and time_ <= 24):
            speak("Good Evening Rohith Vishnu")
        
        speak("How can I help you")
 
    wish()

    def sprec():
    
        rec = sr.Recognizer()
        rec.pause_threshold = 1
        with sr.Microphone() as roh:
        
            print("Listening......")
            var1 = Label( root, text = "Listening......")
            var1.config(background= "orange",font= ("Franklin Gothic Demi" , 25))
            var1.after(3000, lambda : var1.destroy())
            var1.pack(pady = 10)
            aud = rec.listen(roh)
       
        try :
            print("Recognizing......")
            var2 = Label( root, text = "recognizing")
            var2.config(background= "orange",font= ("Franklin Gothic Demi" , 25))
            var2.after(2000, lambda : var2.destroy())
            var2.pack(pady = 10)
            query =rec.recognize_google(aud)
            query = query.lower()
            
            var3 = Label( root, text = query)
            var3.config(background= "orange",font= ("Franklin Gothic Demi" , 25))
            var3.after(5000, lambda : var3.destroy())
            var3.pack(pady = 10 )
            print(query)
            return query
        
        except:
            var4 = Label( root, text = "Sorry I didnt get that")
            var4.config(background= "orange",font= ("Franklin Gothic Demi" , 25))
            var4.after(5000, lambda : var4.destroy())
            var4.pack(pady = 10)
            print("Sorry I didnt get that")
            speak("Sorry I didnt get that")
        
    global_query = sprec()  
 
    
    if ( "wikipedia" in global_query ):
    
        print("Searching on Wikipedia.....")
        speak("Searching on Wikipedia.....")
    
        global_query = global_query.replace("wikipedia" , "")
    
        output = wikipedia.summary(global_query , sentences =2 )
        print(output)
        speak("According to Wikipedia")
        speak(output)
    
    
    elif("open" in global_query):
    
        global_query = global_query.replace("open" , "")
        speak(f"Opening {global_query}") 
        text = "www."+global_query+".com"
        text = text.replace(" ", "")
        webbrowser.open(text)
    
    elif( "the time" in global_query):
        hour = datetime.datetime.now().hour
        min = datetime.datetime.now().minute
    
        print(hour , min)
        speak('its')
        speak(hour)
        speak(min)

     
   
    elif( "play music on spotify" in global_query ):
    
        webbrowser.open_new("https://open.spotify.com/?")
    
    

    elif("play music" in global_query or 'play songs' in global_query):
    
        songs = os.listdir("C:\\Users\\USER\\Music")
        print(songs)
    
    
        os.startfile(os.path.join("C:\\Users\\USER\\Music" , songs[1]))    
    
    
    elif("launch vs code" in global_query or "launch visual studio code" in global_query ):
    
        speak("opening VS code")
        os.startfile("C:\\Users\\USER\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
    
    
    elif( "launch calculator" in global_query ):
    
        speak("opening Calculator")    
        os.startfile('calc.exe')
    
    elif("google" in global_query ):
    
        txt = str(global_query)
        txt = txt.replace("google", "")
        txt = txt.strip()
        print(txt)
        webbrowser.open(txt)

    elif( "launch notepad" in global_query ):
    
        speak("opening notepad")    
        os.startfile('notepad.exe')
    
        speak("Do you want to type anything my assistant")
    
        asd  = sprec()
        if(asd == "yes" or asd == "sure" ):
        
            pyautogui.hotkey('win' , 'h')
        
        else:
            speak("ok")
        
        
    elif("launch settings" in global_query):
    
        pyautogui.hotkey('win', 'i')
        
    elif("launch explorer" in global_query or "launch my computer" in global_query or "launch thic pc" in global_query):
    
        pyautogui.hotkey('win', 'e')
        
        
    elif("launch task manager" in global_query):
    
        pyautogui.hotkey('ctrl', 'shift', 'escape')
        
        
    elif("who are you" in global_query or "what can you do" in global_query): 
        speak("I am your virtual assistant")
        speak("I can open apps , google some info ,open noptepad and type what you dictate, or i can play some music , get info from wikipedia")
        speak("I am developed by rohith vishnu")


    elif("shutdown" in global_query):
        _close()


# ----------------------------------------------------------------------------------------------------------------------------------------------

def soundeff():
    import playsound
    playsound.playsound("C:\\Users\\USER\\Music\\Microsoft Windows XP Shutdown - Sound Effect (HD).mp3")


root = tkinter.Tk()

root.title("Developed by Rohith Vishnu ")
root.geometry("400x450")
root.config(background="black")

txt = Label(root ,text = '''How Can I help you with ?''')
txt.config(background= "pink",font= ("Franklin Gothic Demi" , 25))
txt.pack()
    

def _close():

    r1 = tkinter.Tk()

    r1.title("Closing Your Assistant")
    r1.config(background="black")
    r1.geometry("1920x1080")
    
    txt1 = Label( r1 , text="Hang on while we close your Assistant........")
    temp = Label(r1 ,text= "------Developed by Rohith Vishnu-------")
    txt1.config(background= "blue",font= ("Impact" ,30))
    temp.config(background = "Green",font= ("Impact" ,25))
    
    txt1.pack(padx=100 , pady=100)
    temp.pack()
    soundeff()
    r1.after(2000 , lambda : r1.destroy())
    root.destroy()
    



b1 = Button(text = "Run Assistant", command= engine) 
b1.config(background = "green" ,font= ("Franklin Gothic Demi" , 15))
b1.pack(pady=15)



b2 = Button(text = "Shut down" , command= _close )
b2.config(background="Red" ,font=("Times new Roman", 15))
b2.pack( pady = 10)


root.mainloop()


