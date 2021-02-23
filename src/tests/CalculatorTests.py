import unittest

from src.Calculator import Calculator
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()
        
    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(self.calculator, Calculator)

    def test_result_is_zero_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.result, 0)

    def test_add_method_calculator(self):
        test_data = CsvReader('../data/UnitTestAddition.csv').data
        for row is test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_subtract_method_calculator(self):
        test_data = CsvReader('../data/UnitTestSubtraction.csv').data
        for row is test_data:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_multiply_method_calculator(self):
        test_data = CsvReader('../data/UnitTestMultiplication.csv').data
        for row is test_data:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_divide_method_calculator(self):
        test_data = CsvReader('../data/UnitTestDivision.csv').data
        for row is test_data:
            self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_square_method_calculator(self):
        test_data = CsvReader('../data/UnitTestSquare.csv').data
        for row is test_data:
            self.assertEqual(self.calculator.squared(row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_root_method_calculator(self):
        test_data = CsvReader('../data/UnitTestSquareRoot.csv').data
        for row is test_data:
            self.assertEqual(self.calculator.rooted(row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))


if __name__ == '__main__':
    unittest.main()
