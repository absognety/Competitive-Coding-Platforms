"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Input: [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

"""
from typing import List

def setZerosMatrix(matrix:List[List[int]]) -> List[List[int]]:
    dmatrix1 = [None] * len(matrix)
    for r in range(len(matrix)):
        if 0 in matrix[r]:
            dmatrix1[r] = [0] * len(matrix[r])
        else:
            dmatrix1[r] = matrix[r]
    matrixT = list(zip(*matrix))
    dmatrix2 = [None] * len(matrixT)
    for r in range(len(matrixT)):
        if 0 in matrixT[r]:
            dmatrix2[r] = [0] * len(matrixT[r])
        else:
            dmatrix2[r] = matrixT[r]
    dmatrix2 = list(zip(*dmatrix2))
    zipd1d2 = list(zip(dmatrix1,dmatrix2))
    result = []
    for rw in zipd1d2:
        if rw[0].count(0) > rw[1].count(0):
            result.append(list(rw[0]))
        elif rw[0].count(0) < rw[1].count(0):
            result.append(list(rw[1]))
        else:
            result.append(list(rw[0]))
    return result


if __name__ == '__main__':
    matrix1 = [[1,1,1],[1,0,1],[1,1,1]]
    print (setZerosMatrix(matrix1))
    matrix2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    print (setZerosMatrix(matrix2))
    matrix3 = [[1,0,0,1,0],[2,1,5,0,0],[3,4,0,0,0],[0,0,0,0,0]]
    print (setZerosMatrix(matrix3))