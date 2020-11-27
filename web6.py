class Auto:
    # первыми пишут атрибуты класса. Это глобальные переменные
    # name = 'Lexus'
    # model = 'RX 350L'
    # year = 2020

    # атрибуты объекта
    a_count = 0

    # атрибуты объекта
    def __init__(self, name, model, year):
        self.n = name
        self._m = model # защищенная
        self.__y = year # приавтная
        Auto.a_count += 1
        self.on_start()

    # методы класса
    def on_start(self,):
        speed = 10
        print(f'Go - go! car {self.n} {self._m} with speed {speed}')

    def on_stop(self):
        print('Stop!')

auto_1 = Auto('Mazda', 'Miata', [2020, 2019])
print(auto_1._Auto__y) # доступ к приматным атрибутам
auto_2 = Auto('Lada', 'Granta', 2019)
print(auto_2.a_count)
Auto.on_start(auto_1)
Auto.on_start(auto_2)
# print(auto_1.name)
# auto_1.name = 'Mazda' # изменили имя
# print(auto_1.name)
# print(auto_2.name) # но для второго объекта имя не изменилось, т.к. создалась копия.
