'''
Write a program (function!) that takes a list and returns a new
list that contains all the elements of the first list minus all
the duplicates.

Extras:

Write two different functions to do this - one using a
loop and constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the
solution for that in a different function.
'''

def returnSet(aList):
    return list(set(aList))

def returnUnique(aList):
    newList = []
    [newList.append(item) for item in aList if item not in newList]
    return newList

myList = [1, 1, 1, 2, 2, 3, 5, 8]

print(returnSet(myList))
print(returnUnique(myList))
