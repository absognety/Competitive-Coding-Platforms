def transposeMatrix(matrix,n):
    numRows = len(matrix)
    numCols = len(matrix[0])
    result = ''
    c = 0
    for col in range(numCols):
        for row in range(numRows):
            result += ' ' + str(matrix[row][c])
        c += 1
    result = result[1:]
    return (' '.join(result.split(' ')))
    
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
        print (transposeMatrix(matrix,n))