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
