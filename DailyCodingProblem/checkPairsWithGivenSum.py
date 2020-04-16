def isPairWithGivenSum(arr,n,x):
    left,right = 0,n-1
    arr = sorted(arr)
    while left < right:
        if ((arr[left] + arr[right]) < x):
            left += 1
        elif (arr[left] + arr[right] == x):
            return True
        elif (arr[left] + arr[right] > x):
            right -= 1
    return False

if __name__ == '__main__':
    T = int(input())
    for tcs in range(T):
        arr = list(map(int,input().strip().split()))
        n = len(arr)
        x = int(input())
        print (isPairWithGivenSum(arr,n,x))