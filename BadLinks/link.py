from urllib import parse, request
import requests
import re


class Link:

    def __init__(self, ref):
        self.__ref = ref
        self.__response = requests.get(ref)
        self.__status_code = response.status_code

    def getRef(self):
        return self.__ref

    def geStatusCode(self):
        return self.__status_code

    def getAllLinks(self):
        if (not(isWorking)):
            return False
        html = (response.content).lower()
        hrefList = re.findall(b'href="(.*?)"', html)
        srcList = re.findall(b'src="(.*?)"', html)
        return (convertRelativeToAbsolute(hrefList + srcList))

    def convertRelativeToAbsolute(self, linksList):
        for i in range(len(linksList)):
            if (not(linksList[i].startwith('http'))):
                linksList[i] = urllib.parse.urljoin(self.__ref, linksList[i])
        return linksList

    def __eq__(self, other):
        return (self.getRef() == other.getRef())

    def __ne__(self, other):
        return (self.getRef() != other.getRef())

    def isWorking(self):
        return (not(self.__status_code) or (100 <= self.__status_code <= 301))

