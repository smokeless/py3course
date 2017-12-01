"""Ask the user for a number. Depending on whether the
number is even or odd, print out an appropriate message
to the user. Hint: how does an even / odd number react
differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different
message.
Ask the user for two numbers: one number to check
(call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user.
If not, print a different appropriate message."""
def checkInt(input):
    for i in input:
        try:
            int(i)
            return True
        except ValueError:
            return False

def even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def multipleOfFour(number):
    if number % 4 == 0:
        return True
    else:
        return False

def parseInput(input):
    splitInput = input.split()

    if not checkInt(splitInput):
        print('Please input only numbers.')
        exit(1)

    if len(splitInput) == 1:
        if even(int(splitInput[0])):
            print('This is an even number.')

        if not even(int(splitInput[0])):
            print('This is an odd number.')

        if multipleOfFour((int(splitInput[0]))):
            print('This is a multiple of four.')
        return
    num = int(splitInput[0])
    divisor = int(splitInput[1])

    if num % divisor == 0:
        print(num, 'divided by', divisor, 'results in even divide.' )
    else:
        print(num, 'divided by', divisor, 'results in uneven divide' )

    return



print('If a number is even, this will tell you.')
print('If a number is a multiple of 4 this will tell you.')
print('If you enter two numbers, you can find out if they evenly divide.')
print('Ex: 10 1')

getUserInput = input('>>')
parseInput(getUserInput)