"""
Daily Coding Problem #221

This problem was asked by Zillow.

Let's define a "sevenish" number to be one which is either a power 
of 7, or the sum of unique powers of 7. The first few sevenish 
numbers are 1, 7, 8, 49, and so on. Create an algorithm to find the 
nth sevenish number.

"""

import itertools
def nth_sevenish_number(n):
    a = 0
    i = 0
    sevenish_powers = []
    sums = []
    while True:
        #print (sevenish_powers)
        #print (sums)
        if i == n:
            break
        if len(sevenish_powers) < 2:
            sevenish_powers.append(pow(7,a))
        else:
            for r in range(2,len(sevenish_powers)+1):
                combinations = itertools.combinations(sevenish_powers,
                                                      r)
                for c in combinations:
                    sums.append(sum(c))
            sevenish_powers.append(pow(7,a))
        a,i = a + 1, i + 1
    union = set(sevenish_powers).union(set(sums))
    union = sorted(list(union))
    return union[n-1],union[:25]


print (nth_sevenish_number(5))
print (nth_sevenish_number(15))
print (nth_sevenish_number(20))
print (nth_sevenish_number(28))