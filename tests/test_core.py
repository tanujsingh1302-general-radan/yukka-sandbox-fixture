import unittest

from calc import add, divide, mean


class CoreTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_divide(self):
        self.assertAlmostEqual(divide(1, 4), 0.25)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)

    def test_mean(self):
        self.assertEqual(mean([1, 2, 3, 4]), 2.5)

    def test_mean_empty(self):
        with self.assertRaises(ValueError):
            mean([])


if __name__ == "__main__":
    unittest.main()
