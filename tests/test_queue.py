import unittest
from data_structures.queue.queue import Queue

class TestQueue(unittest.TestCase):
    def test_queue_operations(self):
        q = Queue()
        self.assertTrue(q.is_empty())
        q.enqueue(10)
        q.enqueue(20)
        self.assertEqual(q.peek(), 10)
        self.assertEqual(q.dequeue(), 10)
        self.assertEqual(q.size(), 1)
        self.assertFalse(q.is_empty())