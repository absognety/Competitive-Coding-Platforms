"""
Given an array arr[] consisting of N positive integers and two positive 
integers A and B, the task is to replace each array element with the absolute 
difference of the nearest powers of A and B. If there exists two nearest 
powers, then choose the maximum of the two.

Examples:

Input: arr[] = {5, 12, 25}, A = 2, B = 3
Output: 1 7 5
Explanation:

For element arr[0]( = 5): The nearest power of 2 is 4 and the nearest power 
of 3 is 3. Therefore, the absolute difference of 4 and 3 is 1.
For arr[1]( = 12): The nearest power of 2 is 16 and the nearest power of 
3 is 9. Therefore, the absolute difference of 16 and 9 is 7.
For arr[2]( = 25): The nearest power of 2 is 32 and the nearest power of 
3 is 27. Therefore, the absolute difference of 27 and 32 is 5.
Therefore, the modified array is {1, 7, 5}.

Input: arr[] = {32, 3, 7}, a = 2, b = 3
Output: 0 1 1

"""

#Function to modify array elements 
#by absolute difference of the 
#nearest perfect power of a and b 
import math
def nearestPowerDiff(arr,m,n):
    for i in range(len(arr)):
        print (arr[i])
        p = math.floor(math.log(arr[i],m))
        q = math.floor(math.log(arr[i],n))
        p_1 = math.ceil(math.log(arr[i],m))
        q_1 = math.ceil(math.log(arr[i],n))

        if abs(pow(m,p) - arr[i]) == abs(pow(m,p_1) - arr[i]):
            p = max(p,p_1)
        elif abs(pow(m,p) - arr[i]) < abs(pow(m,p_1) - arr[i]):
            p = p
        elif abs(pow(m,p) - arr[i]) > abs(pow(m,p_1) - arr[i]):
            p = p_1
            
        if abs(pow(n,q) - arr[i]) == abs(pow(n,q_1) - arr[i]):
            q = max(q,q_1)
        elif abs(pow(n,q) - arr[i]) < abs(pow(n,q_1) - arr[i]):
            q = q
        elif abs(pow(n,q) - arr[i]) > abs(pow(n,q_1) - arr[i]):
            q = q_1
            
        if abs(pow(m,p) - arr[i]) == abs(pow(n,q) - arr[i]):
            ele = max(pow(m,p),pow(n,q))
            arr[i] = ele
        else:
            arr[i] = abs(pow(m,p) - pow(n,q))
    return arr

if __name__ == '__main__':
    arr = [5,12,25]
    a = 2
    b = 3
    print (nearestPowerDiff(arr,a,b))
    arr = [32,3,7]
    a = 2
    b = 3
    print (nearestPowerDiff(arr,a,b))