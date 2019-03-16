### count of Zeros in a matrix #####

def countZeros(matrix,n):
    totalCount = 0
    for e in range(n):
        totalCount += matrix[e].count(0)
    return (totalCount)
    
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
            print (countZeros(matrix,n))