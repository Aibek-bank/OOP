""" OOП 2: Другие принципы ООП - Инкапсуляция (Защита данных) """

""" 3 состояния:    1) публичная
                    2) защищенный
                    3) приватный

"""
"""
class PublicExaple: # публичный класс
    def __init__(self, value):
        self.value = value #публичный атрибут

    def info(self):
        return self.value # публичный метод
    
public = PublicExaple(23)
print(public.info()) # вызов публичного метода
print(public.value) # доступ к публичному атрибуту
"""

class ProtectedExample: # Защищенный класс
    def __init__(self, value):
        self._value = value #Зашищенный атрибут

    def _info(self):
        return self._value # защищенный метод
    
# protected = ProtectedExample(43)
# print(protected._info()) # это работает но противоречит принципам инкапсуляции
# print(protected._value) # это тоже работает, можно получить значение напрямую, но это не рекомендуется

class PrivateExample: # Приватный класс
    def __init__(self, value):
        self.__value = value # приватный атрибут
    
    def __info(self): # приватный метод
        return self.__value
    def access_private(self):
        return self.__info()
    
private = PrivateExample(12)
print(private.__info()) #прямой вызов приватного метода вызовет ошибку
print(private.__value) #прямой вызов приватного атрибута вызовет ошибку
print(private.access_private()) # доступ через публичный метод
print(private._PrivateExample__info()) # доступ к приватному атрибуту либо методу через name mangling

# import datetime

# class Car:
#     def __init__(self, marka, model, year, mileage):
#         self.marka = marka
#         self.model = model
#         self.year = year
#         self.mileage = mileage

#     def info(self):
#         return f'Марка - {self.marka}\nМодель - {self.model}'
    
#     def _calculate_age(self):
#         current = datetime.datetime.now().year
#         return f'Возраст машины - {current - self.year}'
        
#     def __update_mileage(self, mileage_update = 1000):
#         self.__mileage = mileage_update
#         return self.__mileage
    
#     def set_mileage(self):
#         return self.__update_mileage
    
# car = Car("Mazda", "Demio", 2008, 140000)

# print(car.info())  
# print(f'Возраст машины - {car._calculate_age()} лет')
# print(f'Обновленный пробег - {car.__update_mileage()} км')


        
