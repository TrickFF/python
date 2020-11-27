class Transport:
    # атрибуты объекта
    def __init__(self, name, model, year):
        self.n = name
        self.m = model # защищенная
        self.y = year # приавтная

    # методы класса
    def on_start(self,):
        speed = 10
        print(f'Go - go! car {self.n} {self.m} with speed {speed}')

    def on_stop(self):
        print('Stop!')

class Auto(Transport):
    def __init__(self, name, model, year, p_s):
        super().__init__()
        self.p = p_s

    def drift(self):
        print("Bzzzzzz")

auto_1 = Auto('Mazda', 'Miata', [2020, 2019], 1)
auto_1.on_start()
auto_1.on_stop()