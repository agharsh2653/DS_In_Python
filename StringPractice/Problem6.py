string = "string"
if(len(string)>2):
     if(string.endswith("ing")):
          string+="ly"
     else:
          string+="ing"

print(string)

lyrics = 'The lyrics is not that poor!'

start = lyrics.find("not")
end = lyrics.find("poor")+4
st1=lyrics[start:end]
print(lyrics.replace(st1,"good"))


print(id(lyrics))