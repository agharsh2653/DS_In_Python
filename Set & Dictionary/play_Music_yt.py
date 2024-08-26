import pywhatkit as pw

def play_music_on_youtube(Song_name):
     pw.playonyt(Song_name)

while True:
     s = input("Enter song name ")
     play_music_on_youtube(s)