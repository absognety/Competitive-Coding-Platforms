arr = list(map(int,input().strip().split()))
n = len(arr)

def rotationCount(arr):
    sortedArr = sorted(arr)
    element = sortedArr[0]
    ind = arr.index(element)
    return (ind)

if __name__ == '__main__':
    print (rotationCount(arr))