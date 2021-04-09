# Created by Leon Hunter at 11:23 AM 10/24/2020
from numbers import Number
from unittest import TestCase

from src.main.calculator import Calculator


class CalculatorTest(TestCase):
    def _test(self, method_to_test, value_sets):
        for value_set in value_sets:
            # given
            first_value = value_set[0]
            second_value = value_set[1]
            expected_calculation = value_set[2]

            # when
            actual_calculation = method_to_test(first_value, second_value)

            calculation_error_message = '''
            first_value = {}
            second_value = {}
            expected_calculation = {}
            actual_calculation = {}
            '''.format(first_value, second_value, expected_calculation, actual_calculation)

            return_type_error_message = '''
            expected return value of `{}` to be of type `Number`
            instead was of type `{}`
            '''.format(method_to_test.__name__, type(actual_calculation))

            # then
            self.assertTrue(isinstance(actual_calculation, Number), return_type_error_message)
            self.assertAlmostEqual(expected_calculation, actual_calculation, calculation_error_message)

    def test_add(self):
        self._test(Calculator().add, [
            (1, 3, 4),
            (5, 8, 13),
            (13, 21, 34),
            (0, 0, 0),
            (3, 1, 4),
            (8, 5, 13),
            (21, 13, 34),
        ])

    def test_subtract(self):
        self._test(Calculator().subtract, [
            (1, 3, -2),
            (5, 8, -3),
            (13, 21, -8),
            (0, 0, 0),
            (3, 1, 2),
            (8, 5, 3),
            (21, 13, 8),
        ])

    def test_multiply(self):
        self._test(Calculator().multiply, [
            (1, 3, 3),
            (5, 8, 40),
            (13, 21, 273),
            (0, 0, 0),
            (3, 1, 3),
            (8, 5, 40),
            (21, 13, 273),
        ])

    def test_divide(self):
        self._test(Calculator().divide, [
            (1, 3, .333),
            (5, 8, .625),
            (13, 21, .619),
            (0, 0, ZeroDivisionError),
            (3, 1, 3),
            (8, 5, 1.6),
            (21, 13, 1.615),
        ])
