'''
Write a program that asks the user how many Fibonnaci
numbers to generate and then generates them. Take this
opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers
in the sequence to generate.(Hint: The Fibonnaci seqence
is a sequence of numbers where the next number in the sequence
is the sum of the previous two numbers in the sequence.
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
'''

def getUserInput():
    print('How many numbers of the Fib sequence do you want?')
    uInput = input('>> ')
    try:
        int(uInput)
    except ValueError:
        print('please input integers.')
    return int(uInput)

def genFib(number):
    list = [1, 1]
    if number == 1:
        print([1])
        return
    if number == 2:
        print([1, 1])
        return
    while len(list) < number:
        list.append(list[-1] + list[-2])

    print(list)


uInput = getUserInput()
genFib(uInput)