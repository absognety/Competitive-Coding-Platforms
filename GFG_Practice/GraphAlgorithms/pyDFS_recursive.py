
##Graph Data Structure##
"""
Using python dictionary to construct a graph.
1. Keys of a dictionary are used as nodes of a graph.
2. Values of each and every node are the list containing nodes
with which edges are shared.
"""

#import queue

graph ={'a':['c'],'b':['d'], 
        'c':['e'],'d':['a', 'd'], 
        'e':['b', 'c']}
visited_array=[]
result = []
def dfs_recursive(G,s,visited_array=[],rs=[]):
    #print (visited_array)
    visited_array.append(s)
    rs.append(visited_array)
    for w in G[s]:
        if w not in visited_array:
            dfs_recursive(G,w,visited_array=visited_array)
    return (rs[len(rs)-1])
            
print (dfs_recursive(graph,'a',visited_array=[],rs=[]))
print (dfs_recursive(graph,'b',visited_array=[],rs=[]))
print (dfs_recursive(graph,'c',visited_array=[],rs=[]))
print (dfs_recursive(graph,'d',visited_array=[],rs=[]))
print (dfs_recursive(graph,'e',visited_array=[],rs=[]))

#Output
#['a', 'c', 'e', 'b', 'd']
#['b', 'd', 'a', 'c', 'e']
#['c', 'e', 'b', 'd', 'a']
#['d', 'a', 'c', 'e', 'b']
#['e', 'b', 'c', 'd', 'a']