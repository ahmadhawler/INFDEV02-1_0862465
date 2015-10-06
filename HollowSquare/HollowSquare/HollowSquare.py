a = int(raw_input("How big do you want the hollow square to be?\n")) #The value of 'a' will be determind when the user has a string
                                                                     #as a value
m, n = a, a #a will be an value for m, how many astericks on 1 line, and for m will be an value for how many astericks going down.

for i in range (m):
    for j in range(n):
        print '*' if i in [0, n-1] or j in [0, m-1] else ' ', #For each asterick going down, there will be first 1 asterick,
    print ''                                                  #then it will skip the asterick untill the maximum of the given value is reached
                                                              #So if a=20 it will print nothing from 1 till 19. 0 and 20 there will be an asterick