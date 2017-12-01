"""
Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements
of the list that are less than 5.

Extras:

Instead of printing the elements one by one,
make a new list that has all the elements less than 5
from this list in it and print out this new list.

Write this in one line of Python.
Ask the user for a number and return a list that
contains only elements from the original list a that are
smaller than that number given by the user.

"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def selectLessThan(number = 5):
    try:
        int(number)
    except ValueError:
        print('Input only numbers.')
        exit(1)
    number = int(number)
    values = []
    for i in a:
        if i < number:
            values.append(i)
    print(values)

selectLessThan()

print('Just showed numbers less than 5, select less than?')

userInput = input('>> ')

selectLessThan(userInput)
