import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.sum(2,2), 4)

    def test_subtract(self):
        self.assertEqual(calc.subtract(4,2), 2)

    def test_multiply(self):
        self.assertEqual(calc.multiply(4,2), 8)

    def test_divide(self):
        self.assertEqual(calc.divide(4,2), 2)
        self.assertRaises(calc.divide(4,0), )

if __name__ == '__main__':
    unittest.main()
