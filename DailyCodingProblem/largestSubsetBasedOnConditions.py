"""
Daily Coding Problem #198

This problem was asked by Google.

Given a set of distinct positive integers, find the largest subset 
such that every pair of elements in the subset (i, j) satisfies 
either i % j = 0 or j % i = 0.

For example, given the set [3, 5, 10, 20, 21], you should return 
[5, 10, 20]. Given [1, 3, 6, 24], return [1, 3, 6, 24].

"""
import itertools
def largest_subset(arr):
    l = len(arr)
    i = l
    while (i > 0):
        subsets = set(itertools.combinations(arr,i))
        for s in subsets:
            checker = set()
            pairs = set(itertools.combinations(s,2))
            for p in pairs:
                if (p[0]%p[1] == 0) or (p[1]%p[0] == 0):
                    checker.add("T")
                else:
                    checker.add("F")
            if len(checker) == 2:
                continue
            elif (len(checker) == 1) and ("T" in checker):
                return s
        i -= 1
    return "no subset satisfies required conditions"

print (largest_subset([3, 5, 10, 20, 21]))
print (largest_subset([1, 3, 6, 24]))