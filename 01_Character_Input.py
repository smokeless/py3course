"""Create a program that asks the user to enter their name and their
age. Print out a message addressed to them that tells them the year
that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another
number and printing out that many copies of the previous message.
(Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines.
(Hint: the string "\n is the same as pressing the ENTER button)"""
import datetime

def checkInt(input):
    try:
        int(input)
        return True
    except ValueError:
        return False

def getYearAt100(age):
    now = datetime.datetime.now()
    currentYear = now.year
    age = 100 - int(age)
    oneHundred = currentYear + age
    return oneHundred

def printMessage(name, age):
    age = getYearAt100(age)
    print('Hey', name, 'you will be 100 in:', age )



print('Please input your name.')
name = input('>>')

print('Please input the age you will be this year.')
age = input('>>')



if checkInt(age):
    printMessage(name, age)
else:
    print('Bad age input.')
    exit(1)

print('How many repeats would you like?')
repeats = input('>>')

if checkInt(repeats):
    for i in range(int(repeats)):
        printMessage(name, age)
else:
    print('Bad multiplier.')
    exit(1)