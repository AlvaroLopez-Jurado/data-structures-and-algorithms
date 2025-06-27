import unittest
from data_structures.linked_list.singly_linked_list import SimplyLinkedList
from data_structures.linked_list.doubly_linked_list import DoublyLinkedList

class TestSinglyLinkedList(unittest.TestCase):
    def test_list_operations(self):
        lst = SimplyLinkedList()
        lst.insert_end(1)
        lst.insert_end(2)
        lst.insert_front(0)
        self.assertEqual(lst.to_list(), [0, 1, 2])
        lst.delete_value(1)
        self.assertEqual(lst.to_list(), [0, 2])
        lst.delete_value(0)
        self.assertEqual(lst.to_list(), [2])

class TestDoublyLinkedList(unittest.TestCase):
    def test_forward_backward(self):
        lst = DoublyLinkedList()
        lst.insert_end(1)
        lst.insert_end(2)
        lst.insert_end(3)
        self.assertEqual(lst.to_list_forward(), [1, 2, 3])
        self.assertEqual(lst.to_list_backward(), [3, 2, 1])