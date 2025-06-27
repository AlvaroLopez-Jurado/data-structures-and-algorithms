import unittest
from algorithms.dinamyc_programming.fibonacci import fibonacci
from algorithms.dinamyc_programming.knapsack import knapsack
from algorithms.dinamyc_programming.lcs import lcs
from algorithms.dinamyc_programming.lis import lis

class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(10), 55)

class TestKnapsack(unittest.TestCase):
    def test_basic_case(self):
        weights = [1, 2, 3]
        values = [10, 15, 40]
        capacity = 6
        self.assertEqual(knapsack(weights, values, capacity), 65)

    def test_zero_capacity(self):
        self.assertEqual(knapsack([1, 2, 3], [10, 15, 40], 0), 0)

    def test_empty_items(self):
        self.assertEqual(knapsack([], [], 10), 0)

    def test_large_input(self):
        weights = list(range(1, 101))
        values = list(range(1, 101))
        capacity = 250
        self.assertTrue(knapsack(weights, values, capacity) > 0)

class TestLCS(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(lcs("ABCBDAB", "BDCAB"), 4)

    def test_empty_strings(self):
        self.assertEqual(lcs("", ""), 0)

    def test_one_empty_string(self):
        self.assertEqual(lcs("ABC", ""), 0)
        self.assertEqual(lcs("", "DEF"), 0)

    def test_identical_strings(self):
        self.assertEqual(lcs("HELLO", "HELLO"), 5)

class TestLIS(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(lis([10, 22, 9, 33, 21, 50, 41, 60]), 5)

    def test_empty_array(self):
        self.assertEqual(lis([]), 0)

    def test_all_decreasing(self):
        self.assertEqual(lis([9, 8, 7, 6]), 1)

    def test_all_increasing(self):
        self.assertEqual(lis([1, 2, 3, 4, 5]), 5)

    def test_with_duplicates(self):
        self.assertEqual(lis([3, 4, 2, 1, 10, 6, 7]), 4)
