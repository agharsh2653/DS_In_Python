def insert_end_char(word):
     s=""
     for i in range(0,4):
          s+=word
     return s

word = input("Enter the word: ")
if(len(word)>2):
     print(insert_end_char(word[len(word)-2:]))
