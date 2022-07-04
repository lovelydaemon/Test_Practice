from main import Shape, Point, is_intersect, is_intersect_x, is_intersect_y

sh1 = Shape(Point(1,1), Point(2,2))
sh2 = Shape(Point(3,3), Point(4,4))
sh3 = Shape(Point(1,1), Point(4,3))
sh4 = Shape(Point(3,-1), Point(6,2))
sh5 = Shape(Point(3,-8), Point(6,-10))
sh6 = Shape(Point(-1,-8), Point(-3,-10))
sh7 = Shape(Point(4,0), Point(5,1))

class TestIntersectX:
    def test_x_not_intersect(self):
        """Прямоугольники не пересекаются"""
        assert is_intersect_x(sh1, sh2) == False

    def test_x_intersect(self):
        """Прямоугольники пересекаются"""
        assert is_intersect_x(sh3, sh4) == True

    def test_x_intersect_equal(self):
        """Прямоугольники одинаковой длины"""
        assert is_intersect_x(sh4, sh5) == True


class TestIntersectY:
    def test_y_not_intersect(self):
        """Прямоугольники не пересекаются"""
        assert is_intersect_y(sh4, sh5) == False

    def test_y_intersect(self):
        """Прямоугольники пересекаются"""
        assert is_intersect_y(sh4, sh3) == True

    def test_y_intersect_equal(self):
        """Прямоугольники одинаковой длины"""
        assert is_intersect_y(sh5, sh6) == True


class TestIntersect:
    def test_intersect(self):
        """Прямоугольники пересекаются"""
        assert is_intersect(sh4, sh3) == True

    def test_not_intersect(self):
        """Прямоугольники не пересекаются"""
        assert is_intersect(sh1, sh2) == False

    def test_intersect_inside(self):
        """Прямоугольник находится внутри другого прямоугольника"""
        assert is_intersect(sh4, sh7) == True

# Написать тесты где проверяется сразу несколько прямоугольников
