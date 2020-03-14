import unittest
from boost_example.constants import PI, CONST_RAW_STRING, CONST_STRING, PRIME_NUMBERS


class AttributesTestCase(unittest.TestCase):
    def test_pi(self):
        self.assertAlmostEqual(PI, 3.14)

    def test_raw_string(self):
        self.assertEqual(CONST_RAW_STRING, "Const raw string")

    def test_string(self):
        self.assertEqual(CONST_STRING, "Const string")

    def test_vector(self):
        self.assertEqual(PRIME_NUMBERS, [2, 3, 5, 7, 11, 13, 17])