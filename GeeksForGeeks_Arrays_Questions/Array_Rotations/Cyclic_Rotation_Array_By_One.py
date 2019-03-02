arr = list(map(int,input().strip().split()))
n = len(arr)

def cyclicRotation(arr,n):
    lastElement = arr[n-1]
    remaining_elements = arr[:n-1]
    new_array = [lastElement] + remaining_elements
    return (new_array)

if __name__ == '__main__':
    print (cyclicRotation(arr,n))