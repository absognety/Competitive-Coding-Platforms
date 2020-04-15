"""
Given an array of integers and an integer x. Find length of maximum size subarray having average of integers greater than or equal to x.

Examples:

Input : arr[] = {-2, 1, 6, -3}, x = 3
Output : 2
Longest subarray is {1, 6} having average
3.5 greater than x = 3.

Input : arr[] = {2, -3, 3, 2, 1}, x = 2
Output : 3
Longest subarray is {3, 2, 1} having 
average 2 equal to x = 2.

"""
# Function to find index in preSum list of tuples upto which 
# all prefix sum values are less than or equal to val. 
def findInd(preSum,n,val):
    #Starting and ending index of search space. 
    l=0
    h=n-1
    # To store required index value
    ans = -1
    # If middle value is less than or equal to 
    # val then index can lie in mid+1..n 
    # else it lies in 0..mid-1
    while (l <= h):
        mid = (l + h)//2
        if preSum[mid][0] <= val:
            ans = mid
            l = mid + 1
        else:
            h = mid - 1
    return ans


# Function to find Longest subarray having average 
# greater than or equal to x. 
def LongestSub(arr,n,x):
    #Update array by subtracting x from 
    #each element
    for i in range(n):
        arr[i] -= x
        
    # Length of Longest subarray. 
    maxlen = 0
    
    # To store current value of prefix sum. 
    total = 0
    
    # To store minimum index value in range 
    # 0..i of preSum vector.
    minInd = [None] * n
    
    # list to store pair of prefix sum 
    # and corresponding ending index value. 
    preSum = []
    
    # Insert values in preSum vector
    for i in range(n):
        total += arr[i]
        preSum.append((total,i))
    preSum = sorted(preSum)
    
    # Update minInd array.
    minInd[0] = preSum[0][1]
    for i in range(1,n):
        minInd[i] = min(minInd[i-1],preSum[i][1])
    total = 0
    for i in range(n):
        total += arr[i]
        
        # If sum is greater than or equal to 0, 
        # then answer is i+1
        if total >= 0:
            maxlen = i + 1
        
        # If sum is less than 0, then find if 
        # there is a prefix array having sum 
        # that needs to be added to current sum to 
        # make its value greater than or equal to 0. 
        # If yes, then compare length of updated 
        # subarray with maximum length found so far
        else:
            ind = findInd(preSum,n,total)
            if (ind != -1) & (minInd[ind] < i):
                maxlen = max(maxlen,i - minInd[ind])
    return maxlen

#Driver Code
if __name__ == '__main__':
    arr = [-2,1,6,-3]
    n = len(arr)
    x = 3
    a = [2,-3,3,2,1]
    m = len(a)
    y = 2
    print (LongestSub(arr,n,x))
    print (LongestSub(a,m,y))