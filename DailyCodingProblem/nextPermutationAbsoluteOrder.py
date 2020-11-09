"""
Daily Coding Problem #205

This problem was asked by IBM.

Given an integer, find the next permutation of it in absolute order. 
For example, given 48975, the next permutation would be 49578.

Brute force approach:  
     Find all permutations of given number then find the one number with
     which given number has minimum difference but permutation - original > 0
"""

import itertools
def find_next_permutation(num):
    num_str = str(num)
    all_permutations = itertools.permutations(num_str,len(num_str))
    differences = dict()
    for p in all_permutations:
        perm = int("".join(p))
        if perm - num > 0:
            differences[(num,perm)] = perm - num
    #print (differences)
    differences = sorted(differences.items(),key=lambda x: x[1])
    return differences[0][0][1]

print (find_next_permutation(48975))