import requests
from bs4 import BeautifulSoup as bs

class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price
        self.__id = hash(name)

    def __str__(self):
        return f"{self.name} — ${self._price:.2f}"

    def __bool__(self):
        return self.name != "" and self._price > 0

    def __len__(self):
        return len(self.name)

    def get_price(self):
        return self._price

class CoinParser:
    def __init__(self, url):
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        self.soup = None
        self.products = []

    def auditSite(self):
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            self.soup = bs(response.text, "html.parser")
        else:
            print("Не вдалося підключитися до сайту")

    def getInfo(self):
        table = self.soup.find('tbody')
        if not table:
            print("Не знайдено таблицю на сторінці")
            return False

        rows = table.find_all('tr')[:10]
        for row in rows:
            name_tag = row.find('a', class_='tw-hidden lg:tw-flex font-bold tw-items-center tw-justify-between')
            price_tag = row.find('span', class_='no-wrap')

            if name_tag and price_tag:
                try:
                    name = name_tag.text.strip()
                    price = float(price_tag.text.replace('$', '').replace(',', '').strip())
                    prod = Product(name, price)
                    if prod:
                        self.products.append(prod)
                except:
                    continue
        return True if self.products else False

    def showInfo(self):
        print("\nТОП-10 криптовалют:")
        print("-" * 40)
        for i, p in enumerate(self.products, 1):
            print(f"{i}. {p}")

    def buyProduct(self):
        try:
            choice = int(input("Оберіть номер монети для покупки (1-10): "))
            if 1 <= choice <= len(self.products):
                qty = float(input("Скільки монет бажаєте купити?: "))
                prod = self.products[choice - 1]
                total = prod.get_price() * qty
                print(f"💰 Ви вибрали {qty} {prod.name}. Загальна вартість: ${total:.2f}")
            else:
                print("❗ Невірний номер")
        except ValueError:
            print("❗ Введіть число")

# --- Основна логіка за шаблоном ---

url = "https://www.coingecko.com/"
obj = CoinParser(url)
obj.auditSite()
site = obj.getInfo()

print('5 найпопулярніші криптомонети:')
if site:
    obj.showInfo()
    obj.buyProduct()
else:
    print("Жодної інформації не отримано")
