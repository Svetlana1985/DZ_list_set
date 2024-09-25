# Задание №1
# list_1 = [5, 6, 'hello', 8, 9, 6, 'hi', 158, 0]
# list_2 = [9, 8, 'hi', 'home', 10, 851, 158]
# list_3 = list(set(list_1) & set(list_2))
# print(list_3)

# Задание №2
# list_1 = [('Россия', 'Москва'), ('Китай', 'Пекин'),
#           ('Япония', 'Токио'), ('Англия', 'Лондон'),
#           ('Италия', 'Рим'), ('Франция', 'Париж')]
# # создание нового словаря
# dict_1 = dict()
# my_country = input('Введите название страны: ')
# for key, val in list_1:
#     dict_1.setdefault(key,val)
# # print(dict_1)
# if my_country in dict_1:
#     print(f'Столица: {dict_1[my_country]}')
# else:
#     print('Указанной страны нет в списке')

# Задание №3
# my_tuple = (['мандарин', 'оранжевый'], ['малина', 'красная'], ['помада', 'красная'], ['мандарин', 'сладкий'])
# # преобразовать в список
# my_list = []
# for i in my_tuple:
#     my_list.extend(i)
# # print(my_list)
# unique_list = []
# for x in my_list:
#     if x not in unique_list:
#         unique_list.append(x)
# print(unique_list)

# Задание №4
# my_str = 'hello', 'hi', 569, 965, 'bell', 0, 'hello', 569, 'hi'
# # конкатенация - сложение всех элементов строки
# my_str_concat = ','.join([str(item) for item in my_str])
# unique_set = set(my_str_concat)
# print(unique_set)

en_fr_dictionary = {
    'table' : 'tableau',
    'dog' : 'chien',
    'book' : 'livre',
    'woman' : 'femme',
}

while True:
    print('+ Добавить слово в словарь')
    print('- Удалить слово из словаря')
    print('* Поиск слова')
    print('/ Замена данных')
    print('0 Завершить программу')
    choice = input('Введите символ для работы со словарем: "+", "-", "*", "/": ')
    if choice == '+':
        en_word = input('Введите слово на английском языке: ')
        fr_word = input('Введите перевод слова на французский: ')
        if en_word not in en_fr_dictionary:
            en_fr_dictionary[en_word] = fr_word
            print(f'Слово {en_word} было добавлено')
        print(en_fr_dictionary)
    elif choice == '-':
        en_word = input('Введите слово, которое нужно удалить: ')
        if en_word in en_fr_dictionary:

            del en_fr_dictionary[en_word]
            print(f'Слово {en_word} удалено')
        else:
            print('Это слово отсутствует в словаре!')
        print(en_fr_dictionary)
    elif choice == '*':
        en_word = input('Введите слово, которое нужно найти: ')
        if en_word in en_fr_dictionary:
            word = en_fr_dictionary[en_word]
            print(f'Искомое слово {word}')
        else:
            print('Слово не найдено')
    elif choice == '/':
        en_word = input('Введите слово для замены: ')
        if en_word in en_fr_dictionary:
            fr_word = input('Введите новый перевод на французском: ')
            en_fr_dictionary[en_word] = fr_word
            print(f'Слово {en_word} обновлено')
        else:
            print('Слово не найдено')
        print(en_fr_dictionary)
    elif choice == '0':
        break











