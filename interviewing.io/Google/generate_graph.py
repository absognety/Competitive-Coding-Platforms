"""
Generate a graph from given list of words composed of characters:
    b, f, g, q
    
words:
    bgg
    fbq
    fqf
    ffq,
    gfg

Write methods for this graph as follows:
    class Graph:
        def add(self,c1,c2) => add edge between c1 and c2
        def remove(self,c1,c2) => removes edge between c1 and c2
        def outgoing(self,c) => returns a list of characters
        def incoming(self,c) => returns a list of characters
        
        
Solution:
    The graph data structure in python can be respresented best by dictionary 
    of sets or dictionary of lists with params (nodes, isDirected)
"""


alphabets = ['b','f','g','q']
words = ['bgg','fbq','fgf','ffq','gfg']

import pprint
import itertools
from collections import defaultdict

class Graph(object):
    """ 
    Graph data structure, undirected by default. 
    1. connections must be a list of tuples
    """

    def __init__(self, connections, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed
        self.add_connections(connections)

    def add_connections(self, connections):
        """ Add connections (list of tuple pairs) to graph """

        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        """ Add connection between node1 and node2 """

        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def remove_node(self, node):
        """ Remove all references to node """

        for n, cxns in self._graph.items():  # python3: items(); python2: iteritems()
            try:
                cxns.remove(node)
            except KeyError:
                pass
        try:
            del self._graph[node]
        except KeyError:
            pass
        
    def remove_edge(self,node1,node2):
        """Removes edge between 2 nodes"""
        
        if node1 in self._graph[node2]:
            self._graph[node2].remove(node1)
            
        if node2 in self._graph[node1]:
            self._graph[node1].remove(node2)
            
        return

    def is_connected(self, node1, node2):
        """ Is node1 directly connected to node2 """

        return node1 in self._graph and node2 in self._graph[node1]

    def find_path(self, node1, node2, path=[]):
        """ Find any path between node1 and node2 (may not be shortest) """

        path = path + [node1]
        if node1 == node2:
            return path
        if node1 not in self._graph:
            return None
        for node in self._graph[node1]:
            if node not in path:
                new_path = self.find_path(node, node2, path)
                if new_path:
                    return new_path
        return None

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))

connections = []
for w in words:
    pairs = set(itertools.combinations(w, 2))
    print (pairs)
    connections.extend(pairs)
    print (connections)
    
connections = list(set(connections))
g = Graph(connections=connections)
print (g._graph)

g.add('a','y')
g.add('v','w')
g.add('a','w')
g.add('w','y')

g.remove_edge('a','y')
g.remove_edge('f','q')
print (g._graph)