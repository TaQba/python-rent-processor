import unittest
from parameterized import parameterized
from core.components.processor import Processor


class ProcessorTestCase(unittest.TestCase):
    def setUp(self):
        self.to_test = Processor()

    @parameterized.expand([
        ("2 and 3", 2, 3, 5),
        ("3 and 5", 3, 5, 8),
        ("3 and 10", 3, 10, 13),
    ])
    def test_zero(self, _, a, b, expected):
        self.assertEqual(a + b, expected)

    @parameterized.expand([
        ("Everything1", 'EverythingEverywhere Ltd & Hutchinson3GUK Ltd',
         'Everything Everywhere Ltd & Hutchison 3G UK Ltd'),
        ("Everything1", 'Everything Everywhere Ltd & Hutchinson 3G UK Ltd',
         'Everything Everywhere Ltd & Hutchison 3G UK Ltd'),
        ("Arqiva1", 'Arqiva Services ltd ', 'Arqiva Ltd'),
        ("Arqiva2", 'Arqiva  ltd ', 'Arqiva Ltd'),
        ("Arqiva3", 'Arqiva UK ltd ', 'Arqiva Ltd'),

    ])
    def test_fix_name(self, _, name, expected):
        self.assertEqual(
            self.to_test.fix_tenant_name(name),
            expected
        )

    def test_get_total_test(self):
        data = [
            {Processor.cn_c_rent: 12.12},
            {Processor.cn_c_rent: 13.13},
        ]
        self.assertEqual(
            self.to_test.get_total_rent(data),
            25.25
        )
