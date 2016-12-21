from link import Link
from myqueue import MyQueue
import pprint


class BadLinks:
    def __init__(self, rsrc):
        self.__rsrc = rsrc
        self.__queue = MyQueue()
        self.__queue.push(Link(self.__rsrc))
        self._handleResource()

    def _handleResource(self):     
        while (not(self.__queue.isEnd())):
            currentURL = self.__queue.pop()
            if (self.__rsrc in currentURL.getRef()):
                links = currentURL.getAllLinks()
            for i in links:
                self.__queue.push(Link(i))

    def printLinks(self):
        goodLinks = open('good_links.txt', 'w')
        badLinks = open('bad_links.txt', 'w')
        
        self.__queue.reset()
        while (not(self.__queue.isEnd())):
            currentURL = self.__queue.pop()
            if (currentURL.isWorking()):
                goodLinks.write(str(currentURL.getRef()) + ' ' + str(currentURL.getStatusCode()) + '\n')
            else:
                badLinks.write(str(currentURL.getRef()) + ' ' + str(currentURL.getStatusCode()) + '\n')
                
        badLinks.close()
        goodLinks.close()

t = BadLinks(b'http://testingcourse.ru/links/')
t.printLinks()
