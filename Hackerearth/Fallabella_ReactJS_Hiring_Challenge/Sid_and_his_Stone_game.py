def minNumStones(n,m):
    total = (n*(n+1))//2
    return (abs(m-total))

if __name__ == '__main__':
    T = int(input())
    for tcase in range(T):
        N, M = list(map(int,input().strip().split()))
        print (minNumStones(N,M))