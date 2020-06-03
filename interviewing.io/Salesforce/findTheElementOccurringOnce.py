"""
Given an array with odd number of elements in which all elements occurring twice in
the array except for one element which occurs only once.

Find that element

Two solutions:
    1. Brute force approach (looping over the whole array and perform extensive search)
    2. Use a hashmap (store the frequencies of all the elements)

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
        
if __name__ == '__main__':
    array = [1,1,2]
    print (findThatElement(array))