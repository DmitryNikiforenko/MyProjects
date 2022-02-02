"""Задание 1"""
print('Задание 1')
'''Файл скрипта - script1.py'''
from sys import argv
script_name, a, b, c = argv
print('Рассчёт заработной платы сотрудника: ')
a = int(a)
b = int(b)
c = int(c)
print(f'Выработка в часах - {a}')
print(f'Ставка в час - {b}')
print(f'Премия - {c}')
print(f'Заработная плата сотрудника составила {((a * b) + c)}')

"""Задание 2"""
print('Задание 2')
a = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print([a[x] for x in range(1, len(a)) if a[x] > a[x - 1]])

"""Задание 3"""
print('Задание 3')
print([x for x in range(20, 240) if x % 20 == 0 or x % 21 == 0])

"""Задание 4"""
print('Задание 4')
a = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print([x for x in a if a.count(x) == 1])

"""Задание 5"""
print('Задание 5')
import functools
print([x for x in range(100, 1002) if x % 2 == 0])
print(functools.reduce(lambda a, b: a * b, [x for x in range(100, 1002) if x % 2 == 0]))

"""Задание 6"""
print('Задание 6')
'''Итератор, генерирующий целые числа, начиная с указанного - script2.py'''
from sys import argv
script_name, a = argv
a = int(a)
from itertools import count
print([print(x) for x in count(a) if x < a + 11])
'''итератор, повторяющий элементы некоторого списка, определённого заранее - script3.py'''
from sys import argv
script_mane, b = argv

from itertools import cycle
c = 0
for x in cycle(b):
    if c > 10:
        break
    else:
        print(x)
        c += 1

"""Задание 7"""
print('Задание 7')
from math import factorial

def fuct(a):
    for x in range(1, a + 1):
        yield factorial(x)

for el in fuct(15):
    print(el)
