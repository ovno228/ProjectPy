# class Animal:
#     def sound(self):
#         pass #пустий код
# class Dog(Animal):
#     def sound(self):
#         return "МЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯУУУونلىسلىولاز"
# class Cat(Animal):
#     def sound(self):
#         return "Гав!"
# class Cow(Animal):
#     def sound(self):
#         return "Мууу"
#
# def speak(an):
#     print(an.sound())
# a1=Dog()
# a2=Cat()
# a3=Cow()
# speak(a1)
# speak(a2)
# speak(a3)


# class Pay:
#     def process(self, money):
#         pass
# class Credit(Pay):
#     def process(self, money):
#         return "Оплата "+str(money)+ "грн здійснена через кредитну карту"
# class Cash(Pay):
#     def process(self, money):
#         return "Оплата "+str(money)+ "грн здійснена через готівку"
# class System(Pay):
#     def process(self, money):
#         return "Оплата "+str(money)+ "грн здійснена через онлайн систему"
# buy=[Credit(),Cash(),System()]
# num=init(input('Введіть суму покупки:'))
# for k in buy:
#     print(k.process(num))


# # Інкапсюляція
# class Dog:
#     def __init__(self,name):
#         self.name=name
# dog1=Dog('Бані')
# print(dog1.name)

# #2) private
# class Dog:
#     def __init__(self,name):
#         self.name=name
#         self.__age=2
#     def info(self):
#         return self.__age
# dog1=Dog('Бані')
# print(dog1.info())
#
# #3) protected
# class Dog:
#     def __init__(self,name):
#         self._breed='бульдог'
# class D (Dog):
#     def info(self):
#         return "Це щеня породі"+self._breed
#
# dog1=D("Бані")
# perint(dog1.info())



# class Person:
#     def __init__(self,name,age,salary):
#         self.name=name #публічний атрибут
#         self._age=age #захищений
#         self.__salary=salary #приватний
#     def info(self):
#         print("Вітаю. Мене звати",self.name)
#         self._infoAge()
#         self.__infoSalary()
#     def _infoAge(self):
#         print('Мій вік',self._age)
#     def __infoSalary(self):
#         print('Моя ЗП', self.__salary)
# class Employee(Person):
#     def __init__(self,name,age,salary,pos):
#         super().__init__(name,age,salary)
#         self.pos=pos
#     def printInfo(self):
#             print('Моя посада', self.pos)
#             print('Мій вік', self._age)
#             # print('Моя ЗП', self.__salary)
# human=Person('Олеся',20,20000)
# emp=Employee('Петро',25,45000,'інженер')
# print(human.name)
# human.info()
# print(emp.name)
# emp.printInfo()
# # print(emp.__salary)
# print(emp._Person__salary)


import random as r
class Character:
    def __init__(self,name,health):
        self.__name=name
        self.__health=50
    def infoName(self):
        return self.__name
    def infoHP(self):
        return self.__health
    def attack(self):
        self.attack = 30
    def takedamage(self):
        self.__leath-=r.randit(0,10)
    def is_alive(self):
        return self.__health
    def __str__(self):
        return self.name+": моє здоровья "+str(self.__health)
class Player:
    def __init__(self,name,health,clas):
        super().__init__(name,health)
    def clas(self):
        self._clas=randit(0,3)
        if clas == 1:
            self._clas == 'Маг'
        else:
            self._clas == 'Воїн'
