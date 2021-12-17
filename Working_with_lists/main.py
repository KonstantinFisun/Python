# Дано два множества: кол-во цветов кубиков и сами цвета

# Количество цветов первого
import random

# count_color_first = 5
# # Количество цветов второго
# count_color_second = 2
#
# # Цвета первого
# color_first = {"Красный", "Синий", "Голубой", "Зеленый", "Розовый"}
#
# # Цвета второго
# color_second = {"Зеленый", "Белый"}
#
# # Найти количество цветов и сами цвета, которые есть у обоих
#
# count_color_public = 0
# color_public = listt()
#
# for i in color_first:
#     if i in color_second:
#         count_color_public += 1
#         color_public.add(i)

# print(color_public)

# Найти количество цветов и сами цвета, которые есть хотя бы у одного


# Дано количество детей, для каждого известно языки которые он знает.
# Найти количество языков и сами языки которые знают все дети.
# Количество и сами языки которые знают хотя бы один.

# count_children = int(input("Введите количество детей"))
#
# language = ["Prolog", "Ruby", "Python", "C++", "C", "Java"]
#
# i = 0
# while i < count_children:
#
#     listt = []
#
#     learned_lang = random.randint(0, 6)
#     j = 0
#
#     while j < learned_lang:
#         listt.append(language[random.randint(0, len(language) - 1)])
#         j += 1
#
#     s1[i] = set(listt)
#
#     i += 1
#
# print(listt)

# Количество дней , количество политических партий, для каждой партии два числа
# Первый день забостовки, второй период с которым забостовка повторяется
# Первый день всегда понедельник, а суббота и воскресенье всегда выходные
# Сколько было рабочих дней всего

count_day = int(input("Количество дней : "))

count_party = int(input("Количество партий : "))

set_day = []

# Записываем количество дней
for i in range(1, count_day + 1):
    if (i % 7 != 6 and i % 7 != 0): set_day.append(i)

settl = set(set_day)

for i in range(0,count_party):
    first_day = int(input("Введите первый день забостовки"))
    period = int(input("Введите период"))

    #Удаляем дни забостовок
    j = first_day
    while j < count_day:
        settl.discard(j)
        j += period

print(settl)
print(len(settl))