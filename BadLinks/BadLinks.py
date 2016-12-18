from urllib import parse, request
import requests
from queue import Queue
from link import Link
from bs4 import BeautifulSoup
import re
import pprint

#soup = BeautifulSoup(html, 'html.parser')
#href_and_src = soup.find_all(href = True)

def FindAllLinks(url):
    response = requests.get(url)
    print(response.status_code)
    html = (response.content).lower()
    hrefList = re.findall(b'href="(.*?)"', html)
    srcList = re.findall(b'src="(.*?)"', html)
    allLinkList = hrefList + srcList
    for i in range(len(allLinkList)):
        print(str(i) + ': ' + str(allLinkList[i]))

queue = Queue()
t = FindAllLinks('http://testingcourse.ru/links/page8.html')
