words = "red, white, black, red, green, black"
lag = words.split(",")
lag.sort()
words=""
for i in range(len(lag)):
     if(lag[i]==lag[i-1]):
          continue
     else:
          words += lag[i] +","

print(words)

#items = "red, white, black, red, green, black"
# words = [word for word in items.split(",")]

# print(",".join(sorted(list(set(words)))))
