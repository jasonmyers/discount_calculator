import unittest
from discount_calculator import DiscountCalculator

class DiscountCalculatorTests(unittest.TestCase):

    def test_ten_percent_discount(self):
        discount_calculator = DiscountCalculator()
        result = discount_calculator.calculate(100,10,'percent')
        self.assertEqual(10.0, result)

    def test_fifteen_percent_discount(self):
        discount_calculator = DiscountCalculator()
        result = discount_calculator.calculate(100,15,'percent')
        self.assertEqual(15.0, result)

    def five_dollar_discount_test(self):
        discount_calculator = DiscountCalculator()
        result = discount_calculator.calculate(250,5,'absolute')
        self.assertEqual(5.0, result)

    def test_invalid_discount_type(self):
        discount_calculator = DiscountCalculator()
        self.assertRaises(ValueError, discount_calculator.calculate, 100, 10, 'rupee')

    def test_floating_point_discount_percentage(self):
        discount_calculator = DiscountCalculator()
        result = discount_calculator.calculate(100,10.0,'percent')
        self.assertEqual(10.0, result)

    def test_floating_point_absolute_amount(self):
        discount_calculator = DiscountCalculator()
        result = discount_calculator.calculate(100,10.0,'absolute')
        self.assertEqual(10.0, result)

    def test_discount_percent_greater_than_hundred(self):
        discount_calculator = DiscountCalculator()
        self.assertRaises(ValueError, discount_calculator.calculate, 100,110,'percent')

    def test_absolute_discount_greater_than_amount(self):
        discount_calculator = DiscountCalculator()
        self.assertRaises(ValueError, discount_calculator.calculate, 100,110,'absolute')