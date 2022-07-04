from dataclasses import dataclass

# что если после 0 где-то еще идут 1, а потом уже начинаются только 0
def get_first_index(array:str) -> int:
    """Return the lowest index of 0"""
    if not isinstance(array, str):
        raise TypeError('array must be str')

    if not array.isdecimal():
        raise ValueError('string contains not only numbers')
    return array.index('0')

ar1 = '1110000000000'
ar2 = '11100000000111100000000000000000'
print(get_first_index(ar1))
print(get_first_index(ar2))


# Задача про прямоугольники
@dataclass
class Point:
    """Точка с координатами x,y"""
    x: int
    y: int

class Shape:
    def __init__(self, point1:Point, point2:Point) -> None:
        """Прямоугольник задается двумя противоположными точками"""
        self.point1 = point1
        self.point2 = point2

    def get_len_x(self):
        """Длина по оси x"""
        return abs(self.point1.x - self.point2.x)

    def get_len_y(self):
        """Длина по оси y"""
        return abs(self.point1.y - self.point2.y)

    def get_min_x(self):
        """Мин между точками x"""
        return min(self.point1.x, self.point2.x)

    def get_max_x(self):
        """Макс между точками x"""
        return max(self.point1.x, self.point2.x)

    def get_min_y(self):
        """Мин между точками y"""
        return min(self.point1.y, self.point2.y)

    def get_max_y(self):
        """Макс между точками y"""
        return max(self.point1.y, self.point2.y)


shape1 = Shape(Point(-5,2), Point(3,-2))
shape2 = Shape(Point(2,6), Point(5,1))
shape3 = Shape(Point(1,1), Point(2,2))
shape4 = Shape(Point(3,2), Point(4,4))


def is_intersect_x(shape1:Shape, shape2:Shape) -> bool:
    """Пересечение по оси x"""
    max_point = shape1.get_max_x()
    min_point = shape1.get_min_x()
    return min_point <= shape2.get_min_x() <= max_point or \
            min_point <= shape2.get_max_x() <= max_point


def is_intersect_y(shape1:Shape, shape2:Shape) -> bool:
    """Пересечение по оси y"""
    max_point = shape1.get_max_y()
    min_point = shape1.get_min_y()
    return min_point <= shape2.get_min_y() <= max_point or \
            min_point <= shape2.get_max_y() <= max_point


# Возможно создать класс для проверки
# Туда подаются для прямоугольника
# У него дальше есть проверки по пересечениям
# А также он может найти площадь пересечения( Ну или любого из поданных прямоугольников)

def is_intersect(shape1:Shape, shape2:Shape) -> bool:
    x = False
    if shape1.get_len_x() >= shape2.get_len_x():
        x = is_intersect_x(shape1, shape2)
    else:
        x = is_intersect_x(shape2, shape1)

    y = False
    if shape1.get_len_y() >= shape2.get_len_y():
        y = is_intersect_y(shape1, shape2)
    else:
        y = is_intersect_y(shape2, shape1)

    return x and y

print(is_intersect(shape1, shape2))
# print(is_intersect(shape2, shape4))
