"""
Ask the user for a string and print out whether this string
is a palindrome or not. (A palindrome is a string that reads
the same forwards and backwards.)
"""

def checkPalindrome(input):
    a = input.lower()
    b = a [::-1]
    if a == b:
        print('Palindrome detected. Initializing countermeasures.')
    else:
        print("Registering safe for now.")

print("This will tell you if a string is a palindrome.")
print("Input your string.")
userInput = input('>> ')

checkPalindrome(userInput)
