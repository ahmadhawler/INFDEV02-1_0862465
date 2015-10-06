celsius = input("What's the weather today in Celsius?") #Here it will ask the user to fill an degree in celsius

if celsius > -273 and celsius < 141: #If it's between minus 273 and plus 141 it can be possible
    kelvin = celsius + 273 #Here it will define what the output is
    print "That is %s in Kelvin" %(kelvin) #It will print the text

else:
    print "That's not possible user, you're going to die" #So if the imput isn't possible, it will print out this message