
class MyQueue:
    
    def push(self, el):
        if ((el in self.__list) or not(el)):
            return
        self.__length += 1
        self.__list.append(el)

    def pop(self):
        if self.empty():
            return
        self.__pos += 1
        return self.__list[self.__pos - 1]

    def length(self):
        return self.__length

    def getPos(self):
        return self.__pos

    def isEnd(self):
        return self.__pos == self.length()

    def empty(self):
        return self.length() == 0

    def reset(self):
        self.__pos = 0

    __list = []
    __pos = 0
    __length = 0
