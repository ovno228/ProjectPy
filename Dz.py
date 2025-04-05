# # ЗАДАНИЕ 1
#
# class Character:
#     def __init__(self, name, health):
#         self.__name = name
#         self.__health = max(0, health)
#
#     def attack(self):
#         raise NotImplementedError("Метод attack() має бути реалізований у підкласі")
#
#     def take_damage(self, amount):
#         self.__health = max(0, self.__health - amount)
#
#     def is_alive(self):
#         return self.__health > 0
#
#     def get_name(self):
#         return self.__name
#
#     def get_health(self):
#         return self.__health
#
#
# class Warrior(Character):
#     def __init__(self, name):
#         super().__init__(name, health=150)
#
#     def attack(self):
#         return f"{self.get_name()} атакує мечем!"
#
#
# class Mage(Character):
#     def __init__(self, name):
#         super().__init__(name, health=80)
#     def attack(self):
#         return f"{self.get_name()} атакує магією!"
#
#
# characters = [Warrior("Артур"), Mage("Мерлін")]
#
# for char in characters:
#     print(char.attack())
#     char.take_damage(30)
#     print(f"{char.get_name()} живий: {char.is_alive()}, здоров'я: {char.get_health()}")

# ЗАДАНИЕ 2

class LibraryItem:
    def __init__(self, title, author, item_id):
        self.__title = title
        self.__author = author
        self.__item_id = item_id
        self.__is_checked_out = False

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_item_id(self):
        return self.__item_id

    def is_same_item(self, other):
        return self.__item_id == other.get_item_id()

    def check_out(self):
        if not self.__is_checked_out:
            self.__is_checked_out = True
            return f"Матеріал '{self.__title}' видано."
        return f"Матеріал '{self.__title}' вже видано."

    def return_item(self):
        if self.__is_checked_out:
            self.__is_checked_out = False
            return f"Матеріал '{self.__title}' повернено."
        return f"Матеріал '{self.__title}' вже знаходиться в бібліотеці."

    def display_info(self):
        raise NotImplementedError("Цей метод повинен бути реалізований у підкласі")


class Book(LibraryItem):
    def __init__(self, title, author, item_id, pages):
        super().__init__(title, author, item_id)
        self.__pages = pages

    def display_info(self):
        print(f"Книга: {self.get_title()}, Автор: {self.get_author()}, Сторінки: {self.__pages}")


class Magazine(LibraryItem):
    def __init__(self, title, author, item_id, issue_number):
        super().__init__(title, author, item_id)
        self.__issue_number = issue_number

    def display_info(self):
        print(f"Журнал: {self.get_title()}, Автор: {self.get_author()}, Номер випуску: {self.__issue_number}")


class Audiobook(LibraryItem):
    def __init__(self, title, author, item_id, duration):
        super().__init__(title, author, item_id)
        self.__duration = duration

    def display_info(self):
        print(f"Аудіокнига: {self.get_title()}, Автор: {self.get_author()}, Тривалість: {self.__duration} хвилин")


items = [
    Book("Майстер і Маргарита", "М. Булгаков", 1, 320),
    Magazine("Наука і життя", "Редакція", 2, 5),
    Audiobook("1984", "Дж. Орвелл", 3, 640)
]

for item in items:
    item.display_info()
    print(item.check_out())
    print(item.return_item())

