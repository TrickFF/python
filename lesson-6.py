# 1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
import json

e = 0

with open('text_1.txt', 'w', encoding='utf-8') as file:
    while e == 0:
        string = input('Введите строку значений, разделенных пробелами (enter для завершения) - ')
        if string:  # если строка пустая, то завершаем работу
            print(string, file=file)
        else:
            e = 1

####################################################################################################

# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('text_1.txt', 'r', encoding='utf-8') as file:
    data = file.read()
    print(data)
    dataset = data.split('\n') # записываем строку в список. Каждая строка элемент списка
    print(f'Количество строк в файле = {len(dataset)-1}')
    dataset = data.split() # записываем строку в список. Каждое слово элемент списка
    print(f'Количество слов в файле = {len(dataset)}')

####################################################################################################

# 3. Создать текстовый файл (не программно), построчно записать фамилии
# сотрудников и величину их окладов. Определить, кто из сотрудников имеет
# оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('text_3.txt', 'r', encoding='utf-8') as file:
    data = file.read() # получаем данные из файла в строку
    print(data)
    data = data.split('\n') # преобразуем строку в список построчно
    workers = {el.split(" ")[0]: float(el.split(" ")[1]) for el in data} # переносим в словарь
    workers2 = [k for k, v in workers.items() if v < 20000]
    print(f'Сотрудники, оклад которых менее 20к: {workers2}')
    print(f'Средний оклад сотрудников = {sum(v for k, v in workers.items())/len(workers)}')

####################################################################################################

# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

#  google переводит лучше, но дает сбои в работе, приходится несколько раз запускать
from googletrans import Translator

translator = Translator()

with open('text_4.txt', 'r', encoding='utf-8') as file:
    data = file.read()  # получаем данные из файла в строку
    print(data)
    dataset = data.split('\n')  # получаем список
    print(dataset)

with open('text_4_2.txt', 'w', encoding='utf-8') as file2:
    for i in range(len(dataset)):
        dataset[i] = dataset[i].split()  # разбиваем элемент списка на строку
        tr = translator.translate(dataset[i][0], dest='ru')  # переводим 1й элемент
        print(tr.text, dataset[i][1], dataset[i][2], file=file2)


#  translate переводит хуже, но не сбоит
from translate import Translator

translator = Translator(from_lang="English", to_lang="Russian")

with open('text_4.txt', 'r', encoding='utf-8') as file:
    data = file.read()  # получаем данные из файла в строку
    print(data)
    dataset = data.split('\n')  # получаем список
    print(dataset)

with open('text_4_2.txt', 'w', encoding='utf-8') as file2:
    for i in range(len(dataset)):
        dataset[i] = dataset[i].split()  # разбиваем элемент списка на строку
        tr = translator.translate(dataset[i][0])  # переводим 1й элемент
        print(tr, dataset[i][1], dataset[i][2], file=file2)

####################################################################################################