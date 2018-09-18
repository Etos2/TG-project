from Tkinter import *

#Load file
tg = {}
try:
    for entry in open("Class10w.txt"):
        entry.rsplit()
        student, attendance = entry.split(":")
        tg[student] = int(attendance) #int to catch errors
    #debug
    print(tg)

except:
    print("Error: Failed to load the attendance")
