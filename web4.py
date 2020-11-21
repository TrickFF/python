# import lib1 as lib
#
# lib.sh_ms()
# print(lib.simple())

# from sys import argv
# name, s_1, s_2, s_3 = argv
# print(argv)
# print(s_1)
# print(s_2)
# print(s_3)

# from random import randint, randrange, random
#
# print(randint(2, 5))  # включает верхнюю границу
# print(randrange(9, 29, 4)) # не включает верхнюю границу
# print(random()) # от 0 до 1, не включая 1 можно умножить
#
# yield - это ключевое слово, которое используется, как return,
# но функция вернет генератор.
# def gen():
#     for el in {1, 2, 3}:
#         yield el
#
# m = next(gen())
# print(m)
# print(m)

from functools import reduce
import  itertools

from itertools import count

for el in count(7):
    if el > 25:
        break
    print(el)
