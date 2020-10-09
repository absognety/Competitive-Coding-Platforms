"""
Daily Coding Problem #160

This problem was asked by Uber.

Given a tree where each edge has a weight, compute the length of the 
longest path in the tree.

For example, given the following tree:

   a
  /|\
 b c d
    / \
   e   f
  / \
 g   h
 
and the weights: a-b: 3, a-c: 5, a-d: 8, d-e: 2, d-f: 4, e-g: 1, e-h: 1, 
the longest path would be c -> a -> d -> f, with a length of 17.

The path does not have to pass through the root, and each node can have 
any amount of children.

Solution:
    Refer Geeksforgeeks for base solution on top of which my solution is 
    built.

"""


from collections import deque
import string
 
class Graph:
 
    # Intialisation of graph
    def __init__(self, vertices):
 
        # No. of vertices
        self.vertices = vertices
 
        # adjacency list
        self.adj = {i: [] for i in range(self.vertices)}
        
        #weights for all pairs of edges
        self.distance = {}
 
    def addEdge(self, u, v,d):
        # add u to v's list
        self.adj[u].append(v)
        # since the graph is undirected
        self.adj[v].append(u)
        #store weight of the edge both ways
        #since graph is undirected
        self.distance[(u,v)] = d
        self.distance[(v,u)] = d
 
    # method return farthest node and its distance from node u
    def BFS(self, u):
        # marking all nodes as unvisited
        visited = [False for i in range(self.vertices + 1)]
        # mark all distance with -1
        distance = [-1 for i in range(self.vertices + 1)]
 
        # distance of u from u will be 0
        distance[u] = 0
        # in-built library for queue which performs fast 
        #oprations on both the ends
        queue = deque()
        queue.append(u)
        # mark node u as visited
        visited[u] = True
 
        while queue:
 
            # pop the front of the queue(0th element)
            front = queue.popleft()
            # loop for all adjacent nodes of node front
 
            for i in self.adj[front]:
                if not visited[i]:
                    # mark the ith node as visited
                    visited[i] = True
                    # make distance of i , one more than distance of front
                    #incase weights are not given otherwise, distance is
                    #incremented by the value of the edge
                    distance[i] = distance[front]+self.distance[(i,front)]
                    # Push node into the stack only if it is not 
                    #visited already
                    queue.append(i)
 
        maxDis = 0
 
        # get farthest node distance and its index
        for i in range(self.vertices):
            if distance[i] > maxDis:
 
                maxDis = distance[i]
                nodeIdx = i
 
        return nodeIdx, maxDis
 
    # method prints longest path of given tree
    def LongestPathLength(self):
 
        # first DFS to find one end point of longest path
        node, Dis = self.BFS(0)
 
        # second DFS to find the actual longest path
        node_2, LongDis = self.BFS(node)
 
        print('Longest path is from', node, 'to', node_2, 'of length', LongDis)
 
 
# create a graph given in the example
 
n = 8
G = Graph(n)
encode_nodes = {
     string.ascii_lowercase[i]:i for i in range(n)
    }
print (encode_nodes)
G.addEdge(encode_nodes['a'],encode_nodes['b'],3)
G.addEdge(encode_nodes['a'],encode_nodes['c'],5)
G.addEdge(encode_nodes['a'],encode_nodes['d'],8)
G.addEdge(encode_nodes['d'],encode_nodes['e'],2)
G.addEdge(encode_nodes['d'],encode_nodes['f'],4)
G.addEdge(encode_nodes['e'],encode_nodes['g'],1)
G.addEdge(encode_nodes['e'],encode_nodes['h'],1)
 
G.LongestPathLength()