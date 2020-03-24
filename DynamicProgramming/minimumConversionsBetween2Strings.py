"""
Edit Distance:
    
    The problem statement is like if we are given two string str1 and str2 
    then how many minimum number of operations can be performed on the str1 that 
    it gets converted to str2.
    
"""
def getMinConversions(str1,str2):
    numRows = len(str1) + 1
    numCols = len(str2) + 1
    distanceTable = [[0 for i in range(numCols)] for j in range(numRows)]
    for m in range(0,numRows,1):
        for n in range(0,numCols,1):
            if (m==0):
                distanceTable[m][n] = n
            elif (n==0):
                distanceTable[m][n] = m
            elif (str1[m-1] == str2[n-1]):
                distanceTable[m][n] = distanceTable[m-1][n-1]
            else:
                distanceTable[m][n] = min (1 + distanceTable[m-1][n],
                                           1 + distanceTable[m][n-1],
                                           1 + distanceTable[m-1][n-1])
    return distanceTable[numRows-1][numCols-1]