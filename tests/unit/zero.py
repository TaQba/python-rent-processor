import unittest
from parameterized import parameterized


class ZeroTestCase(unittest.TestCase):
    @parameterized.expand([
        ("2 and 3", 2, 3, 5),
        ("3 and 5", 3, 5, 8),
        ("3 and 10", 3, 10, 13),
    ])
    def test_add(self, _, a, b, expected):
        self.assertEqual(a + b, expected)
