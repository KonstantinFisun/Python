#Треугольник, прямоугольник - переместить, сравнение по площади
from math import sqrt


class Triangle(object):

    # Конструктор
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.sides()
        self.square()


    # Длины сторон
    # d = √ (x2-x1)²+ (y2-y1)²)
    def sides(self):
        self.a = round(sqrt(pow((self.x2-self.x1),2) + pow((self.y2-self.y1),2)), 5)
        self.b = round(sqrt(pow((self.x3-self.x1),2) + pow((self.y3-self.y1),2)), 5)
        self.c = round(sqrt(pow((self.x3 - self.x2), 2) + pow((self.y3 - self.y2), 2)), 5)

    # Вывод сторон треугольника
    def print_sides(self):
        print(self.a, self.b, self.c)


    # Площадь
    # Формула площади S=sqrt(p*(p-a)(p-b)(p-c))
    def square(self):
        p = (self.a + self.b + self.c) / 2
        self.squ =  round(sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)), 5)

    # Вывод площади
    def print_square(self):
        print("Площадь треугольника: " + str(self.squ))

    # Перемещение
    def move(self, x, y):
        self.x1 += x
        self.y1 += y
        self.x2 += x
        self.y2 += y
        self.x3 += x
        self.y3 += y



class Rectangle(object):
    # Конструктор
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.sides()
        self.square()

    # Длины сторон
    def sides(self):
        self.a = abs(self.x1 - self.x2)
        self.b = abs(self.y1 - self.y2)

    # Вывод сторон треугольника
    def print_sides(self):
        print(self.a, self.b)

    # Площадь
    def square(self):
        self.squ = self.a * self.b

    # Вывод площади
    def print_square(self):
        print("Площадь прямоугольника: " + str(self.squ))

    # Перемещение
    def move(self, x, y):
        self.x1 += x
        self.y1 += y
        self.x2 += x
        self.y2 += y


# Сравнение по площади
def compare(object1,object2):
    print("Больше ")
    if object1.squ > object2.squ:
        object1.print_square()
    else:
        object2.print_square()


def main():
    triangle = Triangle(1, 1, 2, 2, 2, 1)
    rectangle = Rectangle(1, 1, 3, 2)
    compare(rectangle, triangle)


if __name__ == '__main__':
    main()


