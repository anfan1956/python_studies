import os
import random as r
from decimal import *


print(f'\nЗадача 1. вычислить число PI с заданной точностью')
print('самый эффективный метод - с использованием рядов Нилаканта')


def pi_iterations(n):
    p = 4
    pi = 3.0
    k = 2
    while k in range(2, n):
        pi += p/k/(k+1)/(k+2)
        k += 2
        p *= -1
    return pi


dig = 0.00000001
not_enough_iterations = True
for n in range(2, 1000):
    if pi_iterations(n-1) < pi_iterations(n) < pi_iterations(n-1) + dig:
        print(f'для получения числа PI = {pi_iterations(n)} с точностью {dig} количество итераций = {n}')
        not_enough_iterations = False
        break
if not_enough_iterations:
    print('недостаточно циклов для выбранной точности')


print('\nЗадача2. Задайте натуральное число N. Напишите программу, которая составит')
print('список простых множителей числа N.')
# "20" -> [2, 2, 5]


def multipliers(n):
    multi = []
    for i in range(2, n):
        while n % i == 0:
            n = n // i
            multi.append(i)
    return multi


N = 120
print(f'{N} -> {multipliers(N)}')


print('\nЗадача 3. Задайте последовательность чисел. Напишите программу, которая выведет список')
print('неповторяющихся элементов исходной последовательности.')
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]
my_list = [1, 1, 2, 3, 4, 5, 5]
l = len(my_list)
no_repeat = [my_list[i] for i in range(l) if my_list.count(i) == 1]
print(f'{my_list} -> {no_repeat}')

print('\nЗадача 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов')
print('(значения от 0 до 100) многочлена и записать в файл многочлен степени k.')
print('решение задачи будет записано в двух файлах, для следующей задачи')
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


def str_polynom(k):  # generates polynom randomly with the highest power of k
    values = [r.randint(0, 100) for i in range(k+1)]
    polynome = str(values[0]) + ' + ' + str(values[1]) + ' * x'
    for j in range(2, k + 1):
        polynome = polynome + ' + ' + str(values[j]) + ' * x ** ' + str(j) if values[j] != 0 else ''
    polynome = polynome.split(' + ')
    polynome.reverse()
    return ' + '.join(polynome) + ' = 0'


def dict_poly(poly_sting):  # stores polynom parameters as dictionary
    l_poly = poly_sting.split(' + ')
    d_poly = {}
    for el in l_poly:
        key = el.split(' ')[-1] if el.split(' ')[-1].isdigit() else 1
        value = el.split(' ')[0]
        d_poly[key] = value
    return d_poly


def dict_poly_to_string(some_dict):  # generates polynom string from a polynom dictionary
    lst_pol = []
    for z, y in some_dict.items():
        if int(z) > 1:
            lst_pol.append(str(y) + ' * x' + ' ** ' + str(z))
        elif int(z) == 1:
            lst_pol.append(str(y) + ' * x')
        else:
            lst_pol.append(str(y))
    str_pol = ' + '.join(lst_pol)
    return str_pol


def dict_merge(d1, d2):  # merges two dictionaries summing the values for the same key
    for key in d2:
        if key in d1:
            d1[key] = int(d1[key]) + int(d2[key])
        else:
            d1[key] = int(d2[key])
    keys_values = d1.items()
    d1 = {str(key): str(value) for key, value in keys_values }

    return dict(sorted(d1.items(), reverse=True))


text_files = ('less4_1.txt', 'less4_2.txt')
counter = 1
for file in text_files:
    if os.path.exists(file):
        os.remove(file)
    f = open(file, 'a', encoding='utf-8')
    k = r.randint(2, 5)
    str_poly = str_polynom(k)
    f.write(f'{str_poly}')
    f.close()
    print(f'полином {counter}: {str_poly}')
    counter += 1

print('\nЗадача 5. Даны два файла (записаны в предыдущей задаче), в каждом из которых находится запись многочлена.')
print('Задача - сформировать файл, содержащий сумму многочленов.')
for file in text_files:
    f = open(file, 'r', encoding='utf-8')
    poly_f = f.read()
    dct_poly = dict_poly(poly_f)
    if file == 'less4_1.txt':
           d_1 = dct_poly
    else:
        d_2 = dct_poly
    # print(dct_poly)

print(f'для проверки dict из файла less4_1.txt: \n{d_1}\n и dict из файла less4_2.txt: \n{d_2}')

dict_final = dict_merge(d_1, d_2)
print(f'результирующий dict:\n{dict_final}')

file = 'less4_final.txt'
if os.path.exists(file):
    os.remove(file)
f = open(file, 'a', encoding='utf-8')
final_poly = dict_poly_to_string(dict_final)
f.write(final_poly)
print(f'сумма двух многочленов: {final_poly}')



