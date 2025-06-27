import unittest
from algorithms.math.gcd import gcd
from algorithms.math.lcm import lcm
from algorithms.math.sieve_of_eratosthenes import sieve

class TestGCD(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(gcd(48, 18), 6)

class TestLCM(unittest.TestCase):
    def test_lcm(self):
        self.assertEqual(lcm(4, 6), 12)

class TestSieve(unittest.TestCase):
    def test_primes(self):
        self.assertEqual(sieve(10), [2, 3, 5, 7])
        self.assertEqual(sieve(1), [])
        self.assertEqual(sieve(2), [2])