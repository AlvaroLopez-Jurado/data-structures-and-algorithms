import unittest
from algorithms.graphs.bfs  import bfs
from algorithms.graphs.dijkstra import dijkstra

class TestBFS(unittest.TestCase):
    def test_bfs_traversal(self):
        graph = {
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F'],
            'D': [],
            'E': ['F'],
            'F': []
        }
        self.assertEqual(bfs(graph, 'A'), ['A', 'B', 'C', 'D', 'E', 'F'])

class TestDijkstra(unittest.TestCase):
    def test_dijkstra(self):
        graph = {
            'A': [('B', 1), ('C', 4)],
            'B': [('C', 2), ('D', 5)],
            'C': [('D', 1)],
            'D': [],
        }
        expected = {'A':0, 'B':1, 'C':3, 'D':4}
        self.assertEqual(dijkstra(graph, 'A'), expected)
