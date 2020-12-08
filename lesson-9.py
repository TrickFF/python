# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать
# их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
# данных.
class Data:
    def __init__(self, dd, mm, yyyy):
        self.dd = dd
        self.mm = mm
        self.yyyy = yyyy

    def __str__(self):
        return f'День {d1.dd}, Месяц {d1.mm}, Год {d1.yyyy}'

    @classmethod
    def data_split(cls, data):
        dd, mm, yyyy = data.split('-')
        dd, mm, yyyy = int(dd), int(mm), int(yyyy)
        Data.check(mm)
        if Data.check(mm):
            return cls(dd, mm, yyyy)
        else:
            print('Месяц должен быть в диапазоне от 1 дло 12!')

    @staticmethod
    def check(mm):
        if mm <= 12 and mm >= 1:
            return True
        else:
            return False


date = '14-09-2014'
d1 = Data.data_split(date)
print(d1 or ' ')


####################################################################################################

# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
# в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться
# с ошибкой.

class ZeroDiv(Exception):
    def __init__(self, msg):
        self.msg = msg


while True:
    try:
        k = int(input('Введите делимое - '))
        break
    except (ValueError, ZeroDiv) as e:
        print(e)

while True:
    try:
        t = int(input('Введите делитель - '))
        if t == 0:
            raise ZeroDiv('Число не должно быть = 0')
    except (ValueError, ZeroDiv) as e:
        print(e)
    else:
        print(f'Резкльтат деления {k} на {t} = {k / t:.3}')
        break


####################################################################################################

# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на
# наличие только чисел. Проверить работу исключения на реальном примере. Необходимо запрашивать
# у пользователя данные и заполнять список. Класс-исключение должен контролировать типы данных
# элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит
# работу скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
# только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить
# соответствующее сообщение. При этом работа скрипта не должна завершаться.

class ListCheck(Exception):
    def __init__(self, list):
        self.list = list
        a = ListCheck.check(list)
        if a == True:
            print(list)
        else:
            print('В списке присутствуют не только числа!')

    @staticmethod
    def check(list):
        for i in range(len(list)):
            try:
                list[i] = int(list[i])
            except (ValueError, TypeError):
                return False
        return True


e = 0
while e == 0:
    list = input('Введите строку чисел (stop для завершения) - ')
    list = list.split()
    if list[-1] == 'stop':  # если в строке введен stop, то завершаем работу
        list.remove(list[-1])
        e = 1
    l1 = ListCheck(list)
    try:
        l1
        if ListCheck.check == False:
            raise ListCheck
    except ListCheck as e:
        print(e)


####################################################################################################

# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
# в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
# других данных, можно использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных
# на уроках по ООП.

class LessThanZero(Exception):
    def __init__(self):
        print('Цена устройства не должна быть < 0!')


class ValueError(Exception):
    def __init__(self):
        print('Недопустимое значение!')


