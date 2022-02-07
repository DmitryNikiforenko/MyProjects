""" Задание 1 """
print('Задание 1')
import time
class TrafficLight:
    __color = 'red', 'yellow', 'green'

    def running(self):
        x = 1
        while x == 1:
            print(TrafficLight.__color[0])
            time.sleep(7)
            print(TrafficLight.__color[1])
            time.sleep(2)
            print(TrafficLight.__color[2])
            time.sleep(5)

a = TrafficLight()
print(a.running())

""" Задание 2 """
print('Задание 2')
class Road:
    _masf = 25
    _wasf = 5

    def __init__(self, l, w):
        self._length = l
        self._width = w

    def metric(self):
        b = (self._width * self._length * Road._masf * Road._wasf)//1000
        return print(f'Необходимая масса асфальта - {b} тонн')

a = Road(20, 5000)
a.metric()

""" Задание 3 """
print('Задание 3')
class Worker:

    def __init__(self, n, s, p, i):
        self.name = n
        self.surname = s
        self.position = p
        self._income = i

class Position(Worker):
    def get_full_name(self):
        return print(f"Полное имя - {self.name + ' ' + self.surname}")
    def get_total_income(self):
        return print(f"Доход с учётом премии - {self._income.get('wage') + self._income.get('bonus')}")

cash = {"wage": 20, "bonus": 50}
cash1 = {"wage": 150, "bonus": 200}

a = Position('Victoria', 'Lasse', 'worker', cash)
print(a.name)
print(a.surname)
print(a.position)
print(a._income)
a.get_full_name()
a.get_total_income()

a = Position('Vlfdislav', 'Germanovich', 'shef', cash1)
print(a.name)
print(a.surname)
print(a.position)
print(a._income)
a.get_full_name()
a.get_total_income()

""" Задание 4 """
print('Задание 4')
class Car:
    def __init__(self, s, c, n, t, p):
        self.speed = s
        self.color = c
        self.name = n
        self.is_police = p
        self.turn = t

    def go(self):
        return print('Go!')

    def stop(self):
        return print('STOP')

    def turn_direction(self):
        return print(f'Машина повернула - {self.turn}')

    def show_speed(self):
        return print(f'Машина двигается со скоростью {self.speed} км/ч')

class TownCar(Car):
    def __init__(self, s, c, n, t, p):
        super().__init__(s, c, n, t, p)

    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости!!!')

class SportCar(Car):
    def __init__(self, s, c, n, t, p):
        super().__init__(s, c, n, t, p)

class WorkCar(Car):
    def __init__(self, s, c, n, t, p):
        super().__init__(s, c, n, t, p)
    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости!!!')

class PoliceCar(Car):
    def __init__(self, s, c, n, t, p):
        super().__init__(s, c, n, t, p)

a = TownCar(55, 'red', 'toyota', 'left', False)
print(a.speed)
print(a.color)
print(a.name)
print(a.turn)
print(a.is_police)
a.go()
a.stop()
a.turn_direction()
a.show_speed()

a1 = TownCar(70, 'green', 'BMV', None, False)
print(a1.speed)
print(a1.color)
print(a1.name)
print(a1.turn)
print(a1.is_police)
a1.go()
a1.stop()
a1.turn_direction()
a1.show_speed()

b = WorkCar(35, 'black', 'Volvo', 'Right', False)
print(b.speed)
print(b.color)
print(b.name)
print(b.turn)
print(b.is_police)
b.go()
b.stop()
b.turn_direction()
b.show_speed()

b1 = WorkCar(57, 'purple', 'mercedes', 'left', False)
print(b1.speed)
print(b1.color)
print(b1.name)
print(b1.turn)
print(b1.is_police)
b1.go()
b1.stop()
b1.turn_direction()
b1.show_speed()

c = SportCar(150, 'pink', 'MCLaren', 'right', False)
print(c.speed)
print(c.color)
print(c.name)
print(c.turn)
print(c.is_police)
c.go()
c.stop()
c.turn_direction()
c.show_speed()

d = PoliceCar(60, 'white', 'BMV', None, True)
print(d.speed)
print(d.color)
print(d.name)
print(d.turn)
print(d.is_police)
d.go()
d.stop()
d.turn_direction()
d.show_speed()

""" Задание 5 """
print('Задание 5')
class Stationery:

    def __init__(self, t):
        self.title = t

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Отрисовка ручкой')
class Pencil(Stationery):
    def draw(self):
        print('Отрисовка карандашом')
class Handle(Stationery):
    def draw(self):
        print('Отрисовка маркером')

a = Pen('P1')
print(a.title)
a.draw()
b = Pencil('B1')
print(b.title)
b.draw()
c = Handle('C1')
print(c.title)
c.draw()
