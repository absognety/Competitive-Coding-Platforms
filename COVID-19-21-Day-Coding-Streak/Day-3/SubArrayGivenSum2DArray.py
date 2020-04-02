def is_rectangle_there(arr,n,x):
    arrays_sum = [sum(u) for u in arr]
    current_sum = 0
    start = 0
    end = -1
    hashMap = dict()
    for i in range(n):
        current_sum += arrays_sum[i]
        if current_sum - x == 0:
            start = 0
            end = i
            break
        if (current_sum-x) in hashMap:
            start = hashMap.get(current_sum-x)
            end = i
            break
        hashMap[current_sum] = i
    if end == -1:
        return False
    else:
        return True
        

if __name__ == '__main__':    
    t=int(input())
    for _ in range(t):
        n = int(input())
        line = input().strip().split()
        arr = [ [ int( line[i*n+j] ) for j in range(n) ] for i in range(n) ]
        x = int(input())
        if is_rectangle_there( arr, n, x) is True:
            print('Yes')
        else:
            print('No')