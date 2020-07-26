"""
Given an array, print the next biggest element for every element
of an array, the next biggest element of element x is the first 
greater element on the right side of x in array

for the last element, print -1

Input: [4,5,2,1,25]
Output: [5,25,25,25,-1]

Input: [11,3,7,6,11,12]
Output: [12,7,11,11,12,-1]

"""

#Brute force solution
def nextGreaterElement(arr):
    result = []
    for i in range(len(arr)):
        ele = arr[i]
        arr_n = arr[(i+1):]
        m = 0
        while (m <= len(arr_n)-1):
            if arr_n[m] > ele:
                result.append(arr_n[m])
                break
            else:
                m += 1
    result.append(-1)
    return result


#Optimal solution


if __name__ == '__main__':
    for tcase in range(T:=int(input())):
        arr = list(map(int,input().strip().split()))
        print (nextGreaterElement(arr))