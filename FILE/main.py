# Первая строка входных данных содержит количество штатов в США N.
# Далее идет N строк, описывающих штаты США, каждая строка состоит из названия штата и числа выборщиков этого штата.
# Далее до конца файла идут записи результатов голосования по каждому из участников голосования.
# Одна строка соответствует одному избирателю. Записи имеют вид: название штата, имя кандидата, за которого проголосовал
# данный избиратель
# Вывести список кандидатов, упорядоченный по убыванию числа голосов выборщиков, полученных за данного кандидата.
# После имени кандидата вывести число набранных им голосов
import operator
from collections import OrderedDict
# Произвести ввод из файла
input_text = open('input2.txt', 'r')

# Количество штатов
count_state = int(input_text.readline())

# Считываем штат и количество выборщиков
state_elector = dict() # Ключ это штат, значение - количество выборщиков
i = 0
while i < count_state:
    str = input_text.readline().split() # Разделяем
    state_elector[str[0]] = int(str[1]) # Добавляем элементы в словарь
    i += 1

#print(state_elector)


# Считываем голоса
state_voice = dict() # Ключ - Штат,Кандидат ; Значение - количество голосов
for line in input_text:
    str = line.split()
    if (str[0], str[1]) in state_voice.keys(): state_voice[str[0], str[1]] += 1
    else: state_voice[str[0], str[1]] = 1


# print(state_voice)

result = dict()
for key,value in state_elector.items():
    max = -1
    name = ""

    # Находим в каждом штате победителя
    for j,g in state_voice.items():
        if key == j[0] and int(g) > max:
            max = int(g)
            name = j[1]
        else:
            if key == j[0] and int(g) == max and j[1]<name:
                name = j[1]
                max = int(g)

    # Победителю присваиваем все голоса от штата
    if name in result.keys(): result[name] += value
    else: result[name] = value

    # Добавляем кандидатов которые не победили
    for name in state_voice.keys():
        if name[1] not in result.keys(): result[name[1]] = 0

# Сортируем по значениям
res = list(result.items())
res.sort(key = lambda x : x[1], reverse = True)
for i in res:
    print(i[0],":",i[1])

input_text.close()
# for line in input_text:
#     print(line)
