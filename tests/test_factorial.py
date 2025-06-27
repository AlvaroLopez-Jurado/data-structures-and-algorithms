import unittest
from algorithms.recursion.factorial import factorial
from algorithms.recursion.tower_of_hanoi import tower_of_hanoi

class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)

class TestTowerOfHanoi(unittest.TestCase):
    def test_hanoi(self):
        expected = [('A', 'C'), ('A', 'B'), ('C', 'B')]
        self.assertEqual(tower_of_hanoi(2, 'A', 'B', 'C'), expected)