# test_arithmetic.py
import unittest
from arithmetic import add, subtract, multiply, divide, modulus

class TestArithmetic(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(10, 5), 50)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(divide(10, 5), 2.0)
        self.assertEqual(divide(-1, 1), -1.0)
        self.assertEqual(divide(-1, -1), 1.0)
        self.assertRaises(ValueError, divide, 10, 0)  # Тестирование ошибки деления на ноль

    def test_modulus(self):
        self.assertEqual(modulus(10, 3), 1)
        self.assertEqual(modulus(10, 5), 0)
        self.assertEqual(modulus(-1, 2), 1)

if __name__ == '__main__':
    unittest.main()
