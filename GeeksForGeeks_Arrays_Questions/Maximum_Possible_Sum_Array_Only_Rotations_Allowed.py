arr = list(map(int,input().strip().split()))
n = len(arr)

def MPS_Rotations(arr,n):
    arrSum = sum(arr)
    currVal = 0
    for i, v in enumerate(arr):
        currVal += (i*v)
    maxVal = currVal
    for H in range(1,n):
        currVal = currVal + arrSum-(n*arr[n-H])
        if currVal > maxVal:
            maxVal = currVal
    return (maxVal)

if __name__ == '__main__':
    print (MPS_Rotations(arr, n))
