print "Welcome to Rock, Paper, Scissors, Lizard or Spock" #This is the message that is shown when the player enters the game

player1 = raw_input ("Player 1 select your choice please: ") #The choice of player 1
player2 = raw_input ("Player 2 select your choice please: ") #The choice of player 2

if (player1 == 'rock' and player2 == 'rock'):
    print "This game is a tie."

elif (player1 == 'rock' and player2 == 'scissors'):
    print "Rock crushes scissors, player 1 wins"

elif (player1 == 'scissors' and player2 == 'scissors'):
    print "This game is a tie."

elif (player1 == 'paper' and player2 == 'paper'):
    print "This game is a tie."

elif (player1 == 'paper' and player2 == 'scissors'):
    print "Scissors cut paper, player 2 wins"

elif (player1 == 'rock' and player2 == 'paper'):
    print "Paper covers rock, player 2 wins"

elif (player1 == 'paper' and player2 == 'rock'):
    print "Paper covers rock, Player 1 wins"

elif (player1 == 'scissors' and player2 == 'rock'):
    print "Rock crushes scissors, player 2 wins"

elif (player1 == 'spock' and player2 == 'spock'):
    print "This game is a tie."

elif (player1 == 'lizard' and player2 == 'lizard'):
    print "This game is a tie."

elif (player1 == 'spock' and player2 == 'lizard'):
    print "Lizard poisons spock, Player 2 wins"

elif (player1 == 'lizard' and player2 == 'spock'):
    print "Lizard poisons spock, Player 1 wins"

elif (player1 == 'rock' and player2 == 'lizard'):
    print "Rock crushes lizard, Player 1 wins"

elif (player1 == 'lizard' and player2 == 'rock'):
    print "Rock crushes lizard, Player 2 wins"

elif (player1 == 'spock' and player2 == 'rock'):
    print "Spock vaporizes rock, Player 1 wins"

elif (player1 == 'rock' and player2 == 'spock'):
    print "Spock vaporizes rock, Player 2 wins"

elif (player1 == 'scissors' and player2 == 'lizard'):
    print "Scissors decapitates lizard, Player 1 wins"

elif (player1 == 'lizard' and player2 == 'scissors'):
    print "Scissors decapitates lizard, Player 2 wins"

elif (player1 == 'spock' and player2 == 'scissors'):
    print "Spock smashes scissors, Player 1 wins"

elif (player1 == 'scissors' and player2 == 'spock'):
    print "Spock smashes scissors, Player 2 wins"

elif (player1 == 'paper' and player2 == 'lizard'):
    print "Lizard eats paper, Player 2 wins"

elif (player1 == 'lizard' and player2 == 'paper'):
    print "Lizard eats paper, Player 1 wins"

elif (player1 == 'spock' and player2 == 'paper'):
    print "Paper disproves spock, Player 2 wins"

elif (player1 == 'paper' and player2 == 'spock'):
    print "Paper disproves spock, Player 1 wins"

else:
    print "This is not an valid selection. Please select Rock, Paper, Lizard or Spock"

    #So if all these options are chosen, the game wil be played normally. Either a player wins or it's a tie. If not so,
    #there will be an message printed that will show that the chosen option is not possible.