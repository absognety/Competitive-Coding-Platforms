def startPoint(X,Y,numPaths,pointsList):
    currLocation = [X,Y]
    XCoords = [i[0] for i in pointsList]
    YCoords = [i[1] for i in pointsList]
    sumX = sum(XCoords)
    sumY = sum(YCoords)
    return (' '.join([str(currLocation[0]-sumX),str(currLocation[1]-sumY)]))
          
if __name__ == '__main__':
    T = int(input())
    for tcase in range(T):
        X, Y = list(map(int,input().strip().split()))
        numPaths = int(input())
        arr = list(map(int,input().strip().split()))
        pointsList = []
        for p in range(0,len(arr),2):
            pointsList.append(arr[p:p+2])
        print (startPoint(X,Y,numPaths,pointsList))