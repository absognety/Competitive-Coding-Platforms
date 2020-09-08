"""
This question was asked by Google.

Given an N by M matrix consisting only of 1's and 0's, find the 
largest rectangle containing only 1's and return its area.

For example, given the following matrix:

[[1, 0, 0, 0],
 [1, 0, 1, 1],
 [1, 0, 1, 1],
 [0, 1, 0, 0]]

Return 4.

"""

# Python3 program to find largest rectangle  
# with all 1s in a binary matrix  
  
# Finds the maximum area under the histogram represented  
# by histogram. See below article for details.  
# https:# www.geeksforgeeks.org / largest-rectangle-under-histogram / def maxHist(row): 
  
def maxHist(R,C,row):
    # Create an empty stack. The stack holds  
    # indexes of hist array / The bars stored   
    # in stack are always in increasing order  
    # of their heights.  
    result = [] 
  
    top_val = 0     # Top of stack  
  
    max_area = 0 # Initialize max area in current  
                 # row (or histogram)  
  
    area = 0 # Initialize area with current top  
  
    # Run through all bars of given 
    # histogram (or row)  
    i = 0
    while (i < C):  
      
        # If this bar is higher than the  
        # bar on top stack, push it to stack  
        if (len(result) == 0) or (row[result[-1]] <= row[i]): 
            result.append(i) 
            i += 1
        else: 
          
            # If this bar is lower than top of stack,  
            # then calculate area of rectangle with  
            # stack top as the smallest (or minimum  
            # height) bar. 'i' is 'right index' for  
            # the top and element before top in stack 
            # is 'left index'  
            top_val = row[result[-1]]  
            result.pop(-1)  
            area = top_val * i  
  
            if (len(result)): 
                area = top_val * (i - result[-1] - 1 )  
            max_area = max(area, max_area)  
          
    # Now pop the remaining bars from stack  
    # and calculate area with every popped 
    # bar as the smallest bar  
    while (len(result)): 
        top_val = row[result[-1]]  
        result.pop(-1)  
        area = top_val * i  
        if (len(result)):  
            area = top_val * (i - result[-1] - 1 )  
  
        max_area = max(area, max_area)  
      
    return max_area  
  
# Returns area of the largest rectangle  
# with all 1s in A  
def maxRectangle(R,C,arr): 
      
    # Calculate area for first row and  
    # initialize it as result  
    result = maxHist(R,C,arr[0])  
  
    # iterate over row to find maximum rectangular  
    # area considering each row as histogram  
    for i in range(1, R): 
        for j in range(C): 
  
            # if A[i][j] is 1 then add A[i -1][j]  
            if (arr[i][j]): 
                arr[i][j] += arr[i - 1][j]  
  
        # Update result if area with current  
        # row (as last row) of rectangle) is more  
        result = max(result, maxHist(R,C,arr[i]))  
      
    return result  
      
# Driver Code  
if __name__ == '__main__': 
    arr1 = [[0, 1, 1, 0], 
         [1, 1, 1, 1],  
         [1, 1, 1, 1],  
         [1, 1, 0, 0]]  
    R = len(arr1)
    C = len(arr1[0])
    print("Area of maximum rectangle is",  
                         maxRectangle(R,C,arr1)) 
    
    arr2 = [[1, 0, 0, 0],
         [1, 0, 1, 1],
         [1, 0, 1, 1],
         [0, 1, 0, 0]]
    R = len(arr2)
    C = len(arr2[0])
    print("Area of maximum rectangle is",  
                         maxRectangle(R,C,arr2)) 
    
    arr3 = [[0, 1, 1],
            [1, 1, 1],
            [0, 1, 1]]
    R = len(arr3)
    C = len(arr3[0])
    print("Area of maximum rectangle is",  
                         maxRectangle(R,C,arr3)) 
    
    arr4 = [[1, 0, 0, 0],
             [1, 0, 1, 1],
             [1, 0, 1, 1],
             [0, 1, 0, 0]]
    R = len(arr4)
    C = len(arr4[0])
    print("Area of maximum rectangle is",  
                         maxRectangle(R,C,arr4)) 