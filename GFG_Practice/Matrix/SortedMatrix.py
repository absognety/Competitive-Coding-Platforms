def sortedMatrix(matrix,n):
    row = matrix[0]
    for r in matrix[1:]:
        row = row + r
    sorted_matrix = sorted(row)
    return (sorted_matrix)
    

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
        print (' '.join(str(i) for i in sortedMatrix(matrix,n)))