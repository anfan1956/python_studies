import math

# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

print('Задача 1.')
day_num = input('please enter the int number from 1 to 7\n')
if day_num.isdigit():
    if int(day_num) in range(1, 6):
        print(f'{day_num} -> нет')
    elif int(day_num) in range(6, 8):
        print(f'{day_num} -> да')
    else:
        print(f'{day_num}  -> не день недели')
else:
    print(f"{day_num} -> неверный тип данных на вводе")

# 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
print('\nЗадача 2', end='\n')
print('For any value of X, Y, Z - bool variables', end='\n')
print('the following is true:', end='\n')
Bool_space = [True, False]
for x in Bool_space:
    for y in Bool_space:
        for z in Bool_space:
            if not (x and y and z):
                print(f' if x = {x}, y = {y}, z = {z} -> {not x or not y or not z}')

# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости,в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
print('\nЗадача 3.')


def quarter(l, m):
    a = l > 0
    b = m > 0
    if a and b:
        return 1
    elif a and not b:
        return 4
    elif not a and b:
        return 2
    elif not a and not b:
        return 3


x = int(input('введите целое число x:\n'))
y = int(input('введите целое число y:\n'))
print(f'x = {x}; y = {y} -> {quarter(x, y)}')


# Напишите программу, которая по заданному номеру четверти, показывает
# диапазон возможных координат точек в этой четверти (x и y).

print('\nЗадача 4.')
quarter_num = int(input('введите номер четверти: \n'))

match quarter_num:
    case 1:
        print(f'четверть {quarter_num} -> x > 0 and y > 0')
    case 2:
        print(f'четверть {quarter_num} -> x < 0 and y > 0')
    case 3:
        print(f'четверть {quarter_num} -> x < 0 and y < 0')
    case 4:
        print(f'четверть {quarter_num} -> x > 0 and y < 0')
if quarter_num not in range (1, 5):
    print('Неверный ввод. Номер четверти - это число от 1 до 4 включительно')

# Задача 5. Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 2D пространстве.
# Пример:
#
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

print('\nЗадача 5.')
a = input('введите координаты x,y точки A в формате строки:\n')
b = input('введите координаты x,y точки B в формате строки:\n')

point_a = [int(x) for x in a.split(',')]
point_b = [int(x) for x in b.split(',')]
l_square = (point_a[0]-point_b[0])**2 + (point_a[1]-point_b[1])**2
l = math.sqrt(l_square)
l = round(l, 2)

print(f'A({a}); B({b}) -> {l}')
