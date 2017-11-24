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

class bitly(baseDomainAgent):
    def __init__(self):
        self.url = "http://bit.ly/"
    
    def isValid(self, shortURL, destURL, html):
        return  not "does not exist" in html

class tinyurl(baseDomainAgent):
    def __init__(self):
        self.url = "http://tinyurl.com/"
    
    def isValid(self, shortURL, destURL, html):
        return not "Error: Unable to find URL to redirect to." in html

class isgd(baseDomainAgent):
    def __init__(self):
        self.url = "http://is.gd/"
    
    def isValid(self, shortURL, destURL, html):
        return not "The link you followed may be invalid" in html

class tco(baseDomainAgent):
    def __init__(self):
        self.url = "http://t.co/"
    
    def isValid(self, shortURL, destURL, html):
        return not ("このページは存在しません" in html or shortURL == destURL)

class prtnu(baseDomainAgent):
    def __init__(self):
        self.url = "http://prt.nu/"
    
    def isValid(self, shortURL, destURL, html):
        return not "このURLは有効ではありません" in html
