"""
Daily Coding Problem #186

This problem was asked by Microsoft.

Given an array of positive integers, divide the array into two 
subsets such that the difference between the sum of the subsets 
is as small as possible.

For example, given [5, 10, 15, 20, 25], return the sets {10, 25} 
and {5, 15, 20}, which has a difference of 5, which is the smallest 
possible difference.

"""
# iterative process ~ Brute force approach
# this prints any 2 subsets that generates minimum 
# difference of sums possible
import itertools
import collections
def partition_array(arr):
    l = len(arr)
    i = 0
    subset_partitions = dict()
    freqs = collections.Counter(arr)
    repeating = [k for k,v in freqs.items() if v > 1]
    while (i <= l):
        first = set(itertools.combinations(arr,i))
        for f in first:
            s = [x for x in arr if x not in f]
            if len(repeating) > 0:
                for r in repeating:
                    if f.count(r) + s.count(r) < arr.count(r):
                        balance = arr.count(r) - (f.count(r) + s.count(r))
                        s.extend([r] * balance)
            s = tuple(s)
            if (((f,s) not in subset_partitions) & 
               ((s,f) not in subset_partitions)):
               subset_partitions[(f,s)] = abs(sum(f) - sum(s))
        i += 1
    sorted_subsets = sorted(subset_partitions.items(),
                            key = lambda x: x[1])
    return sorted_subsets[0][0],sorted_subsets[0][1]

print (partition_array([5, 10, 15, 20, 25]))