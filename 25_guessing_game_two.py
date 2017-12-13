'''
In a previous exercise, we’ve written a program that “knows”
a number and asks a user to guess it.

This time, we’re going to do exactly the opposite.
You, the user, will have in your head a number between
0 and 100. The program will guess a number, and you,
the user, will say whether it is too high, too low, or your number.

At the end of this exchange, your program should print out how
many guesses it took to get your number.

As the writer of this program, you will have to
choose how your program will strategically guess.
A naive strategy can be to simply start the guessing at 1,
and keep going (2, 3, 4, etc.) until you hit the number.
But that’s not an optimal guessing strategy.
An alternate strategy might be to guess 50
(right in the middle of the range), and then increase
/ decrease by 1 as needed. After you’ve written the program,
try to find the optimal strategy!
(We’ll talk about what is the optimal one next week with the solution.)
'''

def getInput()->str:
    uIn = input('>> ')
    while uIn != 'c' and uIn != 'l' and uIn != 'h':
        uIn = input('c, h, or l>> ')
    return uIn


print('You think of a number between 1 and 100 and I will guess it.')
print('Enter h for high, l for low, c for correct')

guessesMade = 1
workingList= list(range(1, 101))
myGuess = workingList[int(len(workingList)/2)]
gameOver = False
print('My guess is:', myGuess)

while not gameOver:
    print('Enter h for high, l for low, c for correct')
    uIn = getInput()
    if uIn == 'c':
        gameOver = True
        if guessesMade > 1:
            print('I made:', guessesMade, 'guesses.')
        else:
            print('I made:', guessesMade, 'guess.')
            print('My incredible computer brain has defeated you!')
        raise SystemExit

    if uIn == 'h':

    guessesMade += 1