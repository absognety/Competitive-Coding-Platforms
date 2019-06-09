
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

### Depth First Search - Iterative ###
visited_array=[]
def dfs_iterative(G,s,visited_array=[]):
    S = queue.LifoQueue(maxsize=len(G.keys()))
    S.put(s)
    visited_array.append(s)
    while (S.empty()==False):
        v = S.get()
        S.put(v)
        S.get()
        for w in G[v]:
            if w not in visited_array:
                S.put(w)
                visited_array.append(w)
    return (visited_array)

#print depth first traversal resulting with different starting node.
print (dfs_iterative(graph,'a',visited_array=[]))
print (dfs_iterative(graph,'b',visited_array=[]))
print (dfs_iterative(graph,'c',visited_array=[]))
print (dfs_iterative(graph,'d',visited_array=[]))
print (dfs_iterative(graph,'e',visited_array=[]))

#Output
#['a', 'c', 'e', 'b', 'd']
#['b', 'd', 'a', 'c', 'e']
#['c', 'e', 'b', 'd', 'a']
#['d', 'a', 'c', 'e', 'b']
#['e', 'b', 'c', 'd', 'a']

#Sample Test case that can be taken

#testCase = {'1': ['2', '3'],
# '2': ['1', '4', '5'],
# '3': ['1', '5'],
# '4': ['2', '5', '6'],
# '5': ['2', '3', '4', '6'],
# '6': ['4', '5']}