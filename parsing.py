# # шаблон
# import requests #запит
# from bs4 import BeatifulSoup as bs
#
#
# class Name:
#     def __init__(self):
#         self.url=url
#         self.headers={
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
#         }
#         self.soup=None
#     def auditSite(self):
#         response= requests.get(self.url,headers=self.header)
#         if response.status_code==200:
#             self.soup=bs(response.text,"html.parser")
#         else:
#             print("Не вдалося підключитися до сайту")
#     def getInfo(self):
#         pass
#     def showInfo(self):
#         pass
# url="посилання"
# obj=Name(url)
# obj.uaditSite()
# obj.getInfo()
# site=obj.getInfo()
# if site:
#     obj.showInfo()
# else:
#     print("Жодної інформації не отримано")

# # шаблон
# import requests #запит
# from bs4 import BeatifulSoup as bs
#
#
# class Comfy:
#     def __init__(self):
#         self.url=url
#         self.headers={
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
#         }
#         self.soup=None
#     def auditSite(self):
#         response= requests.get(self.url,headers=self.header)
#         if response.status_code==200:
#             self.soup=bs(response.text,"html.parser")
#         else:
#             print("Не вдалося підключитися до сайту")
#             return
#     def getInfo(self):
#         laptop=[]
#         lap=self.soup.find_all('div',class_='products-catalog')
#         if not lap:
#             print('Помилка в пошуку сторінки')
#             return
#         for i in laptop[0:4]:
#             name=i.find('a', class_='prdl-item__name ellipsis-2-lines')
#             nameErorr=name.text() if name else 'Відсутня назва'
#             price=i.find('iv', class_='products-list-item-price__actions-price-current')
#             priceErorr = price.text() if price else 'Відсутня ціна'
#             laptop.append(
#                 {
#                     'Назва':name
#                     'Ціна':price
#                 }
#             )
#             return laptop
#
#
#     def showInfo(self):
#         print('№\t','НАЗВА','\t'*2,'ЦІНА','\t'*2)
# url="https://comfy.ua/ua/black-friday/cat__120/?gad_source=1&gclid=Cj0KCQiAkJO8BhCGARIsAMkswyhJ-lMrSryvvEIyf_s3FPnjgF7ydctFE_R10Yj_zj9l231aRd-ZIeAaAmjrEALw_wcB"
# obj=Name(url)
# obj.uaditSite()
# obj.getInfo()
# site=obj.getInfo()
# if site:
#     obj.showInfo()
# else:
#     print("Жодної інформації не отримано")


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
        coins=[]
        listCoin=self.soup.find('tbody')
        if not listCoin:
            print('Помилка в пошуку на сторінці')
            return coins
        info=listCoin.find_all('tr')[0:5]
        for i in info:
            name=i.find('p',class_='coin-item-name')
            name2=name.text.strip() if name else 'Відсутня назва'
            price = i.find('p', class_='sc-142c02c-0 lmjbLF')
            price2 = name.text.strip() if name else 'Відсутня ціна'
    def showInfo(self):
        print('№\t', 'НАЗВА', '\t' * 2, 'ЦІНА', '\t' * 2)
        print('-'*50)
        for i in coins:
            print('\t',i[`Назва],'')
url="https://coinmarketcap.com/"
obj=Coin(url)
obj.uaditSite()
obj.getInfo()
site=obj.getInfo(site)
print('5 найпопулярніші криптомонети')
if site:
    obj.showInfo()
else:
    print("Жодної інформації не отримано")
