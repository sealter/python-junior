#usr/bin/python3

from urllib.request import urlopen
from bs4 import BeautifulSoup

def getTitle(url) :

    try :
        html = urlopen(url)
    except HttpError as httpErr :
        return None

    try :
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.h1
    except:
        return None
    return title


title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title == None :
    print("Title could not be found")
else :
    print("****", title)

