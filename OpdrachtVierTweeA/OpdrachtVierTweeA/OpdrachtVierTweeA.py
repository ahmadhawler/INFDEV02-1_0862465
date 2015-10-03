print "Welcome to Rock, Paper and Scissors"

player1 = raw_input ("Player 1 select your choice please: ")
player2 = raw_input ("Player 2 select your choice please: ")

if (player1 == 'rock' and player2 == 'rock'):
    print "This game is a tie."

elif (player1 == 'rock' and player2 == 'scissors'):
    print "Player 1 is the winner."

elif (player1 == 'scissors' and player2 == 'scissors'):
    print "This game is a tie."

elif (player1 == 'paper' and player2 == 'paper'):
    print "This game is a tie."

elif (player1 == 'paper' and player2 == 'scissors'):
    print "Player 2 wins"

elif (player1 == 'rock' and player2 == 'paper'):
    print "Player 2 wins"

elif (player1 == 'paper' and player2 == 'rock'):
    print "Player 1 wins"

elif (player1 == 'scissors' and player2 == 'rock'):
    print "Player 2 wins"

else:
    print "This is not an valid selection. Please select Rock, Paper or Scissors"