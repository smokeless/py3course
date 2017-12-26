import random

def checkNumber(number: int)->float:
    if number % 3 == 0:
        return number
    elif (number + 1) % 3 == 0:
        print('('+str(number), '+ 1)')
        print(number + 1)
        return number + 1
    else:
        print('('+str(number), ' - 1)')
        print(number - 1)
        return number - 1


print('input a starting number, or i will generate one.')
uIn = input('>> ')
if not uIn.isdigit():
    print("Didn't input a number, I'll generate one.")
    uIn = random.randint(100, 57821)
uIn = int(uIn)
print('your number is', uIn)

counter = 0
while uIn != 1:
    uIn = checkNumber(uIn)
    print('dividing', uIn, 'by 3')
    uIn = uIn // 3
    counter += 1
    if uIn == 1:
        print(1)
        print('took', counter, 'steps.')
