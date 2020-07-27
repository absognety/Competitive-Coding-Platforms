"""
Daily Coding problem #102

This problem was asked by Lyft.

Given a list of integers and a number K, return which contiguous 
elements of the list sum to K.

For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should 
return [2, 3, 4], since 2 + 3 + 4 = 9.

"""

def allSubArrays(L,L2=None):
    if L2==None:
        L2 = L[:-1]
    if L==[]:
        if L2==[]:
            return []
        return allSubArrays(L2,L2[:-1])
    return [L]+allSubArrays(L[1:],L2)


# return any list that sum to K
def get_elements(arr,k):
    for sub_arr in allSubArrays(arr):
        if sum(sub_arr) == k:
            return sub_arr
    return -1

#print all sub-arrays that sum to k
def get_elements_all(arr,k):
    for sub_arr in allSubArrays(arr):
        if sum(sub_arr) == k:
            print ("\n\nSecond function: ", sub_arr)
    return


if __name__ == '__main__':
    for tcase in range(T:=int(input())):
        arr = list(map(int,input().strip().split()))
        k = int(input())
        print ("First function: ",get_elements(arr, k))
        get_elements_all(arr, k)