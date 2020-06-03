"""
Given an array with odd number of elements in which all elements occurring twice in
the array except for one element which occurs only once.

Find that element

Few solutions:
    1. Brute force approach (looping over the whole array and perform extensive search)
    2. Use a hashmap (store the frequencies of all the elements)
    3. Using bit-magic

"""

import collections
def findThatElement(array):
    n = len(array)
    if n%2 != 1:
        return "no element is occurring once"
    freqs = collections.Counter(array)
    for k,v in freqs.items():
        if v == 1:
            return k
        
def findThatElement2(array):
    x = 0
    for num in array:
        x ^= num
    return x
        
if __name__ == '__main__':
    array = [1,1,2]
    array2 = [1,1,2,2,11,11,3]
    
    print (findThatElement(array))
    print (findThatElement2(array))
    
    print (findThatElement(array2))
    print (findThatElement2(array2))