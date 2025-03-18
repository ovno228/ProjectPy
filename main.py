#class Car:
#    speed=110
#    def __init__(self):
#        self.speed=speed_car
#    def info(selfself):
#        print("Швидкість авто", self.speed)
#    sp=int(input('максимальна швидкість авто:'))

# print("Швидкість авто", auto.speed)
# auto=Car
# auto.info
# auto1=Car(180)
# auto2.info()

# class Pupils:
#     def __init__(self,height,name):
#         self.name=name
#         self.height=height
#     def show(self):
#         print("Ім'я учасника:", self.name, "Зріст:", self.height)
#     def __bool__(self):
#         return self.name!=None
#     def __len__(self):
#         return self.height
#
# p1=Pupils("Ігор", 155)
# p1.__str__()
# p2=Pupils("Оля", 158)
# p2.__str__()
# p3=Pupils("Петро", 162)
# p3.__str__()
# # print(p1.count, "учасника змагань")
# # print(p1.__bool__())
# print(bool(p2))

# import random as r
# class Student:
#     def __init__(self):
#         self.name=name
#         self.happy=r.randint(a:10, B:100)
#         self.progress=r.randint(a:0, b:10)
#         self.alive=True
#     def study(self):
#         print('Час для навчання')
#         self.happy-=r.randit(a:1,b:10)
#     def sleep(self):
#         print('Час для сну')
#         self.happy += r.randint(a:1,b:10)
#     def chill(self):
#         print('Час для відпочинку')
#         self.happy += r.randit(a:50,b:100)
#     def isAlive(self):
#         if 1<self.progress<5:
#             print('Ти на грані відрахування з інституту. Починай навчатися')
#             self.alive=False
#         elif self.progress <=1:
#             print('Відрахування з інституту')
#             self.alive = False
#         elif self.progress >=5
#             print('Відмінно навчаєшся')
#             self.alive = False
#     def everyday(self):
#         print("Рівень щастя", self.happy)
#         print("Прогрес навчання", self.progress
#     def studyLife(self, day):
#             day="День №"+str(day)
#             print(day)
#             res=r, rendint(a:1,b:3)
#             if res==1:
#                 self.study()
#             elif res==2:
#                 self.chill()
#             else:
#                 self.sleep()
#             self.everyday()
#             self.asAlive
# st1=Student('Олег')
# # print(st1.name)
# print("Життя студента", st1.name)
# for k in range(7):
#     if st1.alive==False
#         break
#     st1.studyLife(k)




# симулятор студента

import random as r


