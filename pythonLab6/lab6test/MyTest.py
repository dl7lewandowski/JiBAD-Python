import unittest
from lab6.quadratic_and_line import*


class TestQuadratic(unittest.TestCase):


    def test_delta_equals_zero(self):
        self.assertCountEqual([-1], quadratic(2, 4, 2))

    def test_delta_grater(self):
        self.assertCountEqual((5, 2), quadratic(1, -7, 10))
        self.assertCountEqual((1, -3), quadratic(1, 2, -3))
        self.assertCountEqual((5, 2), quadratic(1, -7, 10))

    def test_delta_less_than_zero(self):
        self.assertCountEqual((), quadratic(2, 1, 3))

    def test_wrong_coefficients(self):
        self.assertRaises(ValueError, quadratic, 0, 0, 0)


class TestLinear(unittest.TestCase):

    def test_wrong_points(self):
        self.assertRaises(ValueError, linear, (0, 0), (0, 0))


    def test_linear_solution(self):
        self.assertCountEqual([1, 3], linear((2, 5), (1, 4)))
        self.assertCountEqual([-3, 2], linear((1, -1), (4, -10)))





if __name__ == '__main__':
    unittest.main()




