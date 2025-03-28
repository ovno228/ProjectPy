# зв'язок классів
# class Human:
#     count=0
#     def __init__(self,name="Vasya"):
#         self.name = name
#         Human.count+=1
#
#
# class Auto:
#     def __init__(self,brand):
#         self.brand=brand
#         self.passenger=[]
#     def add(self,*args):  #необмежена кількість пасажирів/аргументів
#         self.passenger.append(pas)
#     def info(self):
#         if self.passenger==[]:
#             print('Пасажири відсутні у', self.brand)
#         else:
#             print('Пасажири присутні у', self.brand,":")
#             for n in self.passenger:
#                 print(n.name)
#
#
# pas1=Human()
# car1=Auto("Богдан")
# car1.add(pas1)
# car1.info()
#
# НАСПАДКУВАННЯ КЛАСІВ
#
# class Human:
#     def __init__(self,name,age,height,city,animal):
#         self.name=name
#         self.age=age
#         self.height=height
#         self.city=city
#         self.animal=animal
#     def info(self):
#         return 'Вітаю! Я' + self.name+ 'мені' +self.age+' років. Я з міста' +self.city+' Мій зріст'+self.height+'я маю тварин:'+self.animal
# class Pupil(Human):
#     def __init__(self,name,age,height,city,animal,school,clas):
#         super().__init__(name,age,height,city,animal)
#         self.school=school
#         self.clas=clas
#     def __str__(self):
#         return super().__str__()+'Навчаюсь у школ'+str(self.school)+'у'+str(self.clas)+'класі'
# class Worker(Human):
#     def __init__(self,name,age,height,city,animal,job,salary):
#         super().__init__(name, age, height, city, animal)
#         self.job=job
#         self.salary=salary
#     def __str__(self):
#         return super().__str__()+'Працюю на посаді '+self.job+' маю зп '+ str(self.salary)+'$'
#
# h=Human('Маша',12,156,'Запоріжжя','кіт')
# p=Pup=Pupil('Олег',14,170,'Дніпро','Папуга',101,9)
# w=Worker('Яна',35,168,'Львів','немає','дизайнер',3500)
# print(str(h))
# print(p)
# print(w)
# print(h)


class PC:
    def __init__(self,model="HP"):
        super().__init__()
        self.model=model
        self.memory=256
class Display:
    def __init__(self):
        self.res='4k'
class Smart(PC,Display):
    def info(selfself):
        print('Смартфон моделі',self.model,"маж об'єм пам'яти",self.memory,"мб та розширення екрана", self.res)

    tel=Smart('Samsung')
    tel.info()