"""
Create a program that asks the user for a number
and then prints out a list of all the divisors of
that number. (If you don’t know what a divisor is,
it is a number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
"""

def parseInput(number):
    try:
        int(number)
    except ValueError:
        print('Use only numbers.')
        exit(1)

def printDivisors(number):
    number = int(number)
    for i in range(1, number):
        if number % i == 0:
            print(i, 'divides evenly.')

print('Input a number to see all the divisors.')
userInput = input('>> ')
parseInput(userInput)
printDivisors(userInput)