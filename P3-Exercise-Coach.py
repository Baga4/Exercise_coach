"""This is a part of the previous coddig program 
(P2_ExerciseManager.py) you should download that file
in same folder you trying to run this code
"""


from P2_ExerciseManager import speak,dateandtime,save
import time

def cur_time ():
    time=dateandtime ()
    timea=time.split (" ")
    return timea [3]
    
def date ():
    date=dateandtime ()
    dates=date.split (" ")
    return dates[1]
    
def count (n):
   for i in range (1,n):
        speak (str(i))
        time.sleep(1)
      
def time_convert (int):
    mins = int // 60
    sec = int % 60
    mins = mins % 60
    return f" {mins} minutes and {sec} second"
    
    
def asksave (str):
    speak ("Do you want to add the {str} done in your manager app")
    user=input ("Yes/No--> ").capitalize ()
    if user=="Yes":
        date=dateandtime()
        info=f"{date} [DONE✔] {str}"
        save(info)
    elif user=="No":
        speak ("Make a good day")
    else:
        speak ("Only Yes and No is accepted")
        user=input ("-->" )

    
    
def start_exercise ():  
    speak ("Let's start exercising...")
    speak ("You will have exercise and a little break !, Get ready !")
    time.sleep(6)
    count(4)
    speak ("Go")
    
    Exercises=["L sit cross punch" ,
               "lying scissor raise",
               "Body weight crunches",
               "Russian twist",
               "Mountain climbers"
              ]
    for exe in Exercises:
        start_timer=time.time ()
        if exe is "Mountain climbers":
             speak(exe)
             count (20)
             break
        elif exe is "Body weight crunches" or exe is "Russian twist":
             speak (exe)
             count (20)
             speak ("Rest for 10 sec")
             count (10)
        else:
             speak (exe)
             count (20)
             speak ("Rest for 20 sec")
             count (20)
    end_time=time.time()
    time_took=end_time-start_timer
    time_taken=time_convert (time_took)
    speak ("Exercise complete ")
    speak (f"Day {date ()} done !")
    speak (f"You took {time_taken} to complete ")
    asksave ("Exercise")
    
def start_meditation ():
    speak ("This function is still in progress")

         
if __name__=="__main__":
    
    speak ("Good morning")
    speak (f"the time is {cur_time ()}")
    time.sleep (2.5)
    speak ("What should I start ? physical exercise or meditation")
   
    user=input ("-->> ").capitalize ()
    if user=="Exercise":
        start_exercise()
    elif user=="Meditation":
        start_meditation ()



