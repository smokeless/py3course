'''
Take the code from the How To Decode A Website
exercise (if you didn’t do it or just want to play with
some different code, use the code from the solution),
and instead of printing the results to a screen,
write the results to a txt file.
In your code, just make up a name for the file you are saving to.

Extras:

Ask the user to specify the name of the output file that will be saved.

'''

from bs4 import BeautifulSoup
import requests

"""
Use the BeautifulSoup and requests Python packages to print out 
a list of all the article titles on the New York Times homepage.
"""

def getTitles(plainTextHTML, doubleSpace=False):
    '''parse headline titles out'''
    o = BeautifulSoup(plainTextHTML, 'html.parser')
    text = str()
    for title in o.find_all('h2', {'class':'story-heading'}):
        headline = title.getText()
        headline = headline.strip()
        text += headline + '\n'
        if doubleSpace == True:
            text += '\n'
    return text


def makeRequest():
    url    = 'http://newyorktimes.com'
    r      = requests.get(url)
    r_html = r.text
    return r_html


print('Input 1 for single space. 2 for double space. Then a space. Then file name.')
uInput = input('>> ')
unparsedRequest = makeRequest()
uInput = uInput.split()
try:
    int(uInput[0])
except ValueError:
    print('invalid syntax.')

flag     = int(uInput[0])
fileName = uInput[1]

if flag == 1:
    flag = False
elif flag == 2:
    flag = True
else:
    print('invalid flag')
    exit(1)

with open(fileName, 'w') as f:
    f.write(getTitles(unparsedRequest, flag))

#if uInput == '1':
#    getTitles(makeRequest())
#elif uInput == '2':
#    getTitles(makeRequest(), True )
#else:
#    exit(1)