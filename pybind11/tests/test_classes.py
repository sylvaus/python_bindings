import unittest
from pybind_example.classes import Point, Rectangle


class ClassesTestCase(unittest.TestCase):
    def test_point(self):
        p = Point()
        self.assertAlmostEqual(p.x, 0.0)
        self.assertAlmostEqual(p.y, 0.0)
        p = Point(1.2, -45.68)
        self.assertAlmostEqual(p.x, 1.2)
        self.assertAlmostEqual(p.y, -45.68)

    def test_rectangle(self):
        r = Rectangle(Point(1.0, 2.0), Point(-1.0, -2.0))
        self.assertAlmostEqual(r.area(), 8)


