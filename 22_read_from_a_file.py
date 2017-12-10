'''
Given a .txt file that has a list of a bunch of names,
count how many of each name there are in the file, and
print out the results to the screen. I have a .txt file for
you, if you want to use it!

Extra:

Instead of using the .txt file from above
(or instead of, if you want the challenge),
take this .txt file, and count how many of each
“category” of each image there are.
This text file is actually a list of files corresponding
to the SUN database scene recognition database, and lists the
file directory hierarchy for the images. Once you take a look
at the first line or two of the file, it will be clear which
part represents the scene category. To do this, you’re going to
have to remember a bit about string parsing in Python 3.
I talked a little bit about it in this post.

http://www.practicepython.org/assets/Training_01.txt
'''

import requests
import os
#lots of hardcoded stuff. gross, but meets the requirements.
def getFile():
    url    = 'http://www.practicepython.org/assets/Training_01.txt'
    r      = requests.get(url)
    r_html = r.text
    with open('textfile.txt', 'w') as txt:
        txt.write(r_html)

def delFile():
    try:
        os.remove('./textfile.txt')
    except FileNotFoundError:
        print('File not found!')

def countCategory():
    getFile()
    with open('textfile.txt', 'r') as words:
        txt = words.read()
    txt = txt.split('/')
    txt = list(set(txt))
    cleanedTxt = []
    for i in txt:
        if not 'sun' in i and len(i) > 1:
            cleanedTxt.append(i)
    cleanedTxt = set(cleanedTxt)
    print(cleanedTxt)



    delFile()

countCategory()