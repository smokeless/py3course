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

def returnSet(list):
    return list(set(list))

def returnUnique(list):
    newList = []
    [newList.append(item) for item in list if item not in newList]

list = [1, 1, 1, 2, 2, 3, 5, 8]

print(returnSet(list))
print(returnUnique(list))
