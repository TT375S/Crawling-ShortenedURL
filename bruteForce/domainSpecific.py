from abc import ABCMeta, abstractmethod

class baseDomainAgent(metaclass=ABCMeta):
    def __init__(self):
        self.url == "blablabla"
        print("This is base class. DO NOT call or instansiate this class directory.")
    
    @abstractmethod
    def isValid(self, shortURL, destURL, html):
        print("Please implement isValid() method.")
        return False

class owly(baseDomainAgent):
    def __init__(self):
        self.url = "http://ow.ly/"
    
    def isValid(self, shortURL, destURL, html):
        return not shortURL == destURL
        
