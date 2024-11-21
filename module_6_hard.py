import math

class Figure:
    sides_count = 0
    def __init__(self, __color: list, __sides: list):
        self.__sides = __sides # список сторон (int)
        self.__color = __color # список цветов (RGB)
        self.filled = False # закрашенный (bool)

    def get_color(self):
        return self.__color # возвращает список RGB цветов

    def __is_valid_color(self, r: int, g: int, b: int):
        if 0 < r <= 255 and 0 < g <= 255 and 0 < b <= 255: # Сделать красиво, например с циклом
            return True
        else:
            return False

    def set_color(self, r: int, g: int, b: int): # меняет цвет на заданный, если он правильно указан
        if self.__is_valid_color(r, g, b):
            self.__color[0] = r
            self.__color[1] = g
            self.__color[2] = b

    def __is_valid_sides(self, *side: int): # проверяет, что все стороны типа int и что совпадает кол-во сторон
        if all(type(i) is int for i in side) and len(side) == self.sides_count:
            return True
        else:
            return False

    def get_sides(self): # возвращает список сторон
        return self.__sides

    def __len__(self): # возвращает периметр фигуры
        per = 0
        for i in self.__sides:
            per += i
        return per
    
    def set_sides(self, *new_sides: int): # изменяет стороны фигуры
        if len(new_sides) == self.sides_count:
            self.__sides = new_sides
            
class Circle(Figure):
    sides_count = 1
    def __init__(self, __color: list, __sides: list, filled: bool):
        super().__init__(__color, __sides)
        self.__radius = __sides[0] / (2 * math.pi)

    def get_square(self):
            square_circle = math.pi * (self.__radius ** 2)
            return square_circle

class Triangle(Figure):
    sides_count = 3
    def __init__(self, __color: list, __sides: list, filled: bool):
        super().__init__(__color, __sides)

    def get_square(self):
            p = 0.5 * (self.__sides[0] + self.__sides[1] + self.__sides[2])
            square_triangle = math.sqrt(p * (p - self.__sides[0]) * (p - self.__sides[1]) * (p - self.__sides[2]))
            return square_triangle

class Cube(Figure):
    sides_count = 12
    def __init__(self, __color: list, __sides: list, filled: bool):
        super().__init__(__color, __sides)
        list_ = [] # новый список для подкорректированных сторон
        i = 0
        if len(self.__sides) == 1:
            while i < self.sides_count:
                list_.append(self.__sides[0])
                i += 1
        elif len(self.__sides) != 1: # или просто else
            while i < self.sides_count:
                list_.append(1)
                i += 1
        self.__sides = list_

    def get_volume(self):
        pass

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())