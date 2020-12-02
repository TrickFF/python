# часть 2
class Auto:
    def __init__(self, year):
        self.year = year

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if year < 2000:
            self.__year = 2000
        elif year > 2019:
            self.__year = 2019
        else:
            self.__year = year

    def get_auto_year(self):
        return f'Автомобиль выпущен в {str(self.year)} году'

a = Auto(2010)
print(a.get_auto_year())



exit()
# часть 1
class MyClass:
    def __init__(self, param_1, param_2):
        self.param_1 = param_1
        self.param_2 = param_2

    @property # делает методы атрибутами с вызовом без скобок
    def my_method(self):
        return f'Параметры, переданные в класс:' \
               f'{self.param_1}, {self.param_2}'

mc = MyClass('text_1', 'text_2')
# print(mc.param_1)
# print(mc.param_2)

print(mc.my_method)
