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


if __name__ == '__main__':
    arr1 = [4,8,12,9,3]
    arr2 = [4,8,9,3]
    print (findMissing(arr1,arr2))