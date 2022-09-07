import random as r

# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
#  - 0,56 -> 11

print('\nзадача 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.')
str_num = input("введите вещественное число:\n")
sum_digits = 0
for n in str_num:
    if n.isdigit():
        sum_digits += int(n)
print(f'{str_num} ->  {sum_digits}')

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

print('\nзадача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.')
num = int(input("введите целое число > 1:\n"))
factorial = 1
products = []
for i in range(num):
    factorial *= i + 1
    products.append(factorial)
print(f' - пусть N ={num}, тогда {products}')

print('\nЗадача 3.Задайте список из k чисел последовательности (1 + 1\\k)^k и выведите на экран их сумму.')
k = int(input("введите целое число > 1:\n"))
k_list = []
i = 1
k_sum = 0
while i in range(1, k+1):
    k_list.append((1 + 1/i) ** i)
    k_sum += (1 + 1/i) ** i
    i += 1
print(fr'для числа k = {k} сумма последовательности (1 + 1\k)^k: {k_list}: k_sum = {k_sum}')

print('Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].')
print('Найдите произведение элементов на указанных пользователем через пробел позициях.')
N = int(input("введите целое число > 1:\n"))

m_list = [r.randrange(-N, N+1) for x in range(N)]
print(m_list)
print(f'введите через пробел несколько целых чисел от  0 до {N-1} в возрастающем порядке')
print(f'последнее число введите без пробела')
a = input()
my_list = []
product = 1
while a.count(" ") > 0:
    product *= m_list[int(a)]
    my_list.append(int(a.strip(" ")))
    a = input()
product *= m_list[int(a)]
my_list.append(int(a.strip(" ")))
my_indices = ",".join(str(item) for item in my_list)
print(f'произведение элементов c индексами {my_indices} из списка: product = {product}')

print(f'\nЗадача 5.Реализуйте алгоритм перемешивания списка.')
the_list = ['ул. Вавилова', 'Москва', 'РФ', '121514', 'дом', 123]
print(f'оригинальный список: {the_list}')
r.shuffle(the_list)
print(f'после перемешивания функцией: {the_list}')

n = len(the_list)
for i in range(n):
    j = r.randint(0, n - 1)
    element = the_list.pop(j)
    the_list.append(element)
print("После перемешивания алгоритмом: ", the_list)

