from link import Link
from myqueue import MyQueue
import pprint


class BadLinks:
    def __init__(self, rsrc):
        self.__rsrc = rsrc.encode('utf-8')
        self.__queue = MyQueue()
        self.__queue.push(Link(self.__rsrc))
        self._handleResource()

    def _handleResource(self):     
        while (not(self.__queue.isEnd())):
            currentURL = self.__queue.pop()
            if (self.__rsrc in currentURL.getByteRef()):
                links = currentURL.getAllLinks()
            for i in links:
                self.__queue.push(Link(i))

    def __getRefWithStatus(self, link):
        s = str(link.getUtfRef()) + ' - status: '
        s = s+ str(link.getStatusCode()) + '\n'
        return s
    
    def printLinks(self):
        goodLinks = open('good_links.txt', 'w')
        badLinks = open('bad_links.txt', 'w')

        self.__queue.reset()
        while (not(self.__queue.isEnd())):
            currentURL = self.__queue.pop()
            if (currentURL.isWorking()):
                goodLinks.write(self.__getRefWithStatus(currentURL))
            else:
                badLinks.write(self.__getRefWithStatus(currentURL))
                
        badLinks.close()
        goodLinks.close()

#t = BadLinks('http://testingcourse.ru/links/')
url = input('Введите адрес: ')
t = BadLinks(url)
t.printLinks()