class OrgStock:
    dpt_list = ['Склад', 'Отдел продаж', 'Отдел маркетинга', 'Бухгалтерия']
    type_list = ['Принтер', 'Сканер', 'Ксерокс']
    stock = {}

    def inc_to_stock(self):
        '''Добавление устройств на склад'''

        try:
            type = input(f'Выберите тип устройства Принтер(1), Сканер(2), Ксерокс(3): ')
            if type.isdigit() == True:
                type = int(type)
                if type > len(OrgStock.type_list) or type <= 0:
                    raise ValueError
            name = input(f'Введите наименование: ')
            price = float(input(f'Введите цену за ед: '))
            if price < 0:
                raise LessThanZero
            dpt = 0  # 0-е подразделение - склад
            count = len(OrgStock.stock) + 1
            if type == 1:
                Printer.count_pr += 1
            elif type == 2:
                Scaner.count_sc += 1
            elif type == 3:
                Xerox.count_xr += 1
            item = {count: {'Тип устройства': type, 'Модель устройства': name,
                            'Цена за ед': price, 'Подразделение': dpt}}
            OrgStock.stock.update(item)
            print(f'Устройство {name} принято на склад')
        except (ValueError, LessThanZero):
            print('', end='')

    @staticmethod
    def info():
        '''Вывод детальной информации по всем устройствам
        За основу взял ранее сделанное задание, поэтому способ вывода остался такой же
        '''

        if len(OrgStock.stock) > 0:
            type_str = []
            name_str = []
            price_str = []
            dpt_str = []

            # формируем строки вывода
            for k, v in OrgStock.stock.items():
                if v['Тип устройства'] == 1:
                    type_str.append(OrgStock.type_list[0])
                elif v['Тип устройства'] == 2:
                    type_str.append(OrgStock.type_list[1])
                elif v['Тип устройства'] == 3:
                    type_str.append(OrgStock.type_list[2])
                name_str.append(v['Модель устройства'])
                price_str.append(v['Цена за ед'])
                if v['Подразделение'] == 0:
                    dpt_str.append(OrgStock.dpt_list[0])
                elif v['Подразделение'] == 1:
                    dpt_str.append(OrgStock.dpt_list[1])
                elif v['Подразделение'] == 2:
                    dpt_str.append(OrgStock.dpt_list[2])
                elif v['Подразделение'] == 3:
                    dpt_str.append(OrgStock.dpt_list[3])

            # выводим информацию
            print('"Тип устройства"   :', type_str)
            print('"Модель устройства":', name_str)
            print('"Цена за ед"       :', price_str)
            print('"Подразделение"    :', dpt_str)
        print(f'Всего устройств - {len(OrgStock.stock)}')

    @staticmethod
    def move():
        '''Перемещение устройств. Меняется ID подразделения, за котоорым закреплено устройство'''

        a = 0
        while a == 0:
            move_id = input('Введите номер перемещаемого устройства - ')
            if move_id.isdigit() == True:
                move_id = int(move_id)
                if move_id <= len(OrgStock.stock) and move_id >= 0:
                    dpt_id = input(f'Введите номер отдела, куда переместится устройство:\n'
                                   f'0 - {OrgStock.dpt_list[0]}\n'
                                   f'1 - {OrgStock.dpt_list[1]}\n'
                                   f'2 - {OrgStock.dpt_list[2]}\n'
                                   f'3 - {OrgStock.dpt_list[3]} - ')
                    if dpt_id.isdigit() == True:
                        dpt_id = int(dpt_id)
                        if dpt_id <= len(OrgStock.dpt_list) and dpt_id >= 0:
                            OrgStock.stock[move_id]['Подразделение'] = dpt_id
                            a = 1
                        else:
                            print('Нет такого подразделения')
                            continue
                    print(f"Устройство {OrgStock.stock[move_id]['Модель устройства']} с номером {move_id} "
                          f"перемещено в подразделение {OrgStock.dpt_list[dpt_id]}")
                else:
                    print('Нет такого устройства')
            else:
                print('Нет такого устройства')

    @staticmethod
    def total_info():
        '''Вывод информации по количеству устройств каждого типа'''

        print('Общее количество техники в компании:')
        print(f'Принтеров: {Printer.count_pr}\n'
              f'Сканеров : {Scaner.count_sc}\n'
              f'Ксероксов: {Xerox.count_xr}')


class OrgType:
    pass


class Printer(OrgType):
    count_pr = 0


class Scaner(OrgType):
    count_sc = 0


class Xerox(OrgType):
    count_xr = 0


command = ''

# Основное меню
while command != 'exit':
    command = input('Введите команду. help - для вывода справки, exit - для выхода - ')
    if command == '1':
        OrgStock().inc_to_stock()
    elif command == '2':
        OrgStock.move()
    elif command == '3':
        OrgStock.info()
    elif command == '4':
        OrgStock.total_info()
    elif command == 'help':
        print(f'1 - поступление устройства\n'
              f'2 - перемещение устройств\n'
              f'3 - вывод информации об устройствах\n'
              f'4 - вывод информации о количестве устройств по типам\n'
              f'exit - завершение работы')
    elif command == 'exit':
        break
    else:
        print('Нет такой операции!')


####################################################################################################

# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте
# перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры
# класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность
# полученного результата.

class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сумма чисел ({self.a}+{self.b}j) и ({other.a}+{other.b}j) равна:' \
               f' {self.a + other.a} + {self.b + other.b}j'

    def __mul__(self, other):
        return f'Произведение чисел ({self.a}+{self.b}j) и ({other.a}+{other.b}j) равно:' \
               f' {self.a * other.a - self.b * other.b} + {self.a * other.b + other.a * self.b}j'


n1 = ComplexNumber(4, 12)
n2 = ComplexNumber(5, 3)
print(n1 + n2)
print(n1 * n2)
