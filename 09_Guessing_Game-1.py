"""Generate a random number between 1 and 9
(including 1 and 9). Ask the user to guess the number,
then tell them whether they guessed too low, too high,
or exactly right. (Hint: remember to use the user input
lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken,
and when the game ends, print this out."""
import random

def getInput():
    print("I'm thinking of a number from 1 to 9")
    uInput = input('>> ')
    return uInput

def checkInt(input):
    try:
        int(input)
        return True
    except ValueError:
        return False

guesses = 0
wins = 0
number = random.randint(1,9)

while True:
    uInput = getInput()
    if uInput == 'exit':
        print('You guessed', guesses, 'times.')
        exit(1)

    uInput = int(uInput)
    if uInput == number:
        wins += 1
        print('you guessed it!')
        print('you have won', wins, 'times')
    if uInput < number:
        guesses += 1
        print('the number is higher.')

    if uInput > number:
        guesses +=1
        print('the number is lower.')



