import unittest
from cython_example.structs import CPoint, CRectangle


class StructTestCase(unittest.TestCase):
    def test_point(self):
        p = CPoint()
        self.assertAlmostEqual(p.x, 0.0)
        self.assertAlmostEqual(p.y, 0.0)
        p = CPoint(1.2, -45.68)
        self.assertAlmostEqual(p.x, 1.2)
        self.assertAlmostEqual(p.y, -45.68)

    def test_rectangle(self):
        r = CRectangle()
        self.assertAlmostEqual(r.top_left.x, 0.0)
        self.assertAlmostEqual(r.top_left.y, 0.0)
        self.assertAlmostEqual(r.bottom_right.x, 0.0)
        self.assertAlmostEqual(r.bottom_right.y, 0.0)
        r = CRectangle(CPoint(1.0, 2.0), CPoint(-1.0, -2.0))
        self.assertAlmostEqual(r.top_left.x, 1.0)
        self.assertAlmostEqual(r.top_left.y, 2.0)
        self.assertAlmostEqual(r.bottom_right.x, -1.0)
        self.assertAlmostEqual(r.bottom_right.y, -2.0)


