""" ООП - обьектно ориентированное програмирование """


# hello_geeks = "Geeks" # змениный регистр

# HelloGeeks = "Geeks" # Верблюжий регистр

# def car():
#     pass

class Car: # шаблон или чертеж
    def __init__(self, motor, wheel, body): # __init__ - это конструктор
        self.motor = motor # self - ссылка на текущий обьект
        self.wheel = wheel # атрибут класса
        self.body = body
        self.bak = 20
        self.is_start = False # флажок для активации
   
    def info(self): # функция внутри класса превращяются в метод
        print(f"Мотор - {self.motor} колесо - {self.wheel} Кузов - {self.body}")

    def start(self):
        if self.bak > 0:
            self.is_start = True
            print("Машина заведена")
        else:
            print("У машины нет топлива")

    def stop(self):
        self.is_start = False
        print("Машина заглушена")

    def drive(self, city):
        if self.is_start == True:
            print(f"Машина едет в {city}")
        else:
            print("Машина не заведена")

car = Car("V6", "R20", "Khan") # экземпляр класса
car.info()
car.start()
car.drive("Dubai")

# name = ("Asko", "Isko", "Sema")
# my_list = list(name)
# my_list.append("Aslan")
# name = tuple(my_list)
# print(name)

""" Создать класс (book). Передать параметры (avtor, book_name, year). Создать метод инфо. 
ВЫзвать переданный аргумент."""

# class Book:
#     def __init__(self, avtor, book_name, year):
#         self.avtor = avtor 
#         self.book_name = book_name 
#         self.year = year
#     def info(self): 
#         print(f"Автор: {self.avtor}, Название книги: {self.book_name}, Год: {self.year}.")
# Book = Book("Кинг", "R20", "2008")
# Book.info()