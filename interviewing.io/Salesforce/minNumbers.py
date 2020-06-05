"""
Given dollar_bills = [1,5,10,50,100] and given a value, what is the minumum
number of dollar bills we need to make that number (Assume operation sum)

Example:
    x = 105
    x = 100 + 5 (minimum number of dollar bills = 2)
    
Generalized:
    Given a number and array of numbers, what is the minumum number of elements
    from array needed such that their sum results in the given number.
    
Solution:
    Approach-1: 
        1. itertools API solution used here doesn't take into consideration that
        elements can be repeated in achieving the sum
        Example:
            x = 173
            x = 100 + 50 + 10 + 10 + 1 + 1 + 1
            Here 10 is used twice and 1 thrice.
    Approach-2:
        2. greedy solution
        
    Approach-3:
        3. Modulo-operation (modification of Approach-2)
"""

#import itertools
#def minimum_numbers(arr,k):
#    #duplication is restricted here
#    for i in range(1,len(arr)):
#        cbs = set(itertools.combinations(arr,i))
#        for c in cbs:
#            if sum(c) == k:
#                return len(c)
#    return "Given value cannot be achieved with given array elements"


def minimum_numbers2(arr,k):
    result = 0
    arr = sorted(arr,reverse=True)
    while k > 0:
        for a in arr:
            if a <= k:
                k -= a
                result += 1
                break
    return result

def minimum_numbers3(arr,k):
    result = 0
    arr = sorted(arr,reverse=True)
    for a in arr:
        result += (k//a)
        k = k%a
    return result

if __name__ == '__main__':
    dollar_bills = [1,5,10,50,100]
    x = 105
    #print (minimum_numbers(dollar_bills,x))
    print (minimum_numbers2(dollar_bills,x))
    print (minimum_numbers3(dollar_bills,x))
    
    arr = [2,4,10,-2,2]
    k = 4
    #print (minimum_numbers(arr,k))
    print (minimum_numbers2(arr,k))
    print (minimum_numbers3(arr,k))