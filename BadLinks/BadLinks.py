from queue import Queue
from link import Link


class BadLinks:
    def __init__(self, rsrc):
        self.__rsrc = rsrc
        self.__queue = Queue()
        self.__queue.push(Link(self.rsrc))
        self._handleResource()

    def _handleResource(self):
        while (not(self.__queue.isEnd())):
            currentURL = self.__queue.pop()
            if (rsrc in currentURL):
                links = currentURL.GetAllLinks()
                for i in links:
                    queue.push(Link(i))
        print(queue.length())
        

#t = BadLinks('http://testingcourse.ru/links/')
t = Queue()
t.push(1)
