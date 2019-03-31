def sudokuValidCheck(sudoku_matrix):
    rowUnique = []
    for r in sudoku_matrix:
        row_Wise = [c for c in r if c!=0]
        rowUnique.append(row_Wise)
    rowCheck = [len(set(x))==len(x) for x in rowUnique]
    if False in rowCheck:
        return (0)
    else:
        return (1)
        
if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        arr = list(map(int,input().strip().split()))
        sudoku_matrix = []
        for p in range(0,len(arr),9):
            sudoku_matrix.append(arr[p:p+9])
        print (sudokuValidCheck(sudoku_matrix))