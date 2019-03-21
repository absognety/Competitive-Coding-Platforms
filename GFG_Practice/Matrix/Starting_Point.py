def startPoint(X,Y,numPaths,pointsList):
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    T = int(input())
    for tcase in range(T):
        X, Y = list(map(int,input().strip().split()))
        numPaths = int(input())
        arr = list(map(int,input().strip().split()))
        pointsList = []
        for p in range(0,len(arr),2):
            pointsList.append(arr[p:p+2])