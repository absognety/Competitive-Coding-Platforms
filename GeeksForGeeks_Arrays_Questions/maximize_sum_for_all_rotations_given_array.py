arr = list(map(int,input().strip().split()))
n = len(arr)

def sum_arrayInd(array):
    sums=0
    for i,v in enumerate(array):
        sums = sums + (i*v)
    return (sums)

def rotate(array,m):
    cutoff_arr = array[0:m]
    rotated_arr = array[m:] + cutoff_arr
    return (rotated_arr)

def main(arr,n):
    list_of_sums = []
    for i in range(n):
        rotatedArr = rotate(arr,i)
        sum_Arr = sum_arrayInd(rotatedArr)
        list_of_sums.append(sum_Arr)
    return (max(list_of_sums))

if __name__ == '__main__':
    print (main(arr, n))