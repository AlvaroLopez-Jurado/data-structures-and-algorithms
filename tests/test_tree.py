import unittest
from data_structures.tree.binary_search_tree import BinarySearchTree
from data_structures.tree.avl_tree import AVLTree, Node
from data_structures.tree.trie import Trie

class TestTrie(unittest.TestCase):
    def test_insert_and_search(self):
        trie = Trie()
        trie.insert("hello")
        self.assertTrue(trie.search("hello"))
        self.assertFalse(trie.search("hell"))

    def test_starts_with(self):
        trie = Trie()
        trie.insert("apple")
        self.assertTrue(trie.starts_with("app"))
        self.assertFalse(trie.starts_with("apl"))


class TestBinarySearchTree(unittest.TestCase):
    def test_operations(self):
        bst = BinarySearchTree()
        for val in [10, 5, 15, 3, 7]:
            bst.insert(val)
        self.assertEqual(bst.inorder_transversal(), [3, 5, 7, 10, 15])
        self.assertTrue(bst.search(5))
        self.assertFalse(bst.search(20))

class TestAVLTree(unittest.TestCase):
    def test_insert_balancing(self):
        tree = AVLTree()
        root = None
        for key in [10, 20, 30, 40, 50, 25]:
            root = tree.insert(root, key)
        self.assertEqual(root.key, 30)

    def test_single_rotation(self):
        tree = AVLTree()
        root = None
        for key in [30, 20, 10]:
            root = tree.insert(root, key)
        self.assertEqual(root.key, 20)

class TestTrie(unittest.TestCase):
    def test_insert_and_search(self):
        trie = Trie()
        trie.insert("hello")
        self.assertTrue(trie.search("hello"))
        self.assertFalse(trie.search("hell"))

    def test_starts_with(self):
        trie = Trie()
        trie.insert("apple")
        self.assertTrue(trie.starts_with("app"))
        self.assertFalse(trie.starts_with("apl"))
