import random as r
import decimal as d
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции. # Пример:
# - [2, 3, 5, 9, 3] -> на нечётных индексы элементы 3 и 9, ответ: 12
print('\nЗадача 1. Найти сумму элементов списка с нечетными индексами')
l_1 = int(input('введите размер списка:'))
list_1 = []
sum_1 = 0
for i in range(l_1):
    list_1.append(r.randint(0, 9))
    if i % 2 != 0:
        sum_1 += list_1[i]
print(f'для списка {list_1} сумма элементов с нечетными индексами: {sum_1}')


# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
print('\nЗадача 2. Найти произведение пар чисел списка')
l_2 = int(input('введите размер списка:'))
list_2 = [r.randint(1, 9) for i in range(l_2)]
half_list = l_2//2 if l_2 % 2 == 0 else l_2//2 +1
l_product = [list_2[i] * list_2[l_2-i-1] for i in range(half_list)]
print(f'для списка {list_2} список произведений пар чисел списка: {l_product}')


# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19
print('\nЗадача 3. Найти  разницу между максимальным и минимальным значением дробной части элементов списка')
l_3 = int(input('введите размер списка:'))
list_int = [round(r.random() * r.randint(1, 100), 2) for i in range(l_3)]
dec_list = [list_int[i] % 1 for i in range(l_3)]
diff = max(dec_list)-min(dec_list)
print(f'{list_int} =>  {round(diff, 2)}')


# Напишите программу, которая будет преобразовывать десятичное число в двоичное (без встроенных функций).
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
print('\nЗадача 4. Преобразовать десятичное число в двоичное')


def bin_number(i):
    bin_list = []
    while i > 0:
        dig = i % 2
        bin_list.insert(0, dig)
        i = i//2
    return "".join([str(x) for x in bin_list])


int_number = int(input("Введите целое число: "))
print(f'{int_number} -> {bin_number(int_number)}')


# # Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# # Пример:#
# # для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
print('\nЗадача 5. задать натуральное число k, получить список Фибоначчи от f(-k) до f(k)')


def fibonacci(n):
    if n in {0, 1}:
        return n
    elif n == -1:
        return 1
    elif n == -2:
        return -1
    elif n > 0:
        return fibonacci(n - 1) + fibonacci(n - 2)
    else:
        return fibonacci(n + 2) - fibonacci(n + 1)


k = int(input("Введите целое число: "))
f_list = [fibonacci(i) for i in range(-k, k+1)]
print(f'для k = {k} список будет выглядеть так: {f_list}')
