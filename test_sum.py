import unittest
from sumNumbers import sumNun


class TestSumNun(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(sumNun(2, 3), 5)

    def test_negative_numbers(self):
        self.assertEqual(sumNun(-2, -3), -5)

    def test_mixed_numbers(self):
        self.assertEqual(sumNun(-2, 3), 1)

    def test_zero(self):
        self.assertEqual(sumNun(0, 5), 5)
        self.assertEqual(sumNun(0, 0), 0)


if __name__ == "__main__":
    unittest.main()
