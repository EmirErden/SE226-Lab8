from abc import ABC

class Count(ABC):
    def __init__(self, address):
        self.address = address

    def calculateFreqs(self, address):
        pass

class ListCount(Count):
    def __init__(self, address):
        Count.__init__(self, address)

    def calculateFreqs(self, address):
        file = open(address)
        list = file.readline().split()
        words = []

        for i in list:
            if i not in words:
                words.append(i)
        for a in range(0, len(words)):
            print(words[a], "=", list.count(words[a]))


class DictCount(Count):
    def __init__(self, address):
        Count.__init__(self, address)

    def calculateFreqs(self, address):
        file = open(address)
        list = file.readline()
        wordDict = {}
        for word in list.split():
            wordDict[word] = wordDict.get(word, 0) + 1
        for key in wordDict:
            print("{} : {}".format(key, wordDict[key]))


txtFile = "strange.txt"
list = ListCount(txtFile)
list.calculateFreqs(txtFile)

dictionary = DictCount(txtFile)
dictionary.calculateFreqs(txtFile)
