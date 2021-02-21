# This is the pyhton project for time manager  
import pyttsx3
import datetime
import time
from beeply.notes import *

#function for sound
def AlarmSound():

    a = beeps() 
    for i in range(3):
        a.hear('C_',330) 
        a.hear("A") 

# function for alarm 
def alarm():
    
    print('You have selected alarm clock!')
    hour = int(input("Enter the alarm hour (12 hour format):"))
    minute = int(input("Enter alarm minute:"))
    ampm = str(input("am or pm:"))

    if (ampm == "am" and hour == 12):
        hour = hour - 12
    elif (ampm == "pm" and hour == 12):
        hour = hour
    elif (ampm == "pm" and hour != 12):
        hour = hour + 12
    
    while True:
        if (hour == datetime.datetime.now().hour and minute == datetime.datetime.now().minute):
            print("Wake Up!")
            AlarmSound()
            break

# function for text to speech
def speak(i):
    
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(i)
    engine.runAndWait()

# function for reminder        
def reminder():
    
    print('You have selected reminder!')
    print("What do you want to get reminded about? :")
    message=str(input())
    hour = int(input("Enter the reminder hour (12 hour format):"))
    minute = int(input("Enter reminder minute:"))
    ampm = str(input("am or pm:"))
    
    if (ampm == "am" and hour == 12):
           hour = hour - 12
    elif (ampm == "pm" and hour == 12):
       hour = hour
    elif (ampm == "pm" and hour != 12):
       hour = hour + 12

    while True:
        if (hour == datetime.datetime.now().hour and minute == datetime.datetime.now().minute):
            print(message)
            AlarmSound()
            speak(message)
            break    

# function for timer
def timer():
    
    print('You have selected timer!')
    t = int(input("How many seconds do you want to set timer for?"))
    while t:
        min = t // 60
        sec = t % 60
        countdown = '{:02d}:{:02d}'.format(min, sec)
        print(countdown, end="\r")
        time.sleep(1)
        t -= 1
    print("Time's up!!")  
    AlarmSound()  

# Combining all the functions to make a fully functional time manager
# This while loop is created so that program keeps asking for input until it gets the right input i.e. 1 or 2 or 3

print("Welcome to time manager!!")
while True:
    print("What do you want to set? \n(input 1 for alarm, input 2 for reminder, input 3 for timer)")
    task_req = int(input())
    if (task_req == 1):
        alarm()
        break
    elif (task_req == 2):
        reminder()
        break
    elif (task_req == 3):
        timer() 
        break        
    else:
        print("Wrong input!!! Please enter again")    
    
# 1 is for alarm 
# 2 is for reminder 
# 3 is for timer    

    
    
