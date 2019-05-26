
def manhattanMatrix(arr,Sx,Sy,qArr):
    """
    Write Code Here
    """







if __name__ == '__main__':
    T = int(input())
    for tcase in range(T):
        N,M = list(map(int,input().strip().split()))
        arr = []
        for i in range(N):
            row = list(map(int,input().strip().split()))
            arr.append(row)
        Sx,Sy = list(map(int,input().strip().split()))
        Q = int(input())
        qArr = []
        for q in range(Q):
            xi,yi = list(map(int,input().strip().split()))
            qArr.append((xi,yi))
            