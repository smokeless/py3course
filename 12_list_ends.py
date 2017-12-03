"""
Write a program that takes a list of numbers
(for example, a = [5, 10, 15, 20, 25]) and makes a
new list of only the first and last elements of the given list.
For practice, write this code inside a function.
"""

def listEnds( list ):
    newList = []
    newList.append(list[0])
    newList.append(list[-1])
    return newList

a = [5, 10, 15, 20, 25]

print(listEnds(a))
