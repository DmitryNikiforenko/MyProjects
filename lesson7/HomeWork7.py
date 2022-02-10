""" Задание 1 """
print('Задание 1')

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(map(lambda r: '   '.join(map(str, r)), self.matrix)) + '\n'

    def __add__(self, other):
        return Matrix(map(lambda r1, r2: map(lambda x, y: x + y, r1, r2), self.matrix, other.matrix))

m = [[1, 2], [4, 5], [7, 8]]
n = [[2, 3], [5, 6], [8, 9]]

m1 = Matrix(m)
m2 = Matrix(n)
print(m1 + m2)

""" Задание 2 """
print('Задание 2')
from abc import ABC, abstractmethod
class Cloth(ABC):
    result = 0

    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def summary(self):
        pass

    def __add__(self, other):
        Cloth.result = self.summary + other.summary
        return Cloth.result

class Coat(Cloth):
    @property
    def summary(self):
        return round(self.param / 6.5 + 0.5, 2)

class Costume(Cloth):
    @property
    def summary(self):
        return round((self.param * 2) + 0.3, 2)

Coat1 = Coat(15)
Costume1 = Costume(25)
print(Coat1.summary)
print(Costume1.summary)
print(Coat1 + Costume1)

""" Задание 3 """
print('Задание 3')
class Cell:
    result = 0
    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        return f'Сложение {self.cell + other.cell}'

    def __sub__(self, other):
        return f'Вычитание {abs(self.cell - other.cell)}' if self.cell - other.cell != 0\
            else f'Количество ячеек в клетках одинаково!'

    def __mul__(self, other):
        return f'Умножение {self.cell * other.cell}'

    def __truediv__(self, other):
        return f'Деление {self.cell // other.cell}'

a = Cell(655)
b = Cell(30)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
