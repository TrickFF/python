# 1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

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

# для задачи взят файл из 1го задания
with open('text_1.txt', 'r', encoding='utf-8') as file:
    data = file.read()
    print(data)
    dataset = data.split('\n')  # записываем строку в список. Каждая строка элемент списка
    print(f'Количество строк в файле = {len(dataset) - 1}')
    dataset = data.split()  # записываем строку в список. Каждое слово элемент списка
    print(f'Количество слов в файле = {len(dataset)}')

####################################################################################################

# 3. Создать текстовый файл (не программно), построчно записать фамилии
# сотрудников и величину их окладов. Определить, кто из сотрудников имеет
# оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('text_3.txt', 'r', encoding='utf-8') as file:
    data = file.read()  # получаем данные из файла в строку
    print(data)
    data = data.split('\n')  # преобразуем строку в список построчно
    workers = {el.split(" ")[0]: float(el.split(" ")[1]) for el in data}  # переносим в словарь
    workers2 = [k for k, v in workers.items() if v < 20000]
    print(f'Сотрудники, оклад которых менее 20к: {workers2}')
    print(f'Средний оклад сотрудников = {sum(v for k, v in workers.items()) / len(workers)}')

####################################################################################################

# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

# Вариант 1
#  этот переводчик переводит лучше, но дает сбои в работе, приходится несколько раз запускать
from googletrans import Translator

translator = Translator()

with open('text_4.txt', 'r', encoding='utf-8') as file:
    data = file.read()  # получаем данные из файла в строку
    print(data)
    dataset = data.split('\n')  # получаем список
    print(dataset)

# записываем данные в файл text_4_2.txt
with open('text_4_2.txt', 'w', encoding='utf-8') as file2:
    for i in range(len(dataset)):
        dataset[i] = dataset[i].split()  # разбиваем элемент списка на строку
        tr = translator.translate(dataset[i][0], dest='ru')  # переводим 1й элемент
        print(tr.text, dataset[i][1], dataset[i][2], file=file2)

# Вариант 2
#  translate переводит хуже, но не сбоит
from translate import Translator

translator = Translator(from_lang="English", to_lang="Russian")

with open('text_4.txt', 'r', encoding='utf-8') as file:
    data = file.read()  # получаем данные из файла в строку
    print(data)
    dataset = data.split('\n')  # получаем список
    print(dataset)

# записываем данные в файл text_4_2.txt
with open('text_4_2.txt', 'w', encoding='utf-8') as file2:
    for i in range(len(dataset)):
        dataset[i] = dataset[i].split()  # разбиваем элемент списка на строку
        tr = translator.translate(dataset[i][0])  # переводим 1й элемент
        print(tr, dataset[i][1], dataset[i][2], file=file2)

####################################################################################################

# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('text_5.txt', 'w', encoding='utf-8') as file:
    string = input('Введите строку числовых значений, разделенных пробелами - ').split()
    for el in string:
        if el.isdigit() == True:  # записываем в файл только числа из введенной строки
            print(float(el), file=file)

# записываем данные в файл text_5.txt
with open('text_5.txt', 'r', encoding='utf-8') as file:
    string = file.read().split()
    print(f'Числовые значения в файле - {string}')
    string = map(float, string)

print(f'Сумма чисел в файле = {sum(string)}')

####################################################################################################

# 6. Необходимо создать (не программно) текстовый файл, где каждая строка
# описывает учебный предмет и наличие лекционных, практических и лабораторных занятий
# по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
# были все типы занятий. Сформировать словарь, содержащий название предмета и
# общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

import re

with open('text_6.txt', 'r', encoding='utf-8') as file:
    string = file.read().split('\n')  # считываем данные из файла в список, каждый элемент - строка файла

lessons = {el.split(":")[0]: el.split(":")[1] for el in string}  # делим строку на элементы и переносим в словарь

for k, v in lessons.items():
    v = re.findall('(\d+)', v)  # ищем числа в каждом значении словаря и делаем из них список
    lessons[k] = v

print(lessons)

####################################################################################################

# 7. Создать (не программно) текстовый файл, в котором каждая строка
# должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
import json

# Объявляем пременные
count = 0
result = 0
result_total = 0
fin_res = {}
mean = {}
add = []

with open('text_7.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():  # построчно считываем файл
        line = line.split()
        if float(line[2]) - float(line[3]) > 0:  # если результат деятельности компании прибыль
            count += 1  # считаем количество компаний с прибылью
            result += (float(line[2]) - float(line[3]))  # суммируем прибыли компаний
            print(f'Результат работы {line[1]} {line[0]} составляет: {float(line[2]) - float(line[3])}')
        else:
            print(f'Результат работы {line[1]} {line[0]} составляет: {float(line[2]) - float(line[3])}')
        _ = {line[0]: float(line[2]) - float(line[3])}
        fin_res.update(_)  # добавляем в словарь запись
    print(f'Средняя прибыль {count} компаний составляет: {result / count}')
    _ = {"average_profit": result / count}
    mean.update(_)  # добавляем в словарь запись

add = [fin_res, mean]

# записываем информацию в файл text_77.json
with open('text_77.json', 'w', encoding='utf-8') as file:
    json.dump(add, file, indent=2, ensure_ascii=False)
