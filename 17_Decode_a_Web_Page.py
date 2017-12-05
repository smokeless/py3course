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