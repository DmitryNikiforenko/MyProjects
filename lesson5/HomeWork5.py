
"""Задание 1"""
print('Задание 1')
import os
with open(os.path.join(os.getcwd(), 'lesson5', 'txt1.txt'), 'w') as f:
    f.write('')
with open(os.path.join(os.getcwd(), 'lesson5', 'txt1.txt'), 'a') as f:
    b = input('Введите данные: ')
    a = 1
    while a == 1:
        if b == '':
            a = 0
        else:
            f.write(b + '\n')
            b = input('Введите данные: ')
    else:
        pass

"""Задание 2"""
print('Задание 2')
import os
with open(os.path.join(os.getcwd(), 'lesson5', 'txt2.txt'), 'w') as f:
    f.write('asd - asd asd\nqwe qwe qwe qwe\nzxc zxc')
with open(os.path.join(os.getcwd(), 'lesson5', 'txt2.txt')) as f:
    file = f.readlines()
print(f'Количесиво строк: {len(file)}')
c = str()
for x, y in enumerate(file, 1):
    b = y.split()
    for i in b:
        if i == '-':
            b.remove('-')
    print(f'Количество слов в строке {x}) - {len(b)} слова')

"""Задание 3"""
print('Задание 3')
import os

def salary_min(i):
    if i == 1:
        if b[i] < '20000':
            c.append(b[0])
    return c

def salary_mean(i):
    global n
    global m
    if i == 1:
        n += 1
        m += int(b[i])
    return m, n

with open(os.path.join(os.getcwd(), 'lesson5', 'txt3.txt'), 'w') as f:
    f.write('Иванов 20000\nПетров 15000\nСидоров 40000\nКлепанов 45000\nВойтюк 17000\n'
            'Петренко 25000\nСтепанюк 12000\nЛужков 60000\nЖуков 18000\nСеменюк 45000')
with open(os.path.join(os.getcwd(), 'lesson5', 'txt3.txt'),) as f:
    file = f.readlines()
    print(file)
    c = []
    m = int()
    n = int()
    print('Сотрудники, имеющие оклад менее 20000:')
    for x in file:
        b = x.split()
        for i in range(len(b)):
            salary_min(i)
            salary_mean(i)
    for q in c:
        print(q)
    print(f'Средняя величина дохода сотрудников - {m/n}')

"""Задание 4"""
print('Задание 4')
import os
c = []
with open(os.path.join(os.getcwd(), 'lesson5', 'txt4.txt'), 'w') as f:
    f.write('One — 1\nTwo — 2\nThree — 3\nFour — 4')
with open(os.path.join(os.getcwd(), 'lesson5', 'txt4.txt'),) as f:
    print(f.read())
with open(os.path.join(os.getcwd(), 'lesson5', 'txt4.txt'),) as f:
    a = f.readline()
    a.split()
    c.append(a.replace('One', 'Один'))
    a = f.readline()
    a.split()
    c.append(a.replace('Two', 'Два'))
    a = f.readline()
    a.split()
    c.append(a.replace('Three', 'Три'))
    a = f.readline()
    a.split()
    c.append(a.replace('Four', 'Четыре'))
with open(os.path.join(os.getcwd(), 'lesson5', 'txt4.txt'), 'w') as f:
    f.writelines(c)
with open(os.path.join(os.getcwd(), 'lesson5', 'txt4.txt'),) as f:
    print(f.read())

"""Задание 5"""
print('Задание 5')
import os
from functools import reduce
with open(os.path.join(os.getcwd(), 'lesson5', 'txt5.txt'), 'w') as f:
    f.write('1 2 3 4 5 6 7 8 9 10')
with open(os.path.join(os.getcwd(), 'lesson5', 'txt5.txt'),) as f:
    print(reduce(lambda x, y: x + y, [int(x) for x in f.read().split()]))

"""Задание 6"""
print('Задание 6')
import os
from functools import reduce
with open(os.path.join(os.getcwd(), 'lesson5', 'txt6.txt'), 'w') as f:
    f.write('Информатика: 100(лекц) 50(пркт) 20(лабо)\nФизика: 30(лекц) 10(лабо)\nФизкультура: 30(пркт)')

dct = {}
def sort(line):
    c = []
    a = line.split()
    c.append([int(x[:-6]) for x in a if x[-6:] == '(лекц)'])
    c.append([int(x[:-6]) for x in a if x[-6:] == '(пркт)'])
    c.append([int(x[:-6]) for x in a if x[-6:] == '(лабо)'])
    d = reduce(lambda x, y: x + y, reduce(lambda x, y: x + y, c))
    dct.update({a[0]: d})
    return dct

with open(os.path.join(os.getcwd(), 'lesson5', 'txt6.txt'),) as f:
    for line in f:
        sort(line)
    print(dct)

"""Задание 7"""
print('Задание 7')
import os
from functools import reduce
import json
c = []
salary_mean = []
dct = {}

def conpany_cash(line):
    a = line.split()
    b = int(a[2]) - int(a[3])
    if b > 0:
        salary_mean.append(b)
    new_dct = {a[0]: b}
    return dct.update(new_dct)

with open(os.path.join(os.getcwd(), 'lesson5', 'txt7.txt'), 'w') as f:
    f.write('firm_1 ООО 10000 5000\n'
            'firm_2 ЗАО 20000 300000\n'
            'firm_3 ЧУП 100000 50000\n'
            'firm_4 ЗАО 1580000 755000\n'
            'firm_5 ООО 19000 6000')

with open(os.path.join(os.getcwd(), 'lesson5', 'txt7.txt'), ) as f:
    for line in f:
        conpany_cash(line)
q = len(salary_mean)
r = reduce((lambda x, y: x + y), salary_mean) // q
new_dict1 = {'average_profit': r}
dct.update(new_dict1)
print(salary_mean)
print([dct])

with open(os.path.join(os.getcwd(), 'lesson5', 'my_file.json'), 'w') as j:
    json.dump([dct], j)
