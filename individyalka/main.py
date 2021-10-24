# Вариант 4
# Day, mice. "Year" is a mistake#

# Метод шифровки
string = input("Введите текст: ")  # Ввод предложения которое будем шифровать
spisok = []

i = 0
# Идем по символам
while string[i] != '#':
    if 'A' < string[i] < 'z': f = 1
    else:
        spisok.append(string[i])
        i += 1
        continue

    k = 0
    # Идем по слову пока не встретим не букву
    while 'A' < string[i] < 'z':
        i += 1
        k += 1 # Длина слова

    i -= k

    # Заменяем символы
    while 'A' < string[i] < 'z':
        new_a = ord(string[i]) + k
        if 96 < ord(string[i]) < 123: # строчные
            if new_a > 122: new_a = 97 + (new_a - 123)
        else: # прописные
            if new_a > 90: new_a = 65 + (new_a - 91)

        spisok.append(chr(new_a))
        i += 1
spisok.append('#')

print(''.join(spisok))





