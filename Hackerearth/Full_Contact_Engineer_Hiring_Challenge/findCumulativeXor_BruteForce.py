from itertools import combinations

def getXor(arr):
    xor = 0
    for i in arr:
        xor ^= i
    return xor


def getCountBruteForce1(arr, k):
    arr.sort()
    countGreaterThanK = 0
    for r in range(0, len(arr)+1):
        for comb in combinations(arr, r):
            xor = getXor(comb)
            if xor > k:
                countGreaterThanK += 1
    return(countGreaterThanK)


def getCountBruteForce2(arr, k):
    arr.sort()
    countLessThanK = 0
    for r in range(0, len(arr)+1):
        for comb in combinations(arr, r):
            xor = getXor(comb)
            if xor < k:
                countLessThanK += 1
    return(countLessThanK)