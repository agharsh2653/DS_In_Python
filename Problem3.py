import pyttsx3

engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()

# write a python program to print the contents of a directory using the os module.
# search onlime for the function which does that
Problem4
import os
#Select the directories whose content want to list
directory_path = '/hp'

#List of all file and directories.in the specified path
contents = os.listdir(directory_path)

#print all the file and directory name 
for item in contents:
     print(item)
