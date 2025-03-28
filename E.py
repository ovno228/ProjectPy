# # ЗАДАНИЕ 1
# class Product:
#     count = 0
#
#     def __init__(self, name, price, stock):
#         self.name = name
#         self.price = price
#         self.stock = stock
#         Product.count += 1
#
#     def is_available(self, quantity):
#         return self.stock >= quantity
#
#     def reduce_stock(self, quantity):
#         if self.is_available(quantity):
#             self.stock -= quantity
#             return True
#         return False
#
#     def add_stock(self, quantity):
#         self.stock += quantity
#
#
# class Cart:
#     def __init__(self):
#         self.items = {}
#
#     def add_product(self, product, quantity):
#         if product.is_available(quantity):
#             if product.name in self.items:
#                 self.items[product.name]['quantity'] += quantity
#             else:
#                 self.items[product.name] = {'product': product, 'quantity': quantity}
#             product.reduce_stock(quantity)
#             print(f"Добавлено {quantity} единиц {product.name} в корзину.")
#         else:
#             print(f"Недостаточно товара {product.name} на складе.")
#
#     def remove_product(self, product_name):
#         if product_name in self.items:
#             product = self.items[product_name]['product']
#             quantity = self.items[product_name]['quantity']
#             product.add_stock(quantity)  # Возвращаем товар на склад
#             del self.items[product_name]
#             print(f"Удалено {product_name} из корзины.")
#         else:
#             print("Такого товара нет в корзине.")
#
#     def view_cart(self):
#         if not self.items:
#             print("Ваша корзина пуста.")
#         else:
#             print("Содержимое корзины:")
#             for item in self.items.values():
#                 print(f"{item['product'].name} - {item['quantity']} шт.")
#             print(f"Общая сумма: ${self.total_cost()}")
#
#     def total_cost(self):
#         return sum(item['product'].price * item['quantity'] for item in self.items.values())
#
#
# # Создание товаров
# products = [
#     Product("Телефон", 500, 10),
#     Product("Ноутбук", 1000, 5),
#     Product("Наушники", 100, 15),
#     Product("Часы", 200, 7),
#     Product("Планшет", 600, 4),
#     Product("Клавиатура", 50, 20),
#     Product("Мышь", 40, 25),
#     Product("Монитор", 300, 6),
#     Product("Колонка", 150, 10)
# ]
#
# # Игровой процесс
# player_balance = 2000
# cart = Cart()
#
#
# def show_shop():
#     print("Добро пожаловать в магазин!")
#     print("Выберите товар для покупки или введите 0 для выхода:")
#     for i, product in enumerate(products, 1):
#         print(f"{i}. {product.name} - ${product.price} (В наличии: {product.stock})")
#     print("0. Выйти из магазина")
#
#
# def main():
#     global player_balance
#     while True:
#         print(f"Ваш баланс: ${player_balance}")
#         choice = input(
#             "Введите 1, чтобы посмотреть магазин, 2, чтобы посмотреть корзину, 3, чтобы удалить товар из корзины: ")
#         if choice == "1":
#             while True:
#                 show_shop()
#                 choice = input("Выберите товар (0 для выхода): ")
#                 if choice == "0":
#                     break
#                 if choice.isdigit() and 1 <= int(choice) <= len(products):
#                     product = products[int(choice) - 1]
#                     quantity = int(input(f"Сколько {product.name} вы хотите купить? "))
#                     total_price = product.price * quantity
#                     if total_price <= player_balance and product.is_available(quantity):
#                         player_balance -= total_price
#                         cart.add_product(product, quantity)
#                         print(f"Вы купили {quantity} {product.name}. Осталось ${player_balance}.")
#                     else:
#                         print("Недостаточно средств или товара.")
#                 else:
#                     print("Неверный ввод.")
#         elif choice == "2":
#             cart.view_cart()
#         elif choice == "3":
#             cart.view_cart()
#             product_name = input("Введите название товара, который хотите удалить: ")
#             cart.remove_product(product_name)
#         else:
#             print("Неверный ввод.")
#
#
# main()

# ЗАДАНИЕ 2

class BankAccount:
    def __init__(self, owner_name, account_number, balance=0):
        self.owner_name = owner_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        """Поповнення рахунку"""
        if amount > 0:
            self.balance += amount
            print(f"Внесено ${amount}. Тепер на рахунку {self.balance}.")
        else:
            print("Сума поповнення повинна бути більше нуля.")

    def withdraw(self, amount):
        """Зняття коштів"""
        if amount <= self.balance:
            self.balance -= amount
            print(f"Знято ${amount}. Залишок на рахунку {self.balance}.")
        else:
            print("Недостатньо коштів для зняття.")

    def get_balance(self):
        """Перегляд балансу"""
        return self.balance

    def __str__(self):
        return f"Власник: {self.owner_name}, Номер рахунку: {self.account_number}, Баланс: ${self.balance}"


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, owner_name, account_number):
        "Створення нового рахунку"
        if account_number not in self.accounts:
            self.accounts[account_number] = BankAccount(owner_name, account_number)
            print(f"Рахунок для {owner_name} створено.")
        else:
            print("Рахунок з таким номером вже існує.")

    def get_account(self, account_number):
        "Отримати рахунок по номеру"
        return self.accounts.get(account_number, None)

    def transfer(self, from_account_number, to_account_number, amount):
        "Переказ коштів між рахунками"
        from_account = self.get_account(from_account_number)
        to_account = self.get_account(to_account_number)

        if from_account and to_account:
            if from_account.get_balance() >= amount:
                from_account.withdraw(amount)
                to_account.deposit(amount)
                print(f"Переказано ${amount} з рахунку {from_account_number} на рахунок {to_account_number}.")
            else:
                print("Недостатньо коштів для переказу.")
        else:
            print("Один або обидва рахунки не існують.")



def main():
    bank = Bank()

    bank.create_account("Іван Іванов4321", "4321")
    bank.create_account("Петро Петренко1234", "1234")

    while True:
        print("\nМеню:")
        print("1. Поповнити рахунок")
        print("2. Зняти кошти з рахунку")
        print("3. Переказати кошти між рахунками")
        print("4. Переглянути баланс")
        print("5. Вийти")

        choice = input("Виберіть опцію: ")

        if choice == "1":
            account_number = input("Введіть номер рахунку для поповнення: ")
            amount = float(input("Введіть суму для поповнення: "))
            account = bank.get_account(account_number)
            if account:
                account.deposit(amount)
            else:
                print("Рахунок не знайдений.")

        elif choice == "2":
            account_number = input("Введіть номер рахунку для зняття: ")
            amount = float(input("Введіть суму для зняття: "))
            account = bank.get_account(account_number)
            if account:
                account.withdraw(amount)
            else:
                print("Рахунок не знайдений.")

        elif choice == "3":
            from_account_number = input("Введіть номер рахунку для переказу з: ")
            to_account_number = input("Введіть номер рахунку для переказу на: ")
            amount = float(input("Введіть суму для переказу: "))
            bank.transfer(from_account_number, to_account_number, amount)

        elif choice == "4":
            account_number = input("Введіть номер рахунку для перевірки балансу: ")
            account = bank.get_account(account_number)
            if account:
                print(f"Баланс рахунку {account_number}: ${account.get_balance()}")
            else:
                print("Рахунок не знайдений.")

        elif choice == "5":
            print("До побачення!")
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
