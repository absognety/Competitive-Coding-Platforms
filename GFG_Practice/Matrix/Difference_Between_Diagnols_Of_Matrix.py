def diagnolDifference(matrix,n):
    numRows = len(matrix)
    numCols = len(matrix[0])
    d1 = 0
    d2 = 0
    for x in range(numRows):
        d1 += matrix[x][x]
    for y in range(numRows):
        d2 += matrix[y][numCols-1]
        numCols -= 1
    return (abs(d1-d2))

if __name__ == '__main__':
    T = int(input())
    for I in range(T):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        matrix = [[0 for i in range(n)] for j in range(n)]
        k=0
        for i in range(n):
            for j in range(n):
                matrix[i][j] = arr[k]
                k += 1
        print (diagnolDifference(matrix,n))