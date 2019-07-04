#Traversing from one point to another point
#storing the minimum number of steps
def traversal_steps(A,B):
    points = list(zip(A,B))
    minSteps = 0
    for p in range(len(points)-1):
        #taking the manhattan distance between x and y-coordinates 
        d1 = abs(points[p][0] - points[p+1][0])
        d2 = abs(points[p][1] - points[p+1][1])
        #adding the maximum among the two to the running steps parameter
        minSteps += max(d1,d2)
    return (minSteps)
 
#Main Driver Code
if __name__ == '__main__':
    A = list(map(int,input().strip().split()))
    B = list(map(int,input().strip().split()))
    print (traversal_steps(A,B))