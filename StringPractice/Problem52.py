# Write a Python program to print all permutations with a given repetition number of characters of a given string
import string
def permutation(p,up):
     if(len(up)==0):
          list=[]
          list.append(p)
          return list
     
     ch = up[0]
     ans = []
     for i in range(0,len(up)):
          f=p[0:i]
          s=p[0:len(p)]
          ans.append(permutation((f+ch+s),up[:1]))
     return ans

print(permutation("","xyz"))
