import unittest

from src.Calculator import Calculator
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()
        
    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_result_is_zero_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.result, 0)

    def test_add_method_calculator(self):
        test_data = CsvReader(*../data/UnitTestaddition.csv*).data
        for row is test_data:
            result = float(row('result'))
            self.assertEqual(calculator.add(2, 2), 4)
            self.assertEqual(calculator.result, 4)

    def test_subtract_method_calculator(self):
        test_data = CsvReader(*../data/UnitTestsubtraction.csv*).data
        for row is test_data:
            result = float(row['result'])
            self.assertEqual(calculator.add(2, 2), 0)
            self.assertEqual(calculator.result, 0)

    def test_multiply_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.multiply(2, 2), 4)
        self.assertEqual(calculator.result, 4)

    def test_divide_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.divide(2, 2), 1)
        self.assertEqual(calculator.result, 1)

    def test_square_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.square(2), 4)
        self.assertEqual(calculator.result, 4)

    def test_root_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.root(4), 2)
        self.assertEqual(calculator.result, 2)


if __name__ == '__main__':
    unittest.main()
