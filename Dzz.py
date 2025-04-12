# шаблон
import requests #запит
from bs4 import BeatifulSoup as bs


class Name:
    def __init__(self):
        self.url=url
        self.headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        self.soup=None
    def auditSite(self):
        response= requests.get(self.url,headers=self.header)
        if response.status_code==200:
            self.soup=bs(response.text,"html.parser")
        else:
            print("Не вдалося підключитися до сайту")
    def getInfo(self):
        pass
    def showInfo(self):
        pass
url="посилання"
obj=Name(url)
obj.uaditSite()
obj.getInfo()
site=obj.getInfo()
if site:
    obj.showInfo()
else:
    print("Жодної інформації не отримано")