# class Animal:
#     def __init__(self, name="Animal"):
#         self.name = name
#         self.age = 0
#
#
# class Cat:
#     def __init__(self):
#         self.breed = "Unknown"
#
#
# class Pet(Animal, Cat):
#     def __init__(self, name, age, breed):
#         Animal.__init__(self, name)
#         Cat.__init__(self)
#         self.age = age
#         self.breed = breed
#
#     def info(self):
#         print(f"Це {self.name}. Йому {self.age} років і він породи {self.breed}.")
#
#
# my_pet = Pet("Барсик", 3, "шатланський веслоухий")
#
# my_pet.info()

# ЗАДАНИЕ 2

class ТранспортнийЗасіб:
    def __init__(self, швидкість=0):
        self.швидкість = швидкість

class Колесо:
    def __init__(self):
        self.тип = 'Колесо(ну, колесо, чого не зрозумілого?)'

class Автомобіль(ТранспортнийЗасіб, Колесо):
    def __init__(self, марка, швидкість):
        ТранспортнийЗасіб.__init__(self, швидкість)
        Колесо.__init__(self)
        self.марка = марка

    def info(self):
        print(f"Автомобіль {self.марка} має швидкість {self.швидкість} км/год і тип колеса: {self.тип}")

авто = Автомобіль("BMW", 120)

авто.info()
