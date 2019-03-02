import math
arr = list(map(int,input().strip().split()))
n = len(arr)
key = int(input())

def binarySearch(arr,value):
    arr = sorted(arr)
    low=0
    high = len(arr)
    if value in arr:
        while (low<=high):
            mid = math.floor((high+low)/2)
            if (arr[mid]<value):
                low=mid+1
            elif (arr[mid]>value):
                high=mid-1
            else:
                return mid
    else:        
        return -1

def search_element(arr,key):
    diff = [x-arr[i-1] for i,x in enumerate(arr)][1:]
    sorted_diff = sorted(diff)
    ind = diff.index(sorted_diff[0])
    leftArray,rightArray = arr[:(1+ind)],arr[(1+ind):]
    if key > leftArray[0]:
        return (binarySearch(leftArray,key))
    else:
        return (binarySearch(rightArray,key) + len(leftArray))
    
if __name__ == '__main__':
    print (search_element(arr,key))