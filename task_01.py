from dataclasses import dataclass


@dataclass
class Point:
    """Point on the X,Y-axis"""
    x: int
    y: int

class Rectangle:
    def __init__(self, point1:Point, point2:Point) -> None:
        """Creates a rectangle using 2 opposite points"""
        self.point1 = point1
        self.point2 = point2

    @property
    def len_x(self):
        """Return the length of X-axis"""
        return abs(self.point1.x - self.point2.x)

    @property
    def len_y(self):
        """Return the length of Y-axis"""
        return abs(self.point1.y - self.point2.y)

    @property
    def min_x(self):
        """Return the min. point on X-axis"""
        return min(self.point1.x, self.point2.x)

    @property
    def max_x(self):
        """Return the max. point on X-axis"""
        return max(self.point1.x, self.point2.x)

    @property
    def min_y(self):
        """Return the min. point on Y-axis"""
        return min(self.point1.y, self.point2.y)

    @property
    def max_y(self):
        """Return the max. point on Y-axis"""
        return max(self.point1.y, self.point2.y)

    @property
    def area(self):
        """Return the area of rectangle"""
        return self.len_x * self.len_y


def are_intersect_x(rect1:Rectangle, rect2:Rectangle) -> bool:
    """Return True if rectangles intersect on X-axis, otherwise False"""
    start = max(rect1.min_x, rect2.min_x)
    end = min(rect1.max_x, rect2.max_x)
    return end - start >= 0


def are_intersect_y(rect1:Rectangle, rect2:Rectangle) -> bool:
    """Return True if rectangles intersect on Y-axis, otherwise False"""
    start = max(rect1.min_y, rect2.min_y)
    end = min(rect1.max_y, rect2.max_y)
    return end - start >= 0


def are_intersect(rect1:Rectangle, rect2:Rectangle) -> bool:
    """Return True if rectangles intersect, otherwise False"""
    if not are_intersect_x(rect1, rect2) or \
        not are_intersect_y(rect1, rect2):
        return False
    return True


def area(rect1:Rectangle, rect2:Rectangle) -> int:
    """Return the area of the rectangles"""
    if not are_intersect(rect1, rect2): return 0
    left_x = max(rect1.min_x, rect2.min_x)
    left_y = max(rect1.min_y, rect2.min_y)
    right_x = min(rect1.max_x, rect2.max_x)
    right_y = min(rect1.max_y, rect2.max_y)
    new_rect = Rectangle(Point(left_x, left_y), Point(right_x, right_y))
    return new_rect.area


def get_first_index(array:str) -> int:
    """Return the lowest index of 0"""
    if not isinstance(array, str):
        raise TypeError('array must be str')

    if not array.isdecimal():
        raise ValueError('string contains not only numbers')
    return array.index('0')



if __name__ == '__main__':
    rect1 = Rectangle(Point(-5,2), Point(3,-2))
    rect2 = Rectangle(Point(0,6), Point(5,1))
    rect3 = Rectangle(Point(1,1), Point(2,2))
    rect4 = Rectangle(Point(2,2), Point(4,4))
    rect5 = Rectangle(Point(0,0), Point(1,1))

    print(are_intersect(rect1, rect2), area(rect1, rect2))
    print(are_intersect(rect3, rect4), area(rect3, rect4))

    print(get_first_index('111100000000000'))
