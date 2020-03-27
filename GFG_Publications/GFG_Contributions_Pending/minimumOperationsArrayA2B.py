#python3 implementation to find the 
#minimum number of operations in 
#which the array A can be converted 
#to another array B 

#Given two arrays A[] and B[] of length N, the task is to find the 
#minimum number of operations in which the array A can be converted into 
#array B where each operation consists of adding an integer K into a subarray 
#from L to R.

"""
Input: A[] = {3, 7, 1, 4, 1, 2}, B[] = {3, 7, 3, 6, 3, 2}
Output: 1
Explanation:
In the above given example only one operation is required to convert from A to B: L = 3, R = 5 and K = 2
Array after the following operation:
Index 0: A[0] = 3, B[0] = 3
Index 1: A[1] = 7, B[1] = 7
Index 2: A[2] = 1 + 2 = 3, B[2] = 3
Index 3: A[3] = 4 + 2 = 6, B[3] = 6
Index 4: A[4] = 1 + 2 = 3, B[4] = 3
Index 5: A[5] = 2, B[5] = 2

Input: A[] = {1, 1, 1, 1, 1}, B[] = {1, 2, 1, 3, 1}
Output: 2
Explanation:
In the above given example only one operation is required to convert from A to B –
Operation 1: Add 1 to L = 2 to R = 2
Operation 2: Add 2 to L = 4 to R = 4

"""

# Utility function
def checkArray(arrA,arrB,n):
    operations = 0
    i = 0
    while(i < n):
        # if both elements are equal 
        # move to next element
        if ((arrA[i] - arrB[i])==0):
            i += 1
            continue
        # calculate the difference between
        # two elements
        diff = arrA[i] - arrB[i]
        i += 1
        # loop while next pair of elements have the same 
        # difference
        while ((i < n) & (arrA[i] - arrB[i] == diff)):
            i += 1
        #increase the number of 
        # operations required
        operations += 1
    return operations

# Driver code
if __name__ == '__main__':
    
    a = [3,7,1,4,1,2]
    b = [3,7,3,6,3,2]
    
    c = [1,1,1,1,1]
    d = [1,2,1,3,1]
    
    size1 = len(a)
    size2 = len(c)
    print (checkArray(a,b,size1))
    print (checkArray(c,d,size2))