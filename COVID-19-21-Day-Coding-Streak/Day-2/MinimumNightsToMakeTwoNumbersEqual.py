#User function Template for python3

def getPath(a, b):
    # the bfs queue
    queue = []

    # length[i] = length of the shortest
    # path to get from `a' to `i'
    length = {}

    # previous[i] = previous value reached
    # in the shortest path from `a' to `i'
    previous = {}

    # node with value `a' is the first in the path
    queue.append(a)
    length[a] = 0
    previous[a] = None

    while True:
        val = queue.pop(0)

        # add an element to the queue (if it was not
        # already visited
        def try_add(next_val):
            if next_val in length:
                return
            queue.append(next_val)
            length[next_val] = length[val] + 1
            previous[next_val] = val
        
        # add the allowed operations here
        try_add(val - 1)

        try_add(val * 2)

        # check whether we already have a solution
        if b in length:
            break

    path = [b]
    while True:
        if path[-1] == a:
            break
        else:
            path.append(previous[path[-1]])

    path.reverse()
    return path
    
    
def getDecision(m,n):
    #code here
    decisions = []
    Path = getPath(m,n)
    for u in range(1,len(Path)):
        if Path[u] == 2 * Path[u-1]:
            decisions.append("overflow")
        elif Path[u] == Path[u-1]-1:
            decisions.append("eat")
    return decisions[::-1]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

    
t=int(input())
for _ in range(0,t):
    m,n=list(map(int,input().split()))
    a=getDecision(m,n)
    print(*a[::-1])
            
# } Driver Code Ends