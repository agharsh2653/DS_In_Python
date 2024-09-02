tag = ["moon","exercise","sundayfunday","give"]
def longestWord(tag):

     leng=len(tag[0])
     index=0
     for i in range(1,len(tag)):
          if(leng<len(tag[i])):
              leng=len(tag[i])
              index = i

     return leng,index

len,i=longestWord(tag)
print(len,tag[i])
