# Дана строка, состоящая из слов разделенная пробелами
# Для каждого слова, посчитать сколько раз оно встречалась в строке
# print_string = input("Введите предложение: ") # Вводим предложение
# lower_string = [x.lower() for x in [print_string]] # Переводим все символы в нижний регистр
# string = "".join(lower_string) # Преобразуем список в лист
# words = string.split(" ") # Разделяем пробелами

# print("Полученные слова : ", words)

# Создадим множество из этих слов

# set_words = set(words) # Создали множество слов

# words_and_count = dict() # Пустой словарь

# for i in set_words:
#     # print(i, " встречается : ", words.count(i))
#     words_and_count[i] = words.count(i)

# print(words_and_count)

# Найти слово которое встречается чаще всего

# Находим самые частые слова
# max_count = max(words_and_count.values())
# max_list = [k for k, v in words_and_count.items() if v == max_count] # Находим все значение равные максу

# print("Самое часто встречающиеся слово: ", min(max_list))

# Даны пары слов, все различны слова
# Для заданного слова вывести его синоним

# pair = dict() # Создаем словарь, где ключ и значение это слова
# count_pair = 3
# print("Вводите пары")
# for i in range(count_pair):
#     pair[input()] = input()
#
# print(pair)
#
# get_word = input("Введите слово для которого нужно найти синоним: ")
#
# # pair.get(get_word)  # Ищем по ключу
#
# for k, v in pair.items():
#     if k == get_word:
#         print(v)
#         break
#     if v == get_word:
#         print(k)
#         break

# Дан список стран, и для каждой страны города
# Для заданного города, вывести страну

# country_city = {'Россия': ['Краснодар', 'Москва', 'СПБ'],
#                 'Китай': ['Шанхай', 'Пекин', 'Гонконг'],
#                 'США': ['Вашингтон', 'Нью-Йорк', 'Лас-Вегас']}
#
# get_city = input("Введите город: ")
#
# for k, v in country_city.items():
#     if get_city in v: print(k)

