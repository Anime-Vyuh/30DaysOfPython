from datetime import datetime
from playsound import playsound
import pyttsx3 as ts
import time
speak = ts.init()

def gettime():
    try:
        alarm = input("Enter the time to be alarmed(hr:min PM/AM):")
        return alarm
    except TypeError:
        print('Invalid')
    except ValueError:
        print("Invalid")

def time_based(alarm_time):
    alarm_hour=alarm_time[0:2]
    alarm_min=alarm_time[3:5]
    alarm_period=alarm_time[6:8].upper()
    print("Alarm Set")
    speak.say("Alarm Set")
    speak.runAndWait()
    while True:
        now = datetime.now()
        current_hour = now.strftime("%H")
        current_min = now.strftime("%M")
        current_period = now.strftime("%p")
        if current_hour==alarm_hour and current_min==alarm_min and current_period==alarm_period:
            speak.say("Wake up tarun")
            speak.runAndWait()
            time.sleep(2)
            playsound("/home/lucifertrj/Music/Arcade.mp3")
            break

alarm_time = gettime()
time_based(alarm_time)

