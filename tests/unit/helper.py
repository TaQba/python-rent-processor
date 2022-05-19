import unittest
from parameterized import parameterized
from core.components.helper import Helper


class ProcessorTestCase(unittest.TestCase):
    def setUp(self):
        self.to_test = Helper()

    @parameterized.expand([
        ("Test1", "21 Aug 2015", "21 Aug 2007", "20 Aug 2032", True),
        ("Fail 1", "20 Aug 2007", "21 Aug 2007", "20 Aug 2032", False),
        ("Fail 2", "21 Oct 2032", "21 Aug 2007", "20 Aug 2032", False),
        ("Exception", "foo", "bar", "noo", False),
    ])
    def test_compare_date(self, _, date, start, end, expected):
        self.assertEqual(
            self.to_test.between_dates(date, start, end),
            expected
        )

    @parameterized.expand([
        ("Test1", "21 Aug 2015", "21/08/2015"),
        ("Test2", "01 Jan 1999", "01/01/1999"),
    ])
    def test_change_date_format(self, _, date, expected):
        self.assertEqual(
            self.to_test.change_date_format(date),
            expected
        )
