import unittest
from data_structures.stack.stack import Stack

class TestStack(unittest.TestCase):
    def test_stack_operations(self):
        s = Stack()
        self.assertTrue(s.is_empty())
        s.push(1)
        s.push(2)
        self.assertEqual(s.peek(), 2)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.size(), 1)
        self.assertFalse(s.is_empty())
        s.pop()
        self.assertTrue(s.is_empty())

if __name__ == "__main__":
    unittest.main()