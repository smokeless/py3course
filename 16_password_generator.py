'''
Exercise 16 (and Solution)

Write a password generator in Python. Be creative with how you
generate passwords - strong passwords have a mix of lowercase letters,
uppercase letters, numbers, and symbols. The passwords should
be random, generating a new password every time the user asks
for a new password. Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
'''

import random
import string

passwordList = ['blue', 'orange', 'armadillo', 'letter', 'golden']

def genPassword(difficulty):
    password = ''
    random.seed()
    randomNumber = random.randint(0, len(passwordList)-1)
    randomNumber2 = random.randint(0, len(passwordList)-1)
    if difficulty == 1:
        element = passwordList[randomNumber]
        element += passwordList[randomNumber2]
        print(element)
        return
    if difficulty == 2:
        word  = str(random.randint(0,600))
        word += passwordList[randomNumber]
        word += str(random.randint(0,600))
        word += passwordList[randomNumber2]
        word += str(random.randint(0, 600))
        print(word)
        return
    if difficulty == 3:
        characters = string.ascii_letters + string.digits
        word = ''
        for i in range(0, 24):
            word += random.choice(characters)
        print(word)


print('This is for educational purposes, never use'
      ' this to actually generate a password. Enter '
      'a number from 1-3 for complexity')

#No error checking let it burn!
uInput = int(input('>> '))

genPassword(uInput)