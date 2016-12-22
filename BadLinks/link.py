from urllib import parse, request
import requests
import re


class Link:
    def __init__(self, ref):
        self.__ref = ref
        self.__response = False
        self.__status_code = 'skip'
        if (self.__ref.startswith(b'http')):
            self.__response = requests.get(ref)
            self.__status_code = self.__response.status_code

    def getByteRef(self):
        return self.__ref

    def getUtfRef(self):
        return self.__ref.decode('utf-8')

    def getStatusCode(self):
        return self.__status_code

    def getAllLinks(self):
        if (not(self.isWorking)):
            return list()
        html = (self.__response.content).lower()
        hrefList = re.findall(b'href="(.*?)"', html)
        srcList = re.findall(b'src="(.*?)"', html)
        return (self.convertRelativeToAbsolute(hrefList + srcList))

    def convertRelativeToAbsolute(self, linksList):
        for i in range(len(linksList)):
            linksList[i] = parse.urljoin(self.__ref, linksList[i])
        return linksList

    def __eq__(self, other):
        return (self.getByteRef() == other.getByteRef())

    def __ne__(self, other):
        return (self.getByteRef() != other.getByteRef())

    def isWorking(self):
        if (self.__status_code == 'skip'):
            return False
        else:
            return (100 <= self.__status_code <= 301)

