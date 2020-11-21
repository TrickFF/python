import time
import random
import os
import psutil

car_names = ['Audi', 'Toyota', 'Renault', 'Nissan', 'Honda', 'Suzuki']
colors = ['Black', 'Blue', 'Red', 'White', 'Yellow']

def car_list_gen(cars):
    for i in range (cars):
        car = {
            'id':i,
            'name':random.choice(car_names),
            'color':random.choice(colors)
        }
        yield car

# замеряем потребление памяти
process = psutil.Process(os.getpid())
print('Memory before list is created: ' + str(process.memory_info().rss/1000000))

# Вызов функции car_list_gen и время, сколько времени занимает
t1 = time.process_time()
cars = car_list_gen(1000000)
t2 = time.process_time()

# замеряем потребление памяти
process = psutil.Process(os.getpid())
print('Memory after list is created: ' + str(process.memory_info().rss/1000000))

print('Took {} seconds'.format(t2-t1))

exit()

import time
import random
import os
import psutil

car_names = ['Audi', 'Toyota', 'Renault', 'Nissan', 'Honda', 'Suzuki']
colors = ['Black', 'Blue', 'Red', 'White', 'Yellow']

def car_list(cars):
    all_cars = []
    for i in range (cars):
        car = {
            'id': i,
            'name': random.choice(car_names),
            'color': random.choice(colors)
        }
        all_cars.append(car)
    return all_cars

# замеряем потребление памяти
process = psutil.Process(os.getpid())
print('Memory before list is created: ' + str(process.memory_info().rss/1000000))

# Вызов функции car_list и время, сколько времени это занимает
t1 = time.process_time()
cars = car_list(1000000)
t2 = time.process_time()

# замеряем потребление памяти
process = psutil.Process(os.getpid())
print('Memory after list is created: ' + str(process.memory_info().rss/1000000))

print('Took {} seconds'.format(t2-t1))