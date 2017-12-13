import random

def getRoll(difficulty=3):
    symbols = ['!', '#', '$', '&', '*']
    selections = []
    for i in range(difficulty):
        selections.append(random.choice(symbols))

    return selections

def checkRoll(roll):


yourRoll = getRoll()

for i in yourRoll:
    print(i, end=' ')

if checkRoll(yourRoll):
    print('You win!')
else:
    print('You lose, deleting all files.')


