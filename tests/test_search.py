import unittest
from algorithms.search.binary_search import binary_search
from algorithms.search.linear_search import linear_search
from algorithms.search.ternary_search import ternary_search
from algorithms.search.jump_search import jump_search
from algorithms.search.exponential_search import exponential_search
from algorithms.search.interpolation_search import interpolation_search


class TestBinarySearch(unittest.TestCase):
    def test_found(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)

    def test_not_found(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 6), -1)

class TestLinearSearch(unittest.TestCase):
    def test_linear(self):
        self.assertEqual(linear_search([3, 2, 1], 2), 1)
        self.assertEqual(linear_search([3, 2, 1], 4), -1)

class TestTernarySearch(unittest.TestCase):
    def test_ternary(self):
        self.assertEqual(ternary_search([1, 2, 3, 4, 5], 4), 3)

class TestJumpSearch(unittest.TestCase):
    def setUp(self):
        self.arr = list(range(0, 1000, 3))

    def test_jump_search(self):
        self.assertEqual(jump_search(self.arr, 0), 0)
        self.assertEqual(jump_search(self.arr, 998), -1)
        self.assertEqual(jump_search(self.arr, 300), 100)

class TestExponentialSearch(unittest.TestCase):
    def setUp(self):
        self.arr = list(range(0, 1000, 3))

    def test_exponential_search(self):
        self.assertEqual(exponential_search(self.arr, 0), 0)
        self.assertEqual(exponential_search(self.arr, 998), -1)
        self.assertEqual(exponential_search(self.arr, 300), 100)

class TestInterpolationSearch(unittest.TestCase):
    def setUp(self):
        self.arr = list(range(0, 1000, 3))

    def test_interpolation_search(self):
        self.assertEqual(interpolation_search(self.arr, 0), 0)
        self.assertEqual(interpolation_search(self.arr, 998), -1)
        self.assertEqual(interpolation_search(self.arr, 300), 100)