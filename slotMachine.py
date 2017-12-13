import random

def getRoll(difficulty=3):
    symbols = ['!', '#', '$', '&', '*']
    selections = []
    for i in range(difficulty):
        selections.append(random.choice(symbols))

    return selections

def checkRoll(roll):
    for i in roll:
        if i == roll[0]:
            return True
        else:
            return False

yourRoll = getNumbers(3)

for i in yourRoll:
    print(i, end=' ')

if checkRoll(yourRoll):
    print('You win!')
else:
    print('You lose, deleting all files.')


