import random

def getRoll(difficulty=3):
    symbols = ['!', '#', '$', '&', '*']
    selections = []
    for i in range(difficulty):
        selections.append(random.choice(symbols))

    return selections

def checkRoll(roll):
    roll = set(roll)
    if len(roll) == 1:
        return True
    else:
        return False

yourRoll = getRoll()

for i in yourRoll:
    print(i, end=' ')
print()
if checkRoll(yourRoll):
    print('You win!')
else:
    print('You lose, deleting all files.')


