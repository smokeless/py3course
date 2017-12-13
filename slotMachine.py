import random

def getNumbers(difficulty):
    symbols = ['!', '#', '$', '&', '*']
    selections = []
    for i in range(difficulty):
        selections.append(random.choice(symbols))

    return selections

yourRoll = getNumbers(30)

for i in yourRoll:
    print(i, end=' ')

