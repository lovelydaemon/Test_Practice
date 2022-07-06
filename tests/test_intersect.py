from task_01 import Rectangle, Point, are_intersect, are_intersect_x, are_intersect_y

rect1 = Rectangle(Point(1,1), Point(2,2))
rect2 = Rectangle(Point(3,3), Point(4,4))
rect3 = Rectangle(Point(1,1), Point(4,3))
rect4 = Rectangle(Point(3,-1), Point(6,2))
rect5 = Rectangle(Point(3,-8), Point(6,-10))
rect6 = Rectangle(Point(-1,-8), Point(-3,-10))
rect7 = Rectangle(Point(4,0), Point(5,1))

class TestIntersectX:
    """Intersection on X-axis"""
    def test_x_not_intersect(self):
        """Rectangles do not intersect on X-axis"""
        assert are_intersect_x(rect1, rect2) == False

    def test_x_intersect(self):
        """Rectangles intersect on X-axis"""
        assert are_intersect_x(rect3, rect4) == True

    def test_x_intersect_equal(self):
        """Rectangles have the same length on X-axis"""
        assert are_intersect_x(rect4, rect5) == True


class TestIntersectY:
    """Intersection on Y-axis"""
    def test_y_not_intersect(self):
        """Rectangles do not intersect on Y-axis"""
        assert are_intersect_y(rect4, rect5) == False

    def test_y_intersect(self):
        """Rectangles intersect on Y-axis"""
        assert are_intersect_y(rect4, rect3) == True

    def test_y_intersect_equal(self):
        """Rectangles have the same length on Y-axis"""
        assert are_intersect_y(rect5, rect6) == True


class TestIntersect:
    """Intersection on X,Y-axis"""
    def test_intersect(self):
        """Rectangles intersect on X,Y-axis"""
        assert are_intersect(rect4, rect3) == True

    def test_not_intersect(self):
        """Rectangles do not intersect on X,Y-axis"""
        assert are_intersect(rect1, rect2) == False

    def test_intersect_inside(self):
        """Rectangle is inside another rectangle"""
        assert are_intersect(rect4, rect7) == True
