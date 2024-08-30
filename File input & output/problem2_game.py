import random

def game():
     print("You are playing the game..")
     score = random.randint(1,55)
     #Fetch the hiscore
     with open("hiscore.txt") as f:
          hiscore = f.read()
          if(hiscore!=""):
               hiscore = int(hiscore)
          else:
               hiscore = 0
     print("Your score: ",score)
     if(score>hiscore):
          #write this hiscore to the file hiscore
          with open("hiscore.txt","w") as f:
               f.write(str(score))
     return score

game()