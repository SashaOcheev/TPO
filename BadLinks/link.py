class Link:

    def __init__(self, ref, errno, errmsg):
        self.__ref = ref
        self.__errno = errno
        self.__errmsg = msg

    def getRef(self):
        return self.__ref

    def geErrNo(self):
        return self.__errno

    def getErrMsg(self):
        return self.__errmsg

    def __eq__(self, other):
        return (self.getRef() == other.getRef())

    def __ne__(self, other):
        return (self.getRef() != other.getRef())

    def isWorking(self):
        return (not(self.__errno) or (100 <= self.__errno <= 301))

    __ref = ''
    __errno = 0
    __errmsg = ''
