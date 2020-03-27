"""
Form an array of distinct elements with each element as sum of an element from each 
array


Given two arrays arr1[] and arr2[] of equal size which contains distinct elements, 
the task is to find another array with distinct elements such that elements of the 
third array are formed by the addition of the one-one element of the arr1[] and 
arr2[]

Input: arr[] = {1, 7, 8, 3}, arr2[] = {6, 5, 10, 2}
Output: 3 8 13 18
Explantion:
Index 0: 1 + 2 = 3
Index 1: 3 + 5 = 8
Index 2: 7 + 6 = 13
Index 3: 8 + 10 = 18
The elements of the array is distinct.

Input: arr1[] = {15, 20, 3}, arr2[] = {5, 4, 3}
Output: 6 19 25
Explanation:
Index 0: 3 + 3 = 6
Index 1: 15 + 4 = 19
Index 2: 20 + 5 = 25
The elements of the array is distinct.

"""

def thirdArray(arrA,arrB,n):
    third_array = [0]*n
    #sort two arrays
    arrA = sorted(arrA)
    arrB = sorted(arrB)
    #Loop to find the array  
    #such that each element is 
    #sum of other two elements 
    for i in range(n):
        third_array[i] = arrA[i] + arrB[i]
    return " ".join(str(q) for q in third_array)


if __name__ == '__main__':
    a = [1,7,8,3]
    b = [6,5,10,2]
    size = len(a)
    print (thirdArray(a,b,size))