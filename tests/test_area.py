from task_01 import Rectangle, Point, area


rect1 = Rectangle(Point(1,1), Point(2,2))
rect2 = Rectangle(Point(3,3), Point(4,4))
rect3 = Rectangle(Point(1,1), Point(4,3))
rect4 = Rectangle(Point(3,-1), Point(6,2))
rect11 = Rectangle(Point(0,0), Point(5,5))
rect12 = Rectangle(Point(0,0), Point(1,1))

class TestArea:
    def test_area_intersect(self):
        """Return area"""
        assert area(rect3, rect4) == 1

    def test_area_not_intersect(self):
        """Rectangles do not intersect"""
        assert area(rect1, rect2) == 0

    def test_area_inside(self):
        """Rectangle is inside another rectangle"""
        assert area(rect1, rect11) == 1

    def test_area_borders(self):
        """Rectangles intersect by their borders"""
        assert area(rect1, rect12) == 0
