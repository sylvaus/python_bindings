import unittest
from boost_example.classes import Point, Rectangle, Circle, Planet


class ClassesTestCase(unittest.TestCase):
    def test_point(self):
        p = Point()
        self.assertAlmostEqual(p.x, 0.0)
        self.assertAlmostEqual(p.y, 0.0)
        p = Point(1.2, -45.68)
        self.assertAlmostEqual(p.x, 1.2)
        self.assertAlmostEqual(p.y, -45.68)

    def test_rectangle(self):
        r = Rectangle()
        self.assertAlmostEqual(r.area(), 0)
        r = Rectangle(Point(1.0, 2.0), Point(-1.0, -2.0))
        self.assertAlmostEqual(r.area(), 8)
        self.assertAlmostEqual(r.is_shape(), True)

    def test_circle(self):
        c = Circle()
        self.assertEqual(c.area(), 0)
        c = Circle(Point(1.2, 3.5), 12)
        self.assertAlmostEqual(c.center.x, 1.2)
        self.assertAlmostEqual(c.center.y, 3.5)
        self.assertAlmostEqual(c.radius, 12)
        self.assertAlmostEqual(c.area(), 3.14159265359 * 12 * 12)

    def test_planet(self):
        p = Planet("mars", 123568.12)
        self.assertEqual(p.name, "mars")
        self.assertAlmostEqual(p.mass, 123568.12)


