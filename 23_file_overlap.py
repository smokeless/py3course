'''
Exercise 23 (and Solution)

Given two .txt files that have lists of numbers in them,
find the numbers that are overlapping. One .txt file has
a list of all prime numbers under 1000, and the other .txt
file has a list of happy numbers up to 1000.

(If you forgot, prime numbers are numbers that can’t
be divided by any other number. And yes, happy numbers
are a real thing in mathematics - you can look it up on Wikipedia.
The explanation is easier with an example, which I will describe below.)
'''

import requests

def getTextFromSiteList(*arg: str)->list:
    '''In, site urls. Out list of txt of each url.'''
    siteTxtArray = []
    for i in arg:
        r = requests.get(i)
        txt = r.text
        siteTxtArray.append(txt)

    return siteTxtArray

def checkForOverLap(f1: str, f2: str)->str:
    fileOne = f1.split()
    fileTwo = f2.split()
    newList = []
    if len(fileOne) > len(fileTwo):
        for i in f2:
            if i in f1:
                newList.append(i)
    else:
        for i in fileOne:
            if i in fileTwo:
                newList.append(i)





urls    = ['http://www.practicepython.org/assets/primenumbers.txt',
           'http://www.practicepython.org/assets/happynumbers.txt']

txtList = getTextFromSiteList(urls[0], urls[1])
primes  = txtList[0]
happy   = txtList[1]
checkForOverLap(primes, happy)