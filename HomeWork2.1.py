"""Задание 6*"""
print('Задание 6*')
x = input('Для начала формирования структуры данных товаров введите 1. '
          'Для завершения формирования структуры данных товаров введите 0'
          ':')
q = 0
my_list = []
while x == '1':
    q = q + 1
    my_dict = {}
    a = input('Название товара: ')
    a_dict = dict(Название=a)
    my_dict.update(a_dict)
    b = input('Цена: ')
    b_dict = dict(Цена=b)
    my_dict.update(b_dict)
    c = input('Количество: ')
    c_dict = dict(Количество=c)
    my_dict.update(c_dict)
    d = input('Ед: ')
    d_dict = dict(Ед=d)
    my_dict.update(d_dict)
    my_tuple = (q, my_dict)
    my_list.append(my_tuple)
    x = input('Для начала формирования структуры данных товаров введите 1. '
              'Для завершения формирования структуры данных товаров введите 0'
              ':')
else:
    print('Формирования структуры данных товаров завершено')

new_list_1 = []
new_list_2 = []
new_list_3 = []
new_list_4 = []
new_dict = {}

for i in my_list:
    for p in i:
        if type(p) == dict:

            new_list_1.append(p.get('Название'))
            a_dict = dict(Название=new_list_1)
            new_dict.update(a_dict)

            new_list_2.append(p.get('Цена'))
            b_dict = dict(Цена=new_list_2)
            new_dict.update(b_dict)

            new_list_3.append(p.get('Количество'))
            c_dict = dict(Количество=new_list_3)
            new_dict.update(c_dict)

            new_list_4.append(p.get('Ед'))
            d_dict = dict(Ед=new_list_4)
            new_dict.update(d_dict)
        else:
            continue
print(new_dict)
