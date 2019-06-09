
##Graph Data Structure##
"""
Using python dictionary to construct a graph.
1. Keys of a dictionary are used as nodes of a graph.
2. Values of each and every node are the list containing nodes
with which edges are shared.
"""

import queue
graph ={'a':['c'],'b':['d'], 
        'c':['e'],'d':['a', 'd'], 
        'e':['b', 'c']}
visited_array = []

# Where G is the graph and s is the source node
def bfs(G,s,visited_array=[]):
    Q = queue.Queue(maxsize=len(G.keys()))  #Inserting s in queue until all its neighbour vertices are marked.
    Q.put(s)
    visited_array.append(s)
    while (Q.empty()==False):
        # Removing that vertex from queue,whose neighbour will be visited now
        v = Q.get()
        # processing all the neighbours of v
        for w in G[v]:
            if w not in visited_array:
                #Stores w in Q to further visit its neighbour
                Q.put(w)
                visited_array.append(w)
    return (visited_array)

print (bfs(graph,'a',visited_array=[]))
print (bfs(graph,'b',visited_array=[]))
print (bfs(graph,'c',visited_array=[]))
print (bfs(graph,'d',visited_array=[]))
print (bfs(graph,'e',visited_array=[]))


graph2 = {'0': ['1', '2'],
          '1': ['2'], '2': ['0', '3'], '3': ['3','2']}

print (bfs(graph2,'0',visited_array=[]))
print (bfs(graph2,'1',visited_array=[]))
print (bfs(graph2,'2',visited_array=[]))
print (bfs(graph2,'3',visited_array=[]))
