f = open("poem.txt","r")
data = f.read()
if("Twinkle" in data):
     print("The word twinkle is present in the file")
else:
      print("The word twinkle is not present in the file")
f.close()