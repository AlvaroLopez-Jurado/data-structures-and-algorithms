import unittest
from data_structures.min_heap.min_heap import MinHeap

class TestMinHeap(unittest.TestCase):

    def setUp(self):
        self.heap = MinHeap()
        self.heap.push(10)
        self.heap.push(5)
        self.heap.push(20)

    def test_push_and_peek(self):
        self.assertEqual(self.heap.peek(), 5)

    def test_pop(self):
        self.assertEqual(self.heap.pop(), 5)
        self.assertEqual(self.heap.pop(), 10)
        self.assertEqual(self.heap.pop(), 20)
        self.assertIsNone(self.heap.pop())  # Empty heap

    def test_length(self):
        self.assertEqual(len(self.heap), 3)
        self.heap.pop()
        self.assertEqual(len(self.heap), 2)

if __name__ == "__main__":
    unittest.main()
