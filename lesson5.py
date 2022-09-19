import random as r
import re

print('Задача 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".')
the_string = 'я лабвюблю проабвграммировать наабв питоабвне'
deletion = 'абв'
new_string = the_string.replace(deletion, '')
print(f'исходная строка: "{the_string}", \nрезультат: "{new_string}"')


# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
print('\nЗадача 2. Про конфеты')
print('Я - это бот. Я могу проиграть только если: \n'
      '    Партнер знает алгоритм и ход со стороны партнера,\n'
      '    или ход - мой, а остаток кратен (максимальному ходу  + 1)')


def next_move(balance, step):
    return balance % (step + 1)


left = 542
max_take = 128
print(f'начальные условия: количество конфет: {left}, максимальный ход: {max_take}')

note = 'Твой ход!'
my_move = r.getrandbits(1)

while left > 0:
    if my_move:
        print(f'Осталось {left} конфет. Я беру {next_move(left, max_take)}.', end='')
        left = left - next_move(left, max_take)
        my_move = False

        if left == 0:
            note = message = 'выиграл Я!'
            print(note)
            break
        else:
            print(note)
    else:
        partner_take = int(input(f'осталось {left} конфет. Партнер берет конфет: '))
        if partner_take not in range(1, max_take+1):
            print(f'    нужно брать от 1 до {max_take} конфет')
            continue
            # partner_take = int(input(f'осталось {left} конфет. Партнер берет конфет: '))
        else:
            left = left - partner_take
            my_move = True
            if left == 0:
                message = 'выиграл ПАРТНЕР'
                break

print('Игра закончена!')


print('\n\nЗадача 3. Крестики - нолики')
print('Я - это бот. Первый ход  -  всегда "X"')


def player_input(player_symbol):
    valid = False
    while not valid:
        the_answer = input('куда поставить ' + player_symbol + '? : ')
        try:
            the_answer = int(the_answer)
        except:
            print('ошибка ввода')
            continue
        if the_answer in range(1, 10):
            if str(board[the_answer-1]) not in 'XO':
                board[the_answer-1] = player_symbol
                valid = True
            else:
                print('Клетка занята')
        else:
            print('введите число от 1 до 9')


def draw_board(state):
    print('_' * 13)
    for i in range(3):
        print('|', state[0 + i * 3], '|', state[1 + i * 3], '|', state[2 + i * 3], '|')
        print('-' * 13)


def victory(state):
    vic_chain = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for chain in vic_chain:
        if board[chain[0]] == state[chain[1]] == state[chain[2]]:
            return board[chain[0]]
    return False


def main(state):
    counter = 0
    finished = False
    while not finished:
        draw_board(state)
        if counter % 2 == 0:
            player_input('X')
        else:
            player_input('O')
        counter += 1
        if counter > 4:
            current = victory(state)
            if current:
                print(f'Победа досталась {current}!!!')
                finished = True
                break
        if counter == 9:
            print('Ничья')
            break
    draw_board(board)


board = list(range(1, 10))
main(board)

print('\n\nВ следующей задаче рассмотрим генетическое моделирование.\n'
      'Нужно будет ввести число повторов')
repetitions = int(input('Введи число повторов ДНК группы от 2 до 5: '))


print('\nЗадача 4. \n\tКод любого гена может быть представлен четырьмя базовыми кислотами ДНК:\n'
      '\t\tadenine (A), cytosine (C), guanine (G) and thymine (T) \n'
      '\tГенерируем код случайным образом и выводим строку гена на экран.\n'
      '\tИспользуем алгоритм RLE для сжатия.\n'
      '\tПри случайной генерации кода коэффициент сжатия обычно меньше 1.\n'
      f'\tДля анализа эффективности сжатия используем параметр "число повторов = {repetitions}" \n'
      '\tЭто алгоритм RLE пригоден, если исходный код не содержит цифр\n')


def generate_gene(length, repeats):
    str_gene = ''
    gene_symbols = {1: 'A', 2: 'C', 3: 'G', 4: 'T'}
    genes_list = [gene_symbols[r.randint(1, 4)] for i in range(length)]
    for letter in genes_list:
        str_gene = str_gene + letter * repeats
    return str_gene


def rle_encode(some_string):
    rle_string = ""
    i = 0
    while i <= len(some_string)-1:
        count = 1
        ch = some_string[i]
        j = i
        while j < len(some_string)-1:
            if some_string[j] == some_string[j + 1]:
                count = count + 1
                j = j + 1
            else:
                break
        rle_string = rle_string + str(count) + ch
        i = j + 1
    return rle_string


def rle_decode(some_string):
    match_object = re.finditer(r'\d+', some_string)
    m_str = ''
    for match in match_object:
        m_str = m_str + rle_result[match.span()[1]+0] * int(match.group())
    return m_str


gene_length = 100
gene = generate_gene(gene_length, repetitions)
print(f'оригинальный код:\n{gene}')
rle_result = rle_encode(gene)
print(f'сжатый код:\n{rle_result}')
print(f'коэффициент сжатия: {round(len(gene)/len(rle_result), 2)}')
decode_rle = rle_decode (rle_result)
print(f'код гена после распаковки:\n{decode_rle}')














