arr = list(map(int,input().strip().split()))
n = int(input())
def rotate(array,n):
    cutoff_arr = array[0:n]
    rotated_arr = array[n:] + cutoff_arr
    return (rotated_arr)

print (rotate(arr,n))