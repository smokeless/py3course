'''
Write a function that takes an ordered list of numbers
(a list where the elements are in order from smallest to largest)
and another number. The function decides whether or not the
given number is inside the list and returns (then prints)
an appropriate boolean.

Extras:

Use binary search.
'''

import random

def generateSortedList(elements):
    l = []
    for i in range(0, elements):
        x = random.randint(1, 50)
        l.append(x)
    l.sort()
    return l

def generateNumber():
    return random.randint(1, 100)

def inList(listNumbers, number):
    lo = 1
    hi = len(listNumbers)
    if number < listNumbers[0] or number > listNumbers[-1]:
        return False
    if number == listNumbers[0] or number == listNumbers[-1]:
        return True

    while lo <= hi:
        mid = int(lo + (hi-lo)/2)
        if listNumbers[mid] == number:
            return True
        elif listNumbers[mid] < number:
            lo = mid + 1
        else:
            hi = mid - 1
    return False

for i in range(0, 20):
    sl = generateSortedList(10)
    n = generateNumber()
    print(n, sl)
    print(inList(sl, n))

