"""
Daily Coding Problem #218

This problem was asked by Yahoo.

Write an algorithm that computes the reversal of a directed graph. 
For example, if a graph consists of A -> B -> C, it should become 
A <- B <- C.

"""

# Python3 program to find transpose of a graph.  
  
# function to add an edge from vertex  
# source to vertex dest  
def addEdge(adj, src, dest): 
    adj[src].append(dest) 
  
# function to pradjacency list  
# of a graph  
def displayGraph(adj, v): 
    for i in range(v): 
        print(i, "--> ", end = "") 
        for j in range(len(adj[i])): 
            print(adj[i][j], end = " ")  
        print() 
  
# function to get Transpose of a graph  
# taking adjacency list of given graph 
# and that of Transpose graph  
def transposeGraph(adj, transpose, v): 
      
    # traverse the adjacency list of given  
    # graph and for each edge (u, v) add  
    # an edge (v, u) in the transpose graph's 
    # adjacency list 
    for i in range(v): 
        for j in range(len(adj[i])): 
            addEdge(transpose, adj[i][j], i) 
  
# Driver Code 
if __name__ == '__main__': 
    
    #Example-1
    v = 5
    adj = [[] for i in range(v)]  
    addEdge(adj, 0, 1)  
    addEdge(adj, 0, 4)  
    addEdge(adj, 0, 3)  
    addEdge(adj, 2, 0)  
    addEdge(adj, 3, 2)  
    addEdge(adj, 4, 1)  
    addEdge(adj, 4, 3)  
  
    # Finding transpose of graph represented  
    # by adjacency list adj[]  
    transpose = [[] for i in range(v)] 
    transposeGraph(adj, transpose, v)  
  
    # displaying adjacency list of  
    # transpose graph i.e. b  
    displayGraph(transpose, v) 
    
    print ("\n\n")
    #Example-2
    v = 3
    adj = [[] for i in range(v)]
    nodes = {'A':0,'B':1,'C':2}
    addEdge(adj, nodes['A'], nodes['B'])
    addEdge(adj, nodes['B'], nodes['C'])
    
    transpose = [[] for i in range(v)]
    transposeGraph(adj, transpose, v)
    
    displayGraph(transpose, v)