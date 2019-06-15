import allPathsInaMatrix as aPIM
def KingsMarch(cb):
    aPIM.storePaths=''
    m = len(cb)
    n = len(cb[0])
    aPIM.findPaths(cb,m,n)
    myPaths = aPIM.storePaths.split('|')
    myPaths.remove('')
    myPaths = [p for p in myPaths if 'x' not in p]
    myPaths = [list(map(int,list(a)[1:len(a)-1])) for a in myPaths]
    if myPaths:
        myMax = max([sum(u) for u in myPaths])
        S = 0
        for H in myPaths:
            if sum(H)==myMax:
                S += 1
        return (myMax,S)
    else:
        return (0,len(myPaths))

if __name__ == '__main__':
    T = int(input())
    for tcase in range(T):
        n = int(input())
        chess_board = []
        for x in range(n):
            arr = input().strip().split()
            chess_board.append(arr)
        print (KingsMarch(chess_board))