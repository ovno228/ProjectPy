# !!!!!!! Я НЕ МОГУ ПРОВЕРИТЬ РАБОТАЕТ ЛИ КОД, У МЕНЯ НЕ РАБОТАЕТ МОДУЛЬ ЧТО БЫ ЕГО ПРОВЕРИТЬ!!!!
# !!!!!!! КОГДА Я ПЫТАЮСЬ ЗАПУСТИТЬ КОД ВЫДАЁТ СЛЕДУЮЩУЮ ОШИБКУ:
# Traceback (most recent call last):
#   File "C:\Users\Ростислав\PycharmProjects\pythonProject2\Dzzz.py", line 67, in <module>
#     import requests
# ModuleNotFoundError: No module named 'requests'








# ЗАДАНИЕ 1
# import requests
# from bs4 import BeautifulSoup as bs
#
# class Books:
#     def __init__(self, url):
#         self.url = url
#         self.headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
#         }
#         self.soup = None
#         self.data = []
#
#     def auditSite(self):
#         response = requests.get(self.url, headers=self.headers)
#         if response.status_code == 200:
#             self.soup = bs(response.text, "html.parser")
#         else:
#             print("Не вдалося підключитися до сайту")
#
#     def getInfo(self):
#         books = self.soup.find_all('article', class_='product_pod')
#         if not books:
#             print("Помилка в пошуку сторінки")
#             return False
#
#         for book in books[:8]:
#             name = book.h3.a['title']
#             price = book.find('p', class_='price_color').text.strip()
#             rating = book.p['class'][1] if len(book.p['class']) > 1 else 'No rating'
#             self.data.append({'Назва': name, 'Ціна': price, 'Рейтинг': rating})
#         return True
#
#     def showInfo(self):
#         print('№\t', 'НАЗВА', '\t' * 3, 'ЦІНА', '\t', 'РЕЙТИНГ')
#         print('-' * 80)
#         i = 1
#         for item in self.data:
#             print(f"{i}\t{item['Назва'][:30]:30} {item['Ціна']:10} {item['Рейтинг']}")
#             i += 1
#
# url = "http://books.toscrape.com"
# obj = Books(url)
# obj.auditSite()
# site = obj.getInfo()
# if site:
#     obj.showInfo()
# else:
#     print("Жодної інформації не отримано")

# ЗАДАНИЕ 2

import requests
from bs4 import BeautifulSoup as bs

class CoinInfo:
    def __init__(self, url):
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        self.soup = None
        self.data = []

    def auditSite(self):
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            self.soup = bs(response.text, "html.parser")
        else:
            print("Не вдалося підключитися до сайту")

    def getInfo(self):
        coins = self.soup.select('table tbody tr')
        if not coins:
            print("Помилка в пошуку сторінки")
            return False

        for row in coins[:8]:
            name = row.select_one('td:nth-child(3) a')
            price = row.select_one('td:nth-child(4)')
            if name and price:
                self.data.append({'Назва': name.text.strip(), 'Ціна': price.text.strip()})
        return True

    def showInfo(self):
        print('№\t', 'НАЗВА', '\t' * 3, 'ЦІНА')
        print('-' * 60)
        i = 1
        for item in self.data:
            print(f"{i}\t{item['Назва'][:20]:20} {item['Ціна']}")
            i += 1

url = "https://www.coingecko.com/"
obj = CoinInfo(url)
obj.auditSite()
site = obj.getInfo()
if site:
    obj.showInfo()
else:
    print("Жодної інформації не отримано")