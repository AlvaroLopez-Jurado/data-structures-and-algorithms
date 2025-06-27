class Graph:
    def __init__(self, directed=False):
        self.adjacency_list = {}
        self.directed = directed

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, v1, v2):
        self.add_vertex(v1)
        self.add_vertex(v2)
        self.adjacency_list[v1].append(v2)
        if not self.directed:
            self.adjacency_list[v2].append(v1)

    def get_neighbor(self, vertex):
        return self.adjacency_list.get(vertex, [])
    
    def has_path_dfs(self, start, end, visited=None):
        if visited is None:
            visited = set()
        
        if start == end:
            return True
        
        if start in visited:
            return False
        
        visited.add(start)
        for neighbor in self.get_neighbor(start):
            if self.has_path_dfs(neighbor, end, visited):
                return True
            return False
