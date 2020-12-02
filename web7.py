class MyClass:
    def __init__(self, p_1, p_2):
        self.p_1 = p_1
        self.p_2 = p_2

    # def __del__(self):
    #     print(f'Объект удален {self}!')

    def __add__(self, other): # 90 (self) + 91(other)
        return MyClass(self.p_1 + other.p_1, self.p_2 + other.p_2)

    def __str__(self):
         return f'p_1: {self.p_1}, p_2: {self.p_2}'


obj_1 = MyClass(90, 99)
obj_2 = MyClass(91, 100)
print(obj_1 + obj_2 + obj_2)