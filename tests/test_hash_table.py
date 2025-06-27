import unittest
from data_structures.hash_table.hash_table import HashTable

class TestHashTable(unittest.TestCase):
    def test_hash_table(self):
        ht = HashTable()
        ht.set("name", "Alice")
        ht.set("age", 30)
        self.assertEqual(ht.get("name"), "Alice")
        self.assertEqual(ht.get("age"), 30)
        ht.delete("age")
        self.assertIsNone(ht.get("age"))
