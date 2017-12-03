"""
Ask the user for a number and determine whether the number is
prime or not. (For those who have forgotten, a prime number
is a number that has no divisors.). You can (and should!)
use your answer to Exercise 4 to help you.
Take this opportunity to practice using functions, described below.

"""

def getInput():
    print('Input a number to check for prime.')
    uInput = input('>> ')
    try:
        int(uInput)
    except ValueError:
        print('invalid input')
    return int(uInput)

def isPrime(number):
    number = int((number/2)+1)
    for i in range(2, number):
        if number % i == 0:
            print(number, 'divisible by', i)
            return False
    return True


uInput = getInput()
if isPrime(uInput):
    print("It's prime.")
else:
    print("It's not prime.")
