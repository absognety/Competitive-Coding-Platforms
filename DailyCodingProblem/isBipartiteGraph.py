"""
Daily Coding Problem #207

This problem was asked by Dropbox.

Given an undirected graph G, check whether it is bipartite. Recall 
that a graph is bipartite if its vertices can be divided into two 
independent sets, U and V, such that no edge connects vertices of the 
same set.

Reference Implementation:

int n;
vector<vector<int>> adj;

vector<int> side(n, -1);
bool is_bipartite = true;
queue<int> q;
for (int st = 0; st < n; ++st) {
    if (side[st] == -1) {
        q.push(st);
        side[st] = 0;
        while (!q.empty()) {
            int v = q.front();
            q.pop();
            for (int u : adj[v]) {
                if (side[u] == -1) {
                    side[u] = side[v] ^ 1;
                    q.push(u);
                } else {
                    is_bipartite &= side[u] != side[v];
                }
            }
        }
    }
}

cout << (is_bipartite ? "YES" : "NO") << endl;

Example:
  edges = [
		(1, 2), (2, 3), (2, 8), (3, 4), (4, 6), (5, 7), (5, 9), (8, 9), (2, 4)
		# if we remove 2->4 edge, graph is becomes Bipartite
	]
"""

def is_bipartite(graph,n):
    color = [-1] * n
    #vis = [0] * 100011
    color[0] = 1
    q = [0]
    while (len(q)!=0):
        temp = q[0]
        q.pop(0)
        for i in range(n):
            if (graph[temp][i]) & (color[i] == -1):
                color[i] = 1 - color[temp]
                q.append(i)
            elif (graph[temp][i]) & (color[i] == color[temp]):
                return 0
    return 1

if __name__ == '__main__':
    n,e = list(map(int,input().strip().split()))
    graph = [[0 for p in range(n)] for q in range(n)]
    for i in range(e):
        x,y = list(map(int,input().strip().split()))
        x,y = x-1,y-1
        graph[x][y] = 1
        graph[y][x] = 1
    print (is_bipartite(graph,n))