def get_word():  # генерирует случайное слово
    import random

    with open('words.txt', encoding='utf-8') as file:
        word = random.choice(file.read().split(','))
    return word.upper()


def letter_validation(letters_off):
    abc = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    letter_in = input('Введите букву: ').upper()

    if letter_in in letters_off:
        print('Вы вводили ранее эту букву')
        return letter_validation(letters_off)

    elif letter_in not in abc:
        print('Такой буквы нет в алфавитt русского языка')
        return letter_validation(letters_off)

    else:
        return letter_in


def gibbet(n):  # Рисует виселицу
    import json
    with open('gibbet.json') as file:
        a = json.load(file)
    return a[str(n)]


def start_menu():  # Выбор играть / не играть
    print('1 - Начать новую игру', '0 - Выйти из игры', sep='\n')
    a = int(input())
    if a == 1:
        play()
    if a == 0:
        print('До новых встреч!')


def play():
    letters_off = []  # использованные буквы
    lives = 6  # количество жизней

    word = get_word()

    print(f'Слово состоит из {len(word)} букв. У Вас есть право на 6 ошибок.')
    print(word)

    while lives > 0:

        # print()
        print('Использованы буквы:', *letters_off)
        for i in word:
            print(i if i in letters_off else '*', end='')
        print()

        letter_in = letter_validation(letters_off)
        letters_off.append(letter_in)

        if letter_in not in word:
            lives -= 1
            print(gibbet(5 - lives))

            if lives > 0:
                print(f'Такой буквы нет в слове. У Вас осталось попыток: {lives}')
            else:
                print('Вы проиграли. Конец игры.', f'Было загадано слово {word}')
                start_menu()

        elif letter_in in word:
            print('\n', 'Ура! Такая буква есть в слове.', sep='')

            if set(word).intersection(set(letters_off)) == set(word):
                print('Поздравляю! Вы победили!')
                lives = 0
                start_menu()


start_menu()
