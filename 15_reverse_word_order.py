'''
Write a program (using functions!) that asks the user for a
long string containing multiple words. Print back to the user
the same string, except with the words in backwards order.
For example, say I type the string:

  My name is Michele
Then I would see the string:

  Michele is name My
shown back to me.
'''
def reverseInput(longString):
    for i in longString[::-1]:
        print(i, end=' ')
    print()

print('what shall i reverse?')
uInput = input('>> ')
uInput = uInput.split()
reverseInput(uInput)


