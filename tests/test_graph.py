import unittest
from data_structures.graph.graph import Graph

class TestGraph(unittest.TestCase):
    def test_graph(self):
        g = Graph()
        g.add_edge("A", "B")
        g.add_edge("A", "C")
        self.assertIn("B", g.get_neighbor("A"))
        self.assertIn("A", g.get_neighbor("B"))
        self.assertTrue(g.has_path_dfs("A", "B"))
        self.assertFalse(g.has_path_dfs("A", "Z"))

    def test_graph_directed(self):
        g = Graph(directed=True)
        g.add_edge("A", "B")
        self.assertIn("B", g.get_neighbor("A"))
        self.assertNotIn("A", g.get_neighbor("B"))
        self.assertTrue(g.has_path_dfs("A", "B"))
        self.assertFalse(g.has_path_dfs("B", "A"))