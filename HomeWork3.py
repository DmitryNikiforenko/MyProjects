"""Задание 1"""
print('Задание 1')

e = int(input('Введите первое число: '))
f = int(input('Введите первое число: '))

def my_func(a, b):
    if b == 0:
        return 'Деление на ноль невозможно'
    else:
        return a/b

print(my_func(e, f))

"""Задание 2"""
print('Задание 2')

a_ = input('Введите имя: ')
b_ = input('Введите фамилия: ')
c_ = input('Введите год рождения: ')
d_ = input('Введите город проживания: ')
e_ = input('Введите email: ')
f_ = input('Введите телефон: ')

def sum(a, b, c, d, e, f):
    return a, b, c, d, e, f
print(sum(a=a_, b=b_, c=c_, d=d_, e=e_, f=f_))

"""Задание 3"""
print('Задание 3')

def my_func(a, b, c):
    w = []
    w.append(a)
    w.append(b)
    w.append(c)
    q = 0
    for x in w:
        if x > q:
            q = x
        else:
            continue
    if q == a:
        return a + b if b > c else a + c
    elif q == b:
        return a + b if a > c else c + b
    elif q == c:
        return c + a if a > b else b + c
print(my_func(10, 50, 100))

"""Задание 4"""
print('Задание 4')
'''Способ решения через оператор **'''
def step():
    x = int(input('Введите действительное положительное число: '))
    y = int(input('Введите целое отрицательное число: '))
    x = float(1/x**abs(y))
    return x
print(step())
'''Способ решения через цикл'''
def step():
    x = int(input('Введите действительное положительное число: '))
    y = int(input('Введите целое отрицательное число: '))
    q = 0
    b = 1
    while q < y:
        b = x*x
        q = q + 1
    else:
        return 1/b
print(step())

"""Задание 5"""
print('Задание 5')
q = 1
c = []
def calc():
    for x in b:
        i = int(x)
        c.append(i)
    return sum(c)

while q == 1:
    try:
        a = input('Введите числа, разделённые пробелом.'
                  'Для завершения программы введите y: ')
        b = a.split()
        if 'y' in b:
            q = 0
            b.remove('y')
            print(f'Программа завершена с результатом: {calc()}')
            break
        else:
            print(calc())
    except ValueError:
        pass

"""Задание 6"""
print('Задание 6')
def int_func(a):
    return a.title()

print(int_func('abs'))

"""Задание 7"""
print('Задание 7')
def int_func(a):
    return a.title()

print(int_func('abs abs abs'))

