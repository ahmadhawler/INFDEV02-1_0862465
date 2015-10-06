status = True
while(status): #While the status is true the program keeps running until it's broken.
    number = raw_input('Enter a number: ') #It will ask the user to give an number



    try:
        number = float(number) #It will give an decimal number, a floating point number
        print('The absolute value of your input is ' + str(abs(number))) #It will give an string back plus the absolut, that's why the abs
        status = False 

    except ValueError:
        print('Wrong number, please enter an correct number') #If the value of the input is incorrect, the program wil stop
                                                              #and ask for an correct number