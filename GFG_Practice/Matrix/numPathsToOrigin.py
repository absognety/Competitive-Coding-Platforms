import math
def numPaths(n,m):
    Z = math.factorial(n+m)
    X = math.factorial(n)
    Y = math.factorial(m)
    return (Z//(X*Y))
    

if __name__ == '__main__':
    T = int(input())
    for tcase in range(T):
        N, M = list(map(int,input().strip().split()))
        print (numPaths(N,M))