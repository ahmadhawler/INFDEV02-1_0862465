running=True #So while it is running, the password is true
while running:
    p = raw_input("What is your Password? ") #the letter P stands for password
    if len(p) <8:                            #if the password is shorter than 6 characters, it's too short
        print "Your Password is too short"
    if len(p) >15:                           #if the password is longer than 15 characters, it's too long
        print "Your Password is too long"
    if len(p) == 8 or 9 or 10 or 11 or 12 or 13 or 14: #if the password is between 8 and 14 characters, it's OK
        print "Password Length OK"
        running=False #Here, the program will stop, and show the message. 
        #It will say that maybe the password is too long, but it will give you some advice that maybe it's too long, but the length is OK

if p.isupper():
    print "Your Password is weak as it only contains capital letters"

if p.islower():
    print "Your Password is weak as it only contains lower case letters"

if p.isupper and p.islower:
    print "Your Password is of medium strength, try adding some numbers" #Some printed advice


try:
    int(p) #If the password is only numbers, it will say that it's weak.
    print "Your Password is weak as it only contains numbers"
except (ValueError, TypeError): #Here, it will give you an value error for the pasword or an type error, so you know where the problem is
    pass