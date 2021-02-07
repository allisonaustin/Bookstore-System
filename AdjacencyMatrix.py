"""An implementation of the adjacency list representation of a graph"""
from Interfaces import Graph, List
import numpy as np

class AdjacencyList(Graph):
    def __init__(self, n : int):
        self.n = n
        self.adj = np.zeros(n*n)
       
    def add_edge(self, i : int, j : int):
        # todo
        pass
        
    def remove_edge(self, i : int, j : int):
        # todo
        pass
                
    def has_edge(self, i : int, j: int) ->bool:
        # todo
        pass
        
    def out_edges(self, i) -> List:
        # todo
        pass

    def in_edges(self, i) -> List:
        # todo
        pass

    def dfs(self, r : int, dest: int):
        # todo
        pass
    
    def dfs(self, r : int, dest: int):
        # todo
        pass
                    
    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i,%r\n" % (i, self.adj[i].__str__())
        return s

'''
g = AdjacencyList(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(2, 4)
g.add_edge(4, 5)
g.add_edge(1, 4)
g.add_edge(4, 5)

print(g.dfs(0,1))

'''


