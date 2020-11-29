# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color
# (цвет) и метод running (запуск). Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый). Проверить работу примера, создав экземпляр
# и вызвав описанный метод. Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.

# Ваариант 1
from time import sleep
from termcolor import colored


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        for i in range(count):
            print(colored(TrafficLight.__color[0], 'red'))
            sleep(7)
            print(colored(TrafficLight.__color[1], 'yellow'))
            sleep(2)
            print(colored(TrafficLight.__color[2], 'green'))
            sleep(7)
            print(colored(TrafficLight.__color[1], 'yellow'))
            sleep(2)


# выход из цикла, если ввод корректен
while True:
    try:
        count = int(input('Введите количество циклов работы светофора - '))
        if count < 0:
            raise ValueError  # поднимаем ошибку, если count < 0
        break
    except ValueError:
        print('Следует ввести положительное число!')  # обработка ошибки ввода значения

t = TrafficLight()
t.running()

# Вариант 2
from tkinter import Tk, Canvas, Frame, Button


class TrafficLight(Tk):
    __color = ['red', 'yellow', 'green', 'lightgrey', 'black']

    def __init__(self):
        Tk.__init__(self)
        fr = Frame(self)
        fr.pack()
        self.title("Traffic Light")
        self.canvas = Canvas(fr, height=200, width=140)
        self.canvas.pack()

        start_btn = Button(self, text="START", height=1, width=6, command=self.running)
        start_btn.pack()

        stop_btn = Button(self, text="STOP", height=1, width=6, command=self.stop)
        stop_btn.pack()

        self.red = self.canvas.create_rectangle(45, 25, 95, 75, fill=TrafficLight.__color[3])
        self.yellow = self.canvas.create_rectangle(45, 75, 95, 125, fill=TrafficLight.__color[3])
        self.green = self.canvas.create_rectangle(45, 125, 95, 175, fill=TrafficLight.__color[3])

    def change_red(self):
        self.canvas.itemconfigure(self.red, fill=TrafficLight.__color[0])
        self.canvas.itemconfigure(self.yellow, fill=TrafficLight.__color[3])
        self.canvas.itemconfigure(self.green, fill=TrafficLight.__color[3])
        root.after(7000, root.change_yellow_r)

    def change_yellow_r(self):
        self.canvas.itemconfigure(self.red, fill=TrafficLight.__color[3])
        self.canvas.itemconfigure(self.yellow, fill=TrafficLight.__color[1])
        self.canvas.itemconfigure(self.green, fill=TrafficLight.__color[3])
        root.after(2000, root.change_green)

    def change_yellow_g(self):
        self.canvas.itemconfigure(self.red, fill=TrafficLight.__color[3])
        self.canvas.itemconfigure(self.yellow, fill=TrafficLight.__color[1])
        self.canvas.itemconfigure(self.green, fill=TrafficLight.__color[3])
        root.after(2000, root.change_red)

    def change_green(self):
        self.canvas.itemconfigure(self.red, fill=TrafficLight.__color[3])
        self.canvas.itemconfigure(self.yellow, fill=TrafficLight.__color[3])
        self.canvas.itemconfigure(self.green, fill=TrafficLight.__color[2])
        root.after(7000, root.change_yellow_g)

    def running(self):
        self.change_red()

    def stop(self):
        exit()


if __name__ == "__main__":
    root = TrafficLight()
    root.mainloop()


####################################################################################################

# 2. Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина). Значения данных атрибутов должны передаваться
# при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия
# одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна.
# Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road():
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.mass = 25
        self.depth = 5

    def asph_mass(self):
        print(f'Для покрытия дорожного полотна неободимо'
              f' {round(self._length * self._width * self.mass * self.depth / 1000, 2)}'
              f' тонн асфальта')


# выход из цикла, если ввод корректен
while True:
    try:
        len = float(input('Введите длину дороги в метрах - '))
        if len < 0:
            raise ValueError  # поднимаем ошибку, если len < 0
        break
    except ValueError:
        print('Следует ввести положительное число!')  # обработка ошибки ввода значения

# выход из цикла, если ввод корректен
while True:
    try:
        wid = float(input('Введите ширину дороги в метрах - '))
        if wid < 0:
            raise ValueError  # поднимаем ошибку, если wid < 0
        break
    except ValueError:
        print('Следует ввести положительное число!')  # обработка ошибки ввода значения

mass = Road(len, wid)
mass.asph_mass()


####################################################################################################

# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен
# быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов,
# вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


name = input('Введите имя сотрудника - ').title()
surname = input('Введите фамилию сотрудника - ').title()
position = input('Введите должность сотрудника - ').title()

# выход из цикла, если ввод корректен
while True:
    try:
        wage = float(input('Введите зарплату сотрудника в руб. - '))
        if wage < 0:
            raise ValueError  # поднимаем ошибку, если wage < 0
        bonus = float(input('Введите бонус в руб. - '))
        if bonus < 0:
            raise ValueError  # поднимаем ошибку, если bonus < 0
        break
    except ValueError:
        print('Следует ввести положительное число!')  # обработка ошибки ввода значения

wk = Position(name, surname, position, wage, bonus)
print(f'Доход сотрудника {wk.get_full_name()} составляет {wk.get_total_income()} руб.')

####################################################################################################

# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение
# о превышении скорости.
import random as rnd


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} тронулась с места.')

    def stop(self):
        print(f'Машина {self.name} остановилась.')

    def turn(self, direction):
        print(f'Машина {self.name} {direction}.')

    def show_speed(self):
        print(f'Текщая скорость автомобился {self.name} - {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость {self.speed} км/ч, превышение допустимой скорости в 60 км/ч!')
        else:
            print(f'Текщая скорость автомобился {self.name} - {self.speed} км/ч')


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        pass


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 40:
            print(f'Скорость {self.speed} км/ч, превышение допустимой скорости в 40 км/ч!')
        else:
            print(f'Текщая скорость автомобился {self.name} - {self.speed} км/ч')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)

    def siren(self, wcspeed, tcspeed):
        if wcspeed > 40:
            print(f'Превышение скорости грузовым автомобилем. Вкючена сирена!')
        if tcspeed > 60:
            print(f'Превышение скорости а/м городского транспорта. Вкючена сирена!')


def dir():
    ls = ['повернула налево', 'повернула направо', 'развернулась']
    direction = rnd.choice(ls)
    return direction


sc = SportCar(270, 'red', 'Ferrari')
sc.go()
sc.show_speed()
sc.turn(dir())
sc.stop()

wc = WorkCar(rnd.randint(1, 100), 'Blue', 'ZIL')
wc.go()
wc.show_speed()
wc.turn(dir())
wc.stop()

tc = TownCar(rnd.randint(1, 100), 'Yellow', 'GAZelle')
tc.go()
tc.show_speed()
tc.turn(dir())
tc.stop()

pc = PoliceCar(70, 'white', 'Lincoln')
pc.go()
pc.show_speed()
pc.turn(dir())
wcspeed = wc.speed
tcspeed = tc.speed
pc.siren(wcspeed, tcspeed)


####################################################################################################

# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Отрисовка инструмнтом {self.title} ручка')


class Pencil(Stationery):
    def draw(self):
        print(f'Отрисовка инструмнтом {self.title} карандаш')


class Handle(Stationery):
    def draw(self):
        print(f'Отрисовка инструмнтом {self.title} маркер')


pn = Pen('Шариковая')
pn.draw()

pnc = Pencil('Цветной')
pnc.draw()

hd = Handle('Перманентный')
hd.draw()