class Student:
    def __init__(self, name, initial_money, initial_happy, initial_progress, difficulty, sandbox, days, fears_women):
        self.name = name
        self.happy = initial_happy if sandbox else r.randint(10, 100)
        self.progress = initial_progress if sandbox else r.randint(0, 10)
        self.money = initial_money
        self.alive = True
        self.difficulty = difficulty
        self.sandbox = sandbox
        self.days = float('inf') if difficulty == "бесконечний" else days
        self.fears_women = fears_women
        self.has_calculator = False

        if not sandbox:
            if difficulty == "легкий":
                self.money *= 1.5
                self.happy += 20
            elif difficulty == "складний":
                self.money *= 0.5
                self.happy -= 20

    def study(self):
        print('Час для навчання')
        self.happy -= r.randint(5, 10)
        progress_gain = r.randint(1, 3)

        if r.randint(1, 2) == 1:
            print("👩 Однокласниця сіла поруч!")
            if self.fears_women:
                print("😨 Ви боїтеся жінок! Ваш прогрес зменшується.")
                progress_gain *= 0.5

        self.progress += progress_gain

    def sleep(self):
        print('Час для сну')
        self.happy += r.randint(5, 15)

    def chill(self):
        print('Час для відпочинку')
        if self.money >= 20:
            self.happy += r.randint(10, 30)
            self.money -= 20
        else:
            print("Недостатньо грошей для відпочинку!")

    def work(self):
        print('Час для роботи')
        self.money += r.randint(20, 50)
        self.happy -= r.randint(5, 15)
        progress_penalty = {"легкий": 1, "нормальний": 2, "складний": 3}.get(self.difficulty, 2)
        self.progress -= r.randint(0, progress_penalty)

    def shop(self):
        print("Ви зайшли в магазин. Що бажаєте купити?")
        print("1. Лотерейний білет (5 грошей, шанс виграти 500 грошей - 5%)")
        print("2. Калькулятор (50 грошей, знижує вимоги на іспиті на 1, купується один раз)")
        print("3. Вийти з магазину")

        choice = input("Ваш вибір: ")
        if choice == "1" and self.money >= 5:
            self.money -= 5
            if r.randint(1, 100) <= 5:
                print("🎉 Ви виграли 500 грошей у лотерею!")
                self.money += 500
            else:
                print("😢 Ви нічого не виграли.")
        elif choice == "2" and self.money >= 50 and not self.has_calculator:
            self.money -= 50
            self.has_calculator = True
            print("✅ Ви купили калькулятор! Він допоможе вам на іспитах.")
        elif choice == "2" and self.has_calculator:
            print("⚠️ Ви вже купили калькулятор!")
        elif choice == "3":
            print("Ви вийшли з магазину.")
        else:
            print("Недостатньо грошей!")

    def after_classes(self):
        print("Пари закінчились! Куди підеш?")
        print("1. Магазин")
        print("2. Додому спати")
        choice = input("Ваш вибір: ")
        if choice == "1":
            self.shop()
        elif choice == "2":
            self.sleep()

    def isAlive(self):
        progress_threshold = {"легкий": 15, "нормальний": 10, "складний": 8}.get(self.difficulty, 10)
        if self.progress < 2:
            print('Відрахування з інституту')
            self.alive = False
        elif self.progress < 5:
            print('Ти на грані відрахування з інституту. Починай навчатися')
        elif self.progress >= progress_threshold:
            print('Відмінно навчаєшся')
            self.alive = False
        if self.money <= 0:
            print('У тебе закінчилися гроші! Треба працювати.')
            self.work()

    def studyLife(self, day):
        print("День №", day)
        if not self.alive:
            return
        res = r.randint(1, 4)
        if res == 1:
            self.study()
        elif res == 2:
            self.chill()
        elif res == 3:
            self.sleep()
        else:
            self.work()
        self.isAlive()
        self.after_classes()


name = input("Введіть ім'я студента: ")
money = int(input("Скільки у вас грошей на старті? (Тільки для песочницы): ")) if input(
    "Грати в песочниці? (так/ні): ").lower() == "так" else 0
happy = int(input("Рівень щастя на старті? (Тільки для песочницы): ")) if money else 0
progress = int(input("Початковий прогрес? (Тільки для песочницы): ")) if money else 0
difficulty = input("Оберіть рівень складності (легкий/нормальний/складний/бесконечний): ")
days = {"легкий": 50, "нормальний": 250, "складний": 500}.get(difficulty, float('inf'))
fears_women = input("Ти боїшся жінок? (1 - так, 2 - ні): ") == "1"

student = Student(name, money, happy, progress, difficulty, bool(money), days, fears_women)
day = 1
while student.alive and day < student.days:
    student.studyLife(day)
    day += 1

print("Гра закінчена!")




# програма для оцінки


# def determine_grade(score):
#     if 0 <= score <= 49:
#         return "Незадовільно"
#     elif 50 <= score <= 69:
#         return "Задовільно"
#     elif 70 <= score <= 89:
#         return "Добре"
#     elif 90 <= score <= 100:
#         return "Відмінно"
#     else:
#         return "Некоректний бал"
#
# try:
#     score = int(input("Введіть кількість балів (0-100): "))
#     print("Оцінка:", determine_grade(score))
# except ValueError:
#     print("Будь ласка, введіть ціле число!")
