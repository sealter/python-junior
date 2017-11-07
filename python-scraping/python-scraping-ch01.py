#usr/bin/python3

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page1.html")
print(html.read())
bsObj = BeautifulSoup(html.read(), "html.parser")
print(bsObj.h1)

html2 = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj2 = BeautifulSoup(html2.read(), "html.parser")

for name in bsObj2.findAll("span", {"class": "red"}) :
    print(name)


print(bsObj2.findAll({"h1", "h2", "h3"}))

nameList = bsObj2.findAll(text="the prince")
print("**** nameList length = ", len(nameList))



print("******** get_text() ***********")

allText = bsObj2.findAll(id="text")
print("---- text = ", allText[0].get_text())



print("********* findAll using class_ *********")

print("--------- findAll by class_ ", bsObj2.findAll(class_="green"))


print("************** Navigating Trees ************")

print("**** 1. children and descendants *****")

html3 = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj4 = BeautifulSoup(html3.read(), "html.parser")
for child in bsObj4.find("table", {"id": "giftList"}).children :
    print(child)


print("*** 2. sibling ***")

for sibling in bsObj4.find("table", {"id": "giftList"}).tr.next_siblings:
    print(sibling)


for sibling in bsObj4.find("table", {"id": "giftList"}).tr.previous_siblings:
    print(sibling)


print("*** 3. parent ***")

print(bsObj4.find("img", {"src", "../img/gifts/img1.jpg"}))
