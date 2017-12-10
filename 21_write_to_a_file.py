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

    for title in o.find_all('h2', {'class':'story-heading'}):
        headline = title.getText()
        headline = headline.strip()
        print(headline)
        if doubleSpace == True:
            print()



def makeRequest():
    url    = 'http://newyorktimes.com'
    r      = requests.get(url)
    r_html = r.text
    return r_html


print('Input 1 for single space. 2 for double space.')
uInput = input('>> ')

if uInput == '1':
    getTitles(makeRequest())
elif uInput == '2':
    getTitles(makeRequest(), True )
else:
    exit(1)