class MyClass:
    def __init__(self, p_1):
        self.p_1 = p_1

    def __call__(self, new_p_1): # self, *args, **kwargs
        self.p_1 = new_p_1


    def __str__(self):
         return f'p_1: {self.p_1}.'
    

obj_1 = MyClass(90)
obj_2 = MyClass(91)
print(obj_1, obj_2)

# obj_1.p_1 = 'One'
obj_1('One') # вместо обращения к методу перегружаем функцию __call__
obj_2('Two')
print(obj_1, obj_2)