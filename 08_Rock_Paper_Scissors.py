"""
Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input),
compare them, print out a message of congratulations
to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock

"""

import random


moves = { 0 : 'rock', 1 : 'paper', 2 : 'scissors'}

def opponentSelection():
    return( moves[random.randint(0,2)] )


def getPlayerInput():
    print('choose: rock, paper, or scissors')
    uInput = input('>> ')
    uInput.lower()
    if not uInput in moves.values():
        print("not a valid input.")
    return uInput

def determineWinner( player, computer ):
    print('You selected', player )
    print('The computer selected', computer )
    if player == computer:
        print( 'draw' )

    if player == 'rock' and computer == 'paper':
        print('The computer wins.')
    if player == 'rock' and computer == 'scissors':
        print('Player wins.')
    if player == 'paper' and computer == 'scissors':
        print('computer wins.')
    if player == 'paper' and computer == 'rock':
        print('player wins.')
    if player == 'scissors' and computer == 'rock':
        print('computer wins')
    if player == 'scissors' and computer == 'paper':
        print('player wins.')
    return

def playAgain():
    print('play again?')
    uInput = input('[y/n] ')

    if uInput != 'y' and uInput != 'n':
        print('invalid input')
        playAgain()

    if uInput == 'y':
        return True
    else:
        return False

while True:
    computer = opponentSelection()
    player = getPlayerInput()
    if player != 'rock' and player != 'scissors' and player != 'paper':
        player = getPlayerInput()
    determineWinner(player, computer)
    if not playAgain():
        break