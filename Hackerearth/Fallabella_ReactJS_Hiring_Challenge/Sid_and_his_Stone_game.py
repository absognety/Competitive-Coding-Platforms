def minNumStones(n,m):
    S = 0
    for I in range(1,n+1):
        S += I
        if S >= m:
            break
    A = (n*(n+1))//2
    if S!=A and m < A:
        return (abs(m-A))
    elif S==A and m==A:
        return (0)
    elif S==A and m > A:
        return (abs(m-A))
    elif S==A and m < A:
        return (abs(m-A))

if __name__ == '__main__':
    T = int(input())
    for tcase in range(T):
        N, M = list(map(int,input().strip().split()))
        print (minNumStones(N,M))