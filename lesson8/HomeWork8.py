""" Задание 1 """
print('Задание 1')
class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def extract(cls, obj):
        a = obj.data.split('-')
        return print(f'Day - {int(a[0])}\nMonth - {int(a[1])}\nYear - {int(a[2])}')

    @staticmethod
    def valid(obj):
        a = obj.data.split('-')
        if 1 <= int(a[0]) <= 31:
            if 1 <= int(a[1]) <= 12:
                if 2000 >= int(a[2]) >= 0:
                    return f'Введённые значения корректны'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'


data1 = Data('12-9-1999')
print(Data.extract(data1))
print(data1.valid(data1))

""" Задание 2 """
print('Задание 2')
class MyException(Exception):

    def __init__(self, text):
        self.text = text


try:
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))

    if b == 0:
        raise MyException('Деление на ноль невозможно!')

except (ValueError, MyException) as err:
    print(err)
else:
    print(a / b)

""" Задание 3 """
print('Задание 3')
class MyException(Exception):
    def __init__(self, text):
        self.text = text


b = []
a = input('Введите число: ')
while a != 'stop':
    try:
        if a.isdigit() is False:
            raise MyException('Only number!!!')
    except (ValueError, MyException) as err:
        print(err)
        a = input('Введите число: ')
    else:
        b.append(a)
        print(b)
        a = input('Введите число: ')
else:
    print('STOP')
    print(b)


""" Задание 4, 5, 6  """
print('Задание 4, 5, 6')

class StoreMashines:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    def reception(self):
        try:
            unit = input(f'Введите наименование ')
            unit_p = int(input(f'Введите цену за ед '))
            unit_q = int(input(f'Введите количество '))
            unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Текущий список -\n {self.my_store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад -\n {self.my_store_full}')
            return f'Выход'
        else:
            return StoreMashines.reception(self)

class Printer(StoreMashines):
    def to_print(self):
        return f'to print smth {self.numb} times'


class Scanner(StoreMashines):
    def to_scan(self):
        return f'to scan smth {self.numb} times'


class Copier(StoreMashines):
    def to_copier(self):
        return f'to copier smth  {self.numb} times'


unit_1 = Printer('hp', 2000, 5, 10)
unit_2 = Scanner('Canon', 1200, 5, 10)
unit_3 = Copier('Xerox', 1500, 1, 15)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())

""" Задание 7 """
print('Задание 7')
class Complex:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'

    def __add__(self, other):
        print(f'Сумма z1 и z2 равна')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

z_1 = Complex(5, 4)
z_2 = Complex(7, 2)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)

