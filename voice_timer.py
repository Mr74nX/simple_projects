import pyttsx3
import sys, time
voice= pyttsx3.init()
voice.setProperty('rate', 180)
timer=int(input("Set Timer: "))
voices = voice.getProperty('voices')     
voice.setProperty('voice', voices[1].id)
for i in range(timer,0, -1):
    sys.stdout.write(f"\rTime Remaining: {i}  ")
    sys.stdout.flush()
    voice.say(str(i))
    time.sleep(1)
    voice.runAndWait()
