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

#Occurs when no file
except IOError:
    print("Error: Failed to load the attendance")
    print("IOError")

#Occurs when invalid value    
except ValueError:
    print("Error: Failed to load the attendance")
    print("ValueError")

    for entry in open("Class10w.txt"):
        entry.rsplit()
        student, attendance = entry.split(":")
        try:
            attendance = int(attendance)
        except:
            tg[student] = (attendance)
            print(student + ":" + attendance)

except:
    print("Error: Failed to load the attendance")
    print("Unknown Error")    
