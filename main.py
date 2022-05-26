from abc import ABC


class adress(ABC):
    def _init_(self, address):
        self.address = "C:\\Users\\C605\\Desktop\\strange.txt"

    def calculateFreqs(self):
        pass


class ListCount(adress):
    def calculateFreqs(self):
        file = open()
