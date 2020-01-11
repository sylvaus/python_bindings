import unittest
from cython_example.cfunctions import print_hello, add
from cython_example.cppfunctions import plus_two_list


class FunctionsTestCase(unittest.TestCase):
    def test_print_hello(self):
        print_hello()

    def test_add(self):
        self.assertAlmostEqual(1, add(4, -3))

    def test_plus_two_list(self):
        self.assertEqual([3, 4, 5, 6], plus_two_list([1, 2, 3, 4]))


if __name__ == '__main__':
    unittest.main()
