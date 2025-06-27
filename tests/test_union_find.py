import unittest
from data_structures.union_find.union_find import UnionFind

class TestUnionFind(unittest.TestCase):

    def test_initial_state(self):
        uf = UnionFind(5)
        for i in range(5):
            self.assertEqual(uf.find(i), i)

    def test_union_and_find(self):
        uf = UnionFind(5)
        uf.union(0, 1)
        uf.union(1, 2)
        self.assertEqual(uf.find(0), uf.find(2))
        self.assertNotEqual(uf.find(0), uf.find(3))

    def test_union_idempotent(self):
        uf = UnionFind(3)
        self.assertTrue(uf.union(0, 1))
        self.assertFalse(uf.union(0, 1))  # Already connected

    def test_multiple_components(self):
        uf = UnionFind(6)
        uf.union(0, 1)
        uf.union(2, 3)
        uf.union(4, 5)
        self.assertNotEqual(uf.find(0), uf.find(2))
        self.assertNotEqual(uf.find(2), uf.find(4))
        self.assertEqual(uf.find(0), uf.find(1))
        self.assertEqual(uf.find(2), uf.find(3))
        self.assertEqual(uf.find(4), uf.find(5))

if __name__ == "__main__":
    unittest.main()
