"""
Given 2 arrays of distint elements, find one missing element from second
array that is present in first array

Example:
    findMissing([4,8,12,9,3],[4,8,9,3]) => 12
    
"""

#Using set() built-in function
def findMissing(arr1,arr2):
    res = set(arr1) - set(arr2)
    assert len(res) == 1,"there is more than one missing element"
    return list(res)[0]


#Using set() (O(N) and O(N) space)
def findMissing1(arr1,arr2):
    elems = set()
    for s in arr2:
        elems.add(s)
    for b in arr1:
        if b not in elems:
            return b
    return -1


#INT_LIMIT can exceed here in this solution
def findMissing2(arr1,arr2):
    return sum(arr1) - sum(arr2)

#To solve larger integers OVERFLOW problem
#Mostly this will occur in C/C++
def findMissing3(arr1,arr2):
    h1 = h2 = 0
    sums = 0
    while ((h1 < len(arr1)) and (h2 < len(arr2))):
        if sums < 0:
            sums += arr1[h1]
            h1 += 1
        else:
            sums -= arr2[h2]
            h2 += 1
    while (h1 < len(arr1)):
        sums += arr1[h1]
        h1 += 1
    while (h2 < len(arr2)):
        sums -= arr2[h2]
        h2 += 1
        
    return sums


if __name__ == '__main__':
    arr1 = [4,8,12,9,3]
    arr2 = [4,8,9,3]
    print (findMissing(arr1,arr2))
    print (findMissing1(arr1,arr2))
    print (findMissing2(arr1,arr2))
    print (findMissing3(arr1,arr2))