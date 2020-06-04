"""
Given dollar_bills = [1,5,10,50,100] and given a value, what is the minumum
number of dollar bills we need to make that number (Assume operation sum)

Example:
    x = 105
    x = 100 + 5 (minimum number of dollar bills = 2)
    
Generalized:
    Given a number and array of numbers, what is the minumum number of elements
    from array needed such that their sum results in the given number.

"""

import itertools
def minimum_numbers(arr,k):
    for i in range(1,len(arr)):
        cbs = set(itertools.combinations(arr,i))
        for c in cbs:
            if sum(c) == k:
                return len(c)
    return "Given value cannot be achieved with given array elements"

if __name__ == '__main__':
    dollar_bills = [1,5,10,50,100]
    x = 105
    print (minimum_numbers(dollar_bills,x))
    
    arr = [2,4,10,-2,2]
    k = 4
    print (minimum_numbers(arr,k))