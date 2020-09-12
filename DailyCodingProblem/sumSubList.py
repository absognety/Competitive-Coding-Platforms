"""
This Problem was asked by Goldman Sachs

Daily Coding Problem #149

Given a list of numbers L, implement a method sum(i, j) which returns 
the sum from the sublist L[i:j] (including i, excluding j).

For example, given L = [1, 2, 3, 4, 5], sum(1, 3) should return 
sum([2, 3]), which is 5.

You can assume that you can do some pre-processing. sum() should be 
optimized over the pre-processing step.

"""

def sublist_sum(arr,p,q):
    assert (p>=0) & (q<=len(arr)-1),"Given indices are not valid"
    return sum(arr[p:q])

print (sublist_sum([1,2,3,4,5],1,3))