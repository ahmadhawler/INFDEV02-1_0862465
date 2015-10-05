


user_input = raw_input('Enter you word here: ') #The user enters a string/word

word = str (user_input) #The word will be an user input, wich is a string

length = len(word) #Here it will show the lengt of the word, how many characters

i = length # i definse the length

final = []

while i > 0:
    final.append(word[i -1]) #so everytime it will be minus 1
    i -= 1 #so the word must be below zero, so that is will do every word minus one

null = '' #Here, there is nothing filled in

reversed = null.join(final) #Here, it will join the final, so that every string will be minus one

print(reversed) #Eventually, it will print out what the user has as an input