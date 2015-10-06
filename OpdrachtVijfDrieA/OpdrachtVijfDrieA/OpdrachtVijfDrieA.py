import sys

word = raw_input ("Fill in an sentence, user: ") #Here it will ask for an input from the user
n = input ("How many characters do you want to shift, user?") #It will ask for an input again

for a in word:
    a = ord(a) #Here it will turn the the characters into integers
    if ord('a') <= a <= ord('z'): #The value must be between the strings A and Z
        a = a - ord('a') #it will decrease the value with minus one letter but still between 1 and 26
        a = (a + n) % 26 #So again, is will calculate with the value of A and N, given from the input, with a max of 26
        a = a + ord('a') #Add the value of A again so we will be back at the beginning
        a = chr(a) #From the beginning we wanted an integer, now we want an string returned
    elif ord('A') <= a <= ord('Z'): #Exact the same, only for capital letters
        a = a - ord('A')
        a = (a + n) % 26
        a = a + ord('A')
        a = chr(a)
    else:
        a = chr(a) #It will all be automatically printed if not so. But it will only print it if above is not true
    sys.stdout.write(a) #This line of code will print it without enters, but like an sentence