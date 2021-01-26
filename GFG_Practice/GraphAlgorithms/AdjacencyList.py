def addEdge(adj:list,u:int,v:int):
    adj[u].append(v)
    adj[v].append(u)

adj = None
def main(v:int):
    global adj
    adj = [[] for _ in range(v)]
    addEdge(adj,0,1)
    addEdge(adj,0,2)
    addEdge(adj,1,2)
    addEdge(adj,1,3)

main(4)
print (adj)