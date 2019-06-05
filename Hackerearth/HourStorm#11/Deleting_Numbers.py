import itertools
import math
def DeletingNumbers(n,k,arr):
    if len(set(arr)) == len(arr):
        max_score = 0
        for t in list(itertools.combinations(arr,k)):
            array = [item for item in arr if item not in t]
            middle = array[math.floor((1 + len(array))/2) - 1]
            if max_score < middle:
                max_score = middle
    else:
        sort_arr = sorted(arr,reverse=True)
        arr_len = len(arr)
        max_score = sort_arr[math.floor((arr_len+1)/2)-1]
    return (max_score)
    

if __name__ == '__main__':
    n,k = list(map(int,input().strip().split()))
    arr = list(map(int,input().strip().split()))
    print (DeletingNumbers(n,k,arr))