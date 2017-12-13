import random

def getNumbers():
    symbols = ['!', '#', '$', '&', '*']
    selections = []
    for i in range(1, 4):
        selections.append(random.choice(symbols))

    return selections

yourRoll = getNumbers()

for i in yourRoll:
    print(i, end=' ')
print()