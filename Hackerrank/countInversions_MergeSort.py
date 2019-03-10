def countInversions(arr,n):
    numInversions = 0
    i = 0
    while (i < len(arr)-1):
        if (arr[i] > arr[i+1]):
            tmp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = tmp
            i+=1
            numInversions+=1
        else:
            i+=1
    return (numInversions,arr)

if __name__ == '__main__':
    d = int(input())
    num_iterations = int(input())
    for xcase in range(d):
        n = int(input())
        arr = list(map(int,input().strip().split()))
        Total_Inversions = 0
        for X in range(num_iterations):
            numInversions,array = countInversions(arr,n)
            Total_Inversions += numInversions
        print (Total_Inversions)