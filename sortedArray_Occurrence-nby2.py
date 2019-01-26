# Python 3 code to find 
# majority element in a 
# sorted array 
  
def findMajority(arr, n): 
    return arr[int(n/2)] 
  
# Driver Code 
arr = [1, 2, 2, 3] 
n = len(arr)  
print(findMajority(arr, n)) 
  
